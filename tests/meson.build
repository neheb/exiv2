if not expat_dep.found()
  subdir_done()
endif

test(
  'bugfixTests',
  find_program('runner.py'),
  env: bindir,
  args: '--verbose bugfixes',
  timeout: 600,
  is_parallel: false,
  workdir: meson.current_source_dir(),
)

test(
  'lensTests',
  find_program('runner.py'),
  env: bindir,
  args: '--verbose lens_tests',
  timeout: 600,
  is_parallel: false,
  workdir: meson.current_source_dir(),
)

test(
  'tiffTests',
  find_program('runner.py'),
  env: bindir,
  args: '--verbose tiff_test',
  timeout: 600,
  is_parallel: false,
  workdir: meson.current_source_dir(),
)
