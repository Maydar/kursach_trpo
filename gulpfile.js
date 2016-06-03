var gulp = require('gulp');
var babel = require('gulp-babel');
var debug = require('gulp-debug');

gulp.task("babel", function () {
   gulp.src("core/static/js/**/*.js")
       .pipe(babel())
       .pipe(gulp.dest("core/static/dist/js"));
});

gulp.task("copy", function () {
   gulp.src("core/static/js/**/*.html")
       .pipe(gulp.dest("core/static/dist/js"));
});

gulp.task("watch", function () {
    gulp.watch('core/static/js/**/*.js', ['babel']);
    
    gulp.watch('core/static/js/**/*.html', ['copy']);
});

gulp.task('default', ['watch', 'babel', 'copy']);


