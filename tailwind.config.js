const { default: daisyui } = require('daisyui');

// tailwind.config.js
module.exports = {
  content: [
      './templates/**/*.html',  // Ruta para las plantillas de Django
      './gestion_remustar/templates/**/*.html', // Otras rutas de plantillas en aplicaciones
  ],
  theme: {
      extend: {},
  },
  plugins: [
      require('daisyui'), // Activa DaisyUI
  ],
  daisyui: {
    themes: ['coffee']
  }
}