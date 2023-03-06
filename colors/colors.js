import { app } from "../scripts/app.js";

// use HSL color space to generate a different color for each keys
function generateColors(keys, S, L, Hmin = 0, Hmax = 360) {
    var colors = {};
    
    var Hstep = Math.round((Hmax - Hmin) / keys.length);
    
    for (var i = 0; i < keys.length; i++)
    {
        var currentType = keys[i];

        var H = Hmin + (i * Hstep);
        var hexadecimal = hslToHex(H, S, L);

        colors[currentType] = hexadecimal;
    }

    return colors;
}

// from https://stackoverflow.com/a/44134328
function hslToHex(h, s, l) {
    l /= 100;
    const a = s * Math.min(l, 1 - l) / 100;
    const f = n => {
      const k = (n + h / 30) % 12;
      const color = l - a * Math.max(Math.min(k - 3, 9 - k, 1), -1);
      return Math.round(255 * color).toString(16).padStart(2, '0');   // convert to Hex and prefix "0" if needed
    };
    return `#${f(0)}${f(8)}${f(4)}`;
}

const ext = {
    name: "m957ymj75urz.colors",
    async addCustomNodeDefs(defs, app) {
        var categories = [...new Set(Object.entries(defs).map(o => o[1].category).sort())];
        this.categoryColors = generateColors(categories, 30, 26);

        var types = [...new Set(Object.entries(defs).map(o => o[1].output).flat().sort())];
        this.linkColorsOn = generateColors(types, 50, 73);
        this.linkColorsOff = generateColors(types, 25, 50);
    },
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        nodeType.color = this.categoryColors[nodeData.category];
    },
    async registerCustomNodes(app) {
        LGraphCanvas.link_type_colors = {...LGraphCanvas.link_type_colors, ...this.linkColorsOn};
        app.canvas.default_connection_color_byType = {...LGraphCanvas.default_connection_color_byType, ...this.linkColorsOn};
        app.canvas.default_connection_color_byTypeOff = {...LGraphCanvas.default_connection_color_byTypeOff, ...this.linkColorsOff};
    }
};

app.registerExtension(ext);
