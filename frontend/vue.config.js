module.exports = {
    css: {
        loaderOptions: {
            sass: {
                additionalData: `
                @import "@/assets/css/root.scss";
                @import "@/assets/css/_grid-settings.scss";
                @import "@/assets/css/_text-styles.scss";
                `
            }
        }
    }
}