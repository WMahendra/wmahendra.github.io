/* Project-page visuals: a Leaflet map for georeferenced overlays and small
   CSV-driven charts. No build step and no framework; Leaflet is vendored
   locally. Everything degrades to the surrounding text if it fails. */
(function () {
  "use strict";

  var ACCENT = "#17627a", INK = "#23282d", MUTED = "#5c666f", LINE = "#e3e7ea";

  /* ---------- CSV ---------- */
  // Minimal RFC4180-ish parser: handles quoted fields containing commas.
  function parseCSV(text) {
    var rows = [], row = [], field = "", q = false, i, ch;
    for (i = 0; i < text.length; i++) {
      ch = text[i];
      if (q) {
        if (ch === '"') { if (text[i + 1] === '"') { field += '"'; i++; } else { q = false; } }
        else field += ch;
      } else if (ch === '"') q = true;
      else if (ch === ",") { row.push(field); field = ""; }
      else if (ch === "\n") { row.push(field); rows.push(row); row = []; field = ""; }
      else if (ch !== "\r") field += ch;
    }
    if (field.length || row.length) { row.push(field); rows.push(row); }
    if (!rows.length) return [];
    var head = rows.shift();
    return rows.filter(function (r) { return r.length === head.length; })
               .map(function (r) {
                 var o = {}; head.forEach(function (h, k) { o[h.trim()] = r[k]; }); return o;
               });
  }

  function fmt(n) {
    return n >= 1000 ? Math.round(n).toLocaleString() : (Math.round(n * 10) / 10).toLocaleString();
  }

  /* ---------- charts ---------- */
  function drawChart(fig) {
    var src = fig.dataset.src, xk = fig.dataset.x, yk = fig.dataset.y;
    var type = fig.dataset.type, ylabel = fig.dataset.ylabel || yk;
    var host = fig.querySelector(".csv-chart__canvas");
    fetch(src).then(function (r) {
      if (!r.ok) throw new Error(r.status);
      return r.text();
    }).then(function (txt) {
      var rows = parseCSV(txt)
        .map(function (d) { return { x: parseFloat(d[xk]), y: parseFloat(d[yk]) }; })
        .filter(function (d) { return isFinite(d.x) && isFinite(d.y); })
        .sort(function (a, b) { return a.x - b.x; });
      if (!rows.length) throw new Error("no rows");

      var W = 760, H = 300, m = { t: 14, r: 12, b: 38, l: 66 };
      var iw = W - m.l - m.r, ih = H - m.t - m.b;
      var ymax = Math.max.apply(null, rows.map(function (d) { return d.y; }));
      var step = Math.pow(10, Math.floor(Math.log10(ymax))) / 2;
      var top = Math.ceil(ymax / step) * step;
      var sx = function (i) { return m.l + (iw / rows.length) * (i + 0.5); };
      var sy = function (v) { return m.t + ih - (v / top) * ih; };

      var s = ['<svg viewBox="0 0 ' + W + ' ' + H + '" role="img" aria-labelledby="' +
               fig.id + '-t" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto">'];
      s.push('<title id="' + fig.id + '-t">' + ylabel + ' by year, ' +
             rows[0].x + ' to ' + rows[rows.length - 1].x + '</title>');

      // gridlines + y axis
      for (var g = 0; g <= 4; g++) {
        var v = top * g / 4, y = sy(v);
        s.push('<line x1="' + m.l + '" y1="' + y + '" x2="' + (W - m.r) + '" y2="' + y +
               '" stroke="' + LINE + '" stroke-width="1"/>');
        s.push('<text x="' + (m.l - 8) + '" y="' + (y + 4) + '" text-anchor="end" font-size="11" fill="' +
               MUTED + '">' + fmt(v) + '</text>');
      }
      // marks
      if (type === "line") {
        s.push('<path d="' + rows.map(function (d, i) {
          return (i ? "L" : "M") + sx(i).toFixed(1) + " " + sy(d.y).toFixed(1);
        }).join(" ") + '" fill="none" stroke="' + ACCENT + '" stroke-width="2"/>');
        rows.forEach(function (d, i) {
          s.push('<circle cx="' + sx(i).toFixed(1) + '" cy="' + sy(d.y).toFixed(1) +
                 '" r="2.5" fill="' + ACCENT + '"><title>' + d.x + ": " + fmt(d.y) + '</title></circle>');
        });
      } else {
        var bw = Math.max(4, (iw / rows.length) * 0.66);
        rows.forEach(function (d, i) {
          var h = m.t + ih - sy(d.y);
          s.push('<rect x="' + (sx(i) - bw / 2).toFixed(1) + '" y="' + sy(d.y).toFixed(1) +
                 '" width="' + bw.toFixed(1) + '" height="' + Math.max(0, h).toFixed(1) +
                 '" fill="' + ACCENT + '"><title>' + d.x + ": " + fmt(d.y) + '</title></rect>');
        });
      }
      // x labels, thinned so they never collide
      var every = Math.ceil(rows.length / 12);
      rows.forEach(function (d, i) {
        if (i % every) return;
        s.push('<text x="' + sx(i).toFixed(1) + '" y="' + (H - 16) + '" text-anchor="middle" font-size="11" fill="' +
               MUTED + '">' + d.x + '</text>');
      });
      s.push('<line x1="' + m.l + '" y1="' + (m.t + ih) + '" x2="' + (W - m.r) + '" y2="' + (m.t + ih) +
             '" stroke="' + INK + '" stroke-width="1"/>');
      s.push('<text x="' + m.l + '" y="' + (H - 2) + '" font-size="11" fill="' + MUTED + '">Year</text>');
      s.push('<text transform="translate(13,' + (m.t + ih / 2) + ') rotate(-90)" text-anchor="middle" font-size="11" fill="' +
             MUTED + '">' + ylabel + '</text>');
      s.push("</svg>");
      host.innerHTML = s.join("");
    }).catch(function () {
      host.innerHTML = '<p class="csv-chart__fallback">The chart could not be loaded. ' +
                       'The values are in <a href="' + src + '">the source CSV</a>.</p>';
    });
  }

  /* ---------- map ---------- */
  /* Basemaps are all key-free and usable on static hosting with attribution.
     CARTO was dropped because its anonymous endpoint now returns tiles stamped
     "API KEY REQUIRED" - they arrive with HTTP 200 and a valid image, so the
     failure was visible only on screen. Esri World Imagery is the default here
     because satellite context suits a forest-loss map; a muted street basemap
     and OpenStreetMap remain switchable. No Google endpoint is used, since
     those need credentials and their terms do not allow this kind of embed.
     maxNativeZoom is set per service so Leaflet upscales instead of requesting
     zoom levels a service does not publish, which would return blank tiles. */
  var ESRI = "https://server.arcgisonline.com/ArcGIS/rest/services/";
  var ESRI_ATTR = 'Tiles &copy; <a href="https://www.esri.com/">Esri</a>';

  function baseLayers() {
    var grayBase = L.tileLayer(ESRI + "Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}", {
      attribution: ESRI_ATTR + " &mdash; Esri, HERE, Garmin, &copy; OpenStreetMap contributors",
      maxZoom: 19, maxNativeZoom: 16
    });
    var grayRef = L.tileLayer(ESRI + "Canvas/World_Light_Gray_Reference/MapServer/tile/{z}/{y}/{x}", {
      maxZoom: 19, maxNativeZoom: 16, pane: "shadowPane"
    });
    return {
      "Satellite imagery": L.tileLayer(ESRI + "World_Imagery/MapServer/tile/{z}/{y}/{x}", {
        attribution: ESRI_ATTR + " &mdash; Source: Esri, Maxar, Earthstar Geographics and the GIS User Community",
        maxZoom: 19, maxNativeZoom: 18
      }),
      "Light basemap": L.layerGroup([grayBase, grayRef]),
      "OpenStreetMap": L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        maxZoom: 19
      })
    };
  }

  function drawMap(el) {
    if (typeof L === "undefined") return;
    var canvas = el.querySelector(".geo-map__canvas");
    var b = (el.dataset.bounds || "").split(",").map(parseFloat);
    if (b.length !== 4 || b.some(isNaN)) return;
    var bounds = [[b[0], b[1]], [b[2], b[3]]];

    var map = L.map(canvas, { scrollWheelZoom: false, zoomControl: true });
    var bases = baseLayers();
    bases["Satellite imagery"].addTo(map);

    var overlays = {};
    if (el.dataset.overlay) {
      var img = L.imageOverlay(el.dataset.overlay, bounds, { opacity: 0.85,
        alt: "Tree-cover loss year, 2001 to 2023" }).addTo(map);
      overlays["Tree-cover loss year"] = img;
    }
    map.fitBounds(bounds);

    /* One layer control, added once the optional outline has resolved either
       way, so the basemap switcher still works if the GeoJSON fails to load. */
    function addControl() {
      L.control.layers(bases, overlays, { collapsed: true, position: "topright" }).addTo(map);
    }

    if (el.dataset.outline) {
      fetch(el.dataset.outline).then(function (r) { return r.json(); }).then(function (gj) {
        overlays["West Kalimantan provincial boundary"] =
          L.geoJSON(gj, { style: { color: "#ffffff", weight: 1.6, fill: false,
                                   dashArray: "4 3", opacity: 0.95 } }).addTo(map);
        addControl();
      }).catch(addControl);
    } else {
      addControl();
    }
    L.control.scale({ imperial: false }).addTo(map);
    map.on("focus", function () { map.scrollWheelZoom.enable(); });
    map.on("blur", function () { map.scrollWheelZoom.disable(); });
  }

  function init() {
    document.querySelectorAll(".csv-chart").forEach(drawChart);
    document.querySelectorAll(".geo-map").forEach(drawMap);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
