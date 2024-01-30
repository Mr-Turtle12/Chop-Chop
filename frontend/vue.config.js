const path = require('path')

module.exports = {
    css: {
        loaderOptions: {
            sass: {
                additionalData: `
          @import "@/assets/css/_grid-settings.scss";
          @import "@/assets/css/_reset.scss";
          @import "@/assets/css/root.scss";
          @import "@/assets/css/_text-styles.scss";
          @import 'include-media';
        `,
            },
        },
    },
    configureWebpack: {
        resolve: {
            fallback: {
                fs: false,
                path: require.resolve('path-browserify'),
            },
        },
    },
    pluginOptions: {
        electronBuilder: {
            nodeIntegration: true, // Make sure to set nodeIntegration to true
            builderOptions: {
                // Add this section to handle __dirname issue
                extraResources: {
                    from: './resources',
                    to: 'resources',
                },
            },
        },
    },
}
