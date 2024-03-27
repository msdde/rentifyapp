/** @type {import('tailwindcss').Config} */
module.exports = {
    purge: [
        './templates/**/*.html',
    ],
    content: [
      'node_modules/preline/dist/*.js',
    ],
    theme: {
        extend: {
            gridTemplateColumns: {
                '3': 'repeat(3, minmax(0, 1fr))',
            }
        },
    },
    plugins: [
        require('preline/plugin'),
    ],
}
