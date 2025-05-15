import lowle

foo = lowle.imp('foo.py')

foo.hello()

print(lowle.this_module_directory())