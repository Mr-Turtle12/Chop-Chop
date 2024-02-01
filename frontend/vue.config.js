module.exports = {
    css: {
        loaderOptions: {
            sass: {
                additionalData: `
          @import "@/assets/css/_grid-settings.scss";
          @import "@/assets/css/_reset.scss";
          @import "@/assets/css/root.scss";
          @import "@/assets/css/_text-styles.scss";
          @import '@/../node_modules/include-media/dist/_include-media.scss';
        `
            },
        },
    },
}
