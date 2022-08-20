```sh
$ cat hello_world.py
def hello():
    # This is a comment line
    print("Hello, world!")


if __name__ == "__main__":
    hello()
```

```sh
$ docker build -t helloworld:pyconjp-2022 .
$ docker run -it -v $(pwd):/app helloworld:pyconjp-2022 python3 hello_world.py
Hello, world!

$ docker run -it -v $(pwd):/app helloworld:pyconjp-2022 python3 -m tokenize hello_world.py

0,0-0,0:            ENCODING       'utf-8'        
1,0-1,3:            NAME           'def'          
1,4-1,9:            NAME           'hello'        
1,9-1,10:           OP             '('            
1,10-1,11:          OP             ')'            
1,11-1,12:          OP             ':'            
1,12-1,13:          NEWLINE        '\n'           
2,4-2,28:           COMMENT        '# This is a comment line'
2,28-2,29:          NL             '\n'           
3,0-3,4:            INDENT         '    '         
3,4-3,9:            NAME           'print'        
3,9-3,10:           OP             '('            
3,10-3,25:          STRING         '"Hello, world!"'
3,25-3,26:          OP             ')'            
3,26-3,27:          NEWLINE        '\n'           
4,0-4,1:            NL             '\n'           
5,0-5,1:            NL             '\n'           
6,0-6,0:            DEDENT         ''             
6,0-6,2:            NAME           'if'           
6,3-6,11:           NAME           '__name__'     
6,12-6,14:          OP             '=='           
6,15-6,25:          STRING         '"__main__"'   
6,25-6,26:          OP             ':'            
6,26-6,27:          NEWLINE        '\n'           
7,0-7,4:            INDENT         '    '         
7,4-7,9:            NAME           'hello'        
7,9-7,10:           OP             '('            
7,10-7,11:          OP             ')'            
7,11-7,12:          NEWLINE        '\n'           
8,0-8,0:            DEDENT         ''             
8,0-8,0:            ENDMARKER      ''             

$ docker run -it -v $(pwd):/app helloworld:pyconjp-2022 python3 -m ast hello_world.py
Module(
   body=[
      FunctionDef(
         name='hello',
         args=arguments(
            posonlyargs=[],
            args=[],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
         body=[
            Expr(
               value=Call(
                  func=Name(id='print', ctx=Load()),
                  args=[
                     Constant(value='Hello, world!')],
                  keywords=[]))],
         decorator_list=[]),
      If(
         test=Compare(
            left=Name(id='__name__', ctx=Load()),
            ops=[
               Eq()],
            comparators=[
               Constant(value='__main__')]),
         body=[
            Expr(
               value=Call(
                  func=Name(id='hello', ctx=Load()),
                  args=[],
                  keywords=[]))],
         orelse=[])],
   type_ignores=[])

$ docker run -it -v $(pwd):/app helloworld:pyconjp-2022 python3 -m dis hello_world.py
  0           0 RESUME                   0

  1           2 LOAD_CONST               0 (<code object hello at 0xffffa37539f0, file "hello_world.py", line 1>)
              4 MAKE_FUNCTION            0
              6 STORE_NAME               0 (hello)

  6           8 LOAD_NAME                1 (__name__)
             10 LOAD_CONST               1 ('__main__')
             12 COMPARE_OP               2 (==)
             18 POP_JUMP_FORWARD_IF_FALSE    12 (to 44)

  7          20 PUSH_NULL
             22 LOAD_NAME                0 (hello)
             24 PRECALL                  0
             28 CALL                     0
             38 POP_TOP
             40 LOAD_CONST               2 (None)
             42 RETURN_VALUE

  6     >>   44 LOAD_CONST               2 (None)
             46 RETURN_VALUE

Disassembly of <code object hello at 0xffffa37539f0, file "hello_world.py", line 1>:
  1           0 RESUME                   0

  3           2 LOAD_GLOBAL              1 (NULL + print)
             14 LOAD_CONST               1 ('Hello, world!')
             16 PRECALL                  1
             20 CALL                     1
             30 POP_TOP
             32 LOAD_CONST               0 (None)
             34 RETURN_VALUE

$ docker run -it -v $(pwd):/app helloworld:pyconjp-2022 python3 -m compileall hello_world.py
Compiling 'hello_world.py'...

$ xxd __pycache__/hello_world.cpython-311.pyc
00000000: a70d 0d0a 0000 0000 5643 2d63 6e00 0000  ........VC-cn...
00000010: e300 0000 0000 0000 0000 0000 0002 0000  ................
00000020: 0000 0000 00f3 3000 0000 9700 6400 8400  ......0.....d...
00000030: 5a00 6501 6401 6b02 0000 0000 720c 0200  Z.e.d.k.....r...
00000040: 6500 a600 0000 ab00 0000 0000 0000 0000  e...............
00000050: 0100 6402 5300 6402 5300 2903 6300 0000  ..d.S.d.S.).c...
00000060: 0000 0000 0000 0000 0003 0000 0003 0000  ................
00000070: 00f3 2400 0000 9700 7401 0000 0000 0000  ..$.....t.......
00000080: 0000 0000 6401 a601 0000 ab01 0000 0000  ....d...........
00000090: 0000 0000 0100 6400 5300 2902 4e7a 0d48  ......d.S.).Nz.H
000000a0: 656c 6c6f 2c20 776f 726c 6421 2901 da05  ello, world!)...
000000b0: 7072 696e 74a9 00f3 0000 0000 fa0e 6865  print.........he
000000c0: 6c6c 6f5f 776f 726c 642e 7079 da05 6865  llo_world.py..he
000000d0: 6c6c 6f72 0700 0000 0100 0000 7316 0000  llor........s...
000000e0: 0080 00e5 0409 882f d104 1ad4 041a d004  ......./........
000000f0: 1ad0 041a d004 1a72 0500 0000 da08 5f5f  .......r......__
00000100: 6d61 696e 5f5f 4e29 0272 0700 0000 da08  main__N).r......
00000110: 5f5f 6e61 6d65 5f5f 7204 0000 0072 0500  __name__r....r..
00000120: 0000 7206 0000 00fa 083c 6d6f 6475 6c65  ..r......<module
00000130: 3e72 0a00 0000 0100 0000 733c 0000 00f0  >r........s<....
00000140: 0301 0101 f002 0201 1bf0 0002 011b f000  ................
00000150: 0201 1bf0 0a00 040c 887a d203 19f0 0001  .........z......
00000160: 010c d804 0980 4581 4784 4780 4780 4780  ......E.G.G.G.G.
00000170: 47f0 0301 010c f000 0101 0c72 0500 0000  G..........r....
```

```sh
$ docker run -it -v $(pwd):/app helloworld:pyconjp-2022 bash -c 'strace python3 hello_world.py 2>strace_log.txt'
Hello, world!

$ cat strace_log.txt
execve("/usr/local/bin/python3", ["python3", "hello_world.py"], 0xffffdad101a8 /* 14 vars */) = 0
brk(NULL)                               = 0xaaaaccdb1000
faccessat(AT_FDCWD, "/etc/ld.so.preload", R_OK) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=7294, ...}) = 0
mmap(NULL, 7294, PROT_READ, MAP_PRIVATE, 3, 0) = 0xffff9c0e9000
close(3)                                = 0
openat(AT_FDCWD, "/usr/local/lib/libpython3.11.so.1.0", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0\267\0\1\0\0\0\340\374\16\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=5596952, ...}) = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffff9c0e7000
mmap(NULL, 5932624, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xffff9bb14000
mprotect(0xffff9bf19000, 65536, PROT_NONE) = 0
mmap(0xffff9bf29000, 1380352, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x405000) = 0xffff9bf29000
mmap(0xffff9c07a000, 271952, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0xffff9c07a000
close(3)                                = 0
openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0\267\0\1\0\0\0`\17\2\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=1455120, ...}) = 0
mmap(NULL, 1527752, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xffff9b99f000
mprotect(0xffff9bafc000, 61440, PROT_NONE) = 0
mmap(0xffff9bb0b000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x15c000) = 0xffff9bb0b000
mmap(0xffff9bb11000, 12232, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0xffff9bb11000
close(3)                                = 0
openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libpthread.so.0", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0\267\0\1\0\0\0 a\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=160200, ...}) = 0
mmap(NULL, 197632, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xffff9b96e000
mprotect(0xffff9b98a000, 61440, PROT_NONE) = 0
mmap(0xffff9b999000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1b000) = 0xffff9b999000
mmap(0xffff9b99b000, 13312, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0xffff9b99b000
close(3)                                = 0
openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libdl.so.2", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0\267\0\1\0\0\0P\17\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=14560, ...}) = 0
mmap(NULL, 78080, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xffff9b95a000
mprotect(0xffff9b95d000, 61440, PROT_NONE) = 0
mmap(0xffff9b96c000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x2000) = 0xffff9b96c000
close(3)                                = 0
openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libutil.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0\267\0\1\0\0\0000\20\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=14672, ...}) = 0
mmap(NULL, 78112, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xffff9b946000
mprotect(0xffff9b948000, 65536, PROT_NONE) = 0
mmap(0xffff9b958000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x2000) = 0xffff9b958000
close(3)                                = 0
openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libm.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0\267\0\1\0\0\0000\273\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=633000, ...}) = 0
mmap(NULL, 696448, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xffff9b89b000
mprotect(0xffff9b934000, 65536, PROT_NONE) = 0
mmap(0xffff9b944000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x99000) = 0xffff9b944000
close(3)                                = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffff9c0e5000
mprotect(0xffff9bb0b000, 16384, PROT_READ) = 0
mprotect(0xffff9b944000, 4096, PROT_READ) = 0
mprotect(0xffff9b958000, 4096, PROT_READ) = 0
mprotect(0xffff9b96c000, 4096, PROT_READ) = 0
mprotect(0xffff9b999000, 4096, PROT_READ) = 0
mprotect(0xffff9bf29000, 188416, PROT_READ) = 0
mprotect(0xaaaabe270000, 4096, PROT_READ) = 0
mprotect(0xffff9c0ee000, 4096, PROT_READ) = 0
munmap(0xffff9c0e9000, 7294)            = 0
set_tid_address(0xffff9c0e5e00)         = 10
set_robust_list(0xffff9c0e5e10, 24)     = 0
rt_sigaction(SIGRTMIN, {sa_handler=0xffff9b973b94, sa_mask=[], sa_flags=SA_SIGINFO}, NULL, 8) = 0
rt_sigaction(SIGRT_1, {sa_handler=0xffff9b973c50, sa_mask=[], sa_flags=SA_RESTART|SA_SIGINFO}, NULL, 8) = 0
rt_sigprocmask(SIG_UNBLOCK, [RTMIN RT_1], NULL, 8) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
brk(NULL)                               = 0xaaaaccdb1000
brk(0xaaaaccdd2000)                     = 0xaaaaccdd2000
openat(AT_FDCWD, "/usr/lib/locale/locale-archive", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/share/locale/locale.alias", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/locale/C.UTF-8/LC_CTYPE", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=346132, ...}) = 0
mmap(NULL, 346132, PROT_READ, MAP_PRIVATE, 3, 0) = 0xffff9b846000
close(3)                                = 0
openat(AT_FDCWD, "/usr/lib/aarch64-linux-gnu/gconv/gconv-modules.cache", O_RDONLY) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=27004, ...}) = 0
mmap(NULL, 27004, PROT_READ, MAP_SHARED, 3, 0) = 0xffff9c0de000
close(3)                                = 0
futex(0xffff9bb10864, FUTEX_WAKE_PRIVATE, 2147483647) = 0
getcwd("/app", 4096)                    = 5
getrandom("\x69\xb9\x00\xbf\xf0\xbe\xd8\x9f\xde\x8c\xd8\xcc\x81\x2d\x69\x42\x6f\x33\xc3\x97\x26\x5f\x74\xb7", 24, GRND_NONBLOCK) = 24
gettid()                                = 10
mmap(NULL, 1048576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffff9b746000
mmap(NULL, 266240, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffff9b705000
mmap(NULL, 135168, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffff9b6e4000
mmap(NULL, 16384, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffff9b6e0000
brk(0xaaaaccdf3000)                     = 0xaaaaccdf3000
newfstatat(AT_FDCWD, "/usr/local/bin/python3", {st_mode=S_IFREG|0755, st_size=6168, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/pyvenv.cfg", O_RDONLY) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/local/bin/pyvenv.cfg", O_RDONLY) = -1 ENOENT (No such file or directory)
readlinkat(AT_FDCWD, "/usr/local/bin/python3", "python3.11", 4096) = 10
readlinkat(AT_FDCWD, "/usr/local/bin/python3.11", 0xffffc8839be0, 4096) = -1 EINVAL (Invalid argument)
openat(AT_FDCWD, "/usr/local/bin/python3._pth", O_RDONLY) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/local/bin/python3.11._pth", O_RDONLY) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/local/bin/pybuilddir.txt", O_RDONLY) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/bin/Modules/Setup.local", 0xffffc883ebb0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/bin/lib/python311.zip", 0xffffc883e930, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python311.zip", 0xffffc883e930, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/lib/python311.zip", 0xffffc883e930, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/bin/lib/python3.11/os.py", 0xffffc883e780, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/bin/lib/python3.11/os.pyc", 0xffffc883e780, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/os.py", {st_mode=S_IFREG|0644, st_size=39461, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/bin/lib/python3.11/lib-dynload", 0xffffc883e930, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/lib-dynload", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
sysinfo({uptime=939, loads=[1792, 1152, 0], totalram=16763854848, freeram=15561834496, sharedram=343891968, bufferram=37244928, totalswap=1073737728, freeswap=1073737728, procs=474, totalhigh=0, freehigh=0, mem_unit=1}) = 0
openat(AT_FDCWD, "/etc/localtime", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=118, ...}) = 0
fstat(3, {st_mode=S_IFREG|0644, st_size=118, ...}) = 0
read(3, "TZif2\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\1\0\0\0\0"..., 4096) = 118
lseek(3, -62, SEEK_CUR)                 = 56
read(3, "TZif2\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\1\0\0\0\0"..., 4096) = 62
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python311.zip", 0xffffc883e350, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python311.zip", 0xffffc883e620, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
fstat(3, {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
getdents64(3, 0xaaaaccde6010 /* 207 entries */, 32768) = 6880
getdents64(3, 0xaaaaccde6010 /* 0 entries */, 32768) = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__init__.cpython-311-aarch64-linux-gnu.so", 0xffffc883e620, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__init__.abi3.so", 0xffffc883e680, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__init__.so", 0xffffc883e680, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__init__.py", {st_mode=S_IFREG|0644, st_size=5884, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__init__.py", {st_mode=S_IFREG|0644, st_size=5884, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/__init__.cpython-311.pyc", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__init__.py", O_RDONLY|O_CLOEXEC) = 3
fcntl(3, F_GETFD)                       = 0x1 (flags FD_CLOEXEC)
fstat(3, {st_mode=S_IFREG|0644, st_size=5884, ...}) = 0
ioctl(3, TCGETS, 0xffffc883e220)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
fstat(3, {st_mode=S_IFREG|0644, st_size=5884, ...}) = 0
read(3, "\"\"\" Standard \"encodings\" Package"..., 5885) = 5884
read(3, "", 1)                          = 0
close(3)                                = 0
brk(0xaaaacce25000)                     = 0xaaaacce25000
brk(0xaaaacce46000)                     = 0xaaaacce46000
mmap(NULL, 1048576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffff9b5e0000
brk(0xaaaacce68000)                     = 0xaaaacce68000
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__init__.py", {st_mode=S_IFREG|0644, st_size=5884, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/__init__.cpython-311.pyc.281473290457776", O_WRONLY|O_CREAT|O_EXCL|O_CLOEXEC, 0644) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=0, ...}) = 0
write(3, "\247\r\r\n\0\0\0\0\333\354\37c\374\26\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\6\0\0"..., 6571) = 6571
close(3)                                = 0
renameat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/__init__.cpython-311.pyc.281473290457776", AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/__init__.cpython-311.pyc") = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/encodings", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
fstat(3, {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
getdents64(3, 0xaaaacce4d870 /* 125 entries */, 32768) = 4224
getdents64(3, 0xaaaacce4d870 /* 0 entries */, 32768) = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/aliases.py", {st_mode=S_IFREG|0644, st_size=15677, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/aliases.py", {st_mode=S_IFREG|0644, st_size=15677, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/aliases.cpython-311.pyc", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/aliases.py", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=15677, ...}) = 0
ioctl(3, TCGETS, 0xffffc883d630)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
fstat(3, {st_mode=S_IFREG|0644, st_size=15677, ...}) = 0
read(3, "\"\"\" Encoding Aliases Support\n\n  "..., 15678) = 15677
read(3, "", 1)                          = 0
close(3)                                = 0
brk(0xaaaacce89000)                     = 0xaaaacce89000
brk(0xaaaacceab000)                     = 0xaaaacceab000
brk(0xaaaacced4000)                     = 0xaaaacced4000
brk(0xaaaaccecf000)                     = 0xaaaaccecf000
brk(0xaaaaccec5000)                     = 0xaaaaccec5000
brk(0xaaaacceb3000)                     = 0xaaaacceb3000
brk(0xaaaaccea0000)                     = 0xaaaaccea0000
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/aliases.py", {st_mode=S_IFREG|0644, st_size=15677, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/aliases.cpython-311.pyc.281473290776752", O_WRONLY|O_CREAT|O_EXCL|O_CLOEXEC, 0644) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=0, ...}) = 0
write(3, "\247\r\r\n\0\0\0\0\333\354\37c==\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\5\0\0"..., 12653) = 12653
close(3)                                = 0
renameat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/aliases.cpython-311.pyc.281473290776752", AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/aliases.cpython-311.pyc") = 0
brk(0xaaaacce83000)                     = 0xaaaacce83000
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/utf_8.py", {st_mode=S_IFREG|0644, st_size=1005, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/utf_8.py", {st_mode=S_IFREG|0644, st_size=1005, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/utf_8.cpython-311.pyc", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/utf_8.py", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=1005, ...}) = 0
ioctl(3, TCGETS, 0xffffc883e280)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
fstat(3, {st_mode=S_IFREG|0644, st_size=1005, ...}) = 0
read(3, "\"\"\" Python 'utf-8' Codec\n\n\nWritt"..., 1006) = 1005
read(3, "", 1)                          = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/utf_8.py", {st_mode=S_IFREG|0644, st_size=1005, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/utf_8.cpython-311.pyc.281473290457136", O_WRONLY|O_CREAT|O_EXCL|O_CLOEXEC, 0644) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=0, ...}) = 0
write(3, "\247\r\r\n\0\0\0\0\333\354\37c\355\3\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\5\0\0"..., 2322) = 2322
close(3)                                = 0
renameat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/utf_8.cpython-311.pyc.281473290457136", AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/utf_8.cpython-311.pyc") = 0
rt_sigaction(SIGPIPE, {sa_handler=SIG_IGN, sa_mask=[], sa_flags=SA_ONSTACK}, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGXFSZ, {sa_handler=SIG_IGN, sa_mask=[], sa_flags=SA_ONSTACK}, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGHUP, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGINT, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGQUIT, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGILL, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGTRAP, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGABRT, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGBUS, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGFPE, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGKILL, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGUSR1, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGSEGV, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGUSR2, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGPIPE, NULL, {sa_handler=SIG_IGN, sa_mask=[], sa_flags=SA_ONSTACK}, 8) = 0
rt_sigaction(SIGALRM, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGTERM, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGSTKFLT, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGCHLD, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGCONT, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGSTOP, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGTSTP, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGTTIN, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGTTOU, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGURG, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGXCPU, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGXFSZ, NULL, {sa_handler=SIG_IGN, sa_mask=[], sa_flags=SA_ONSTACK}, 8) = 0
rt_sigaction(SIGVTALRM, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGPROF, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGWINCH, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGIO, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGPWR, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGSYS, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_2, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_3, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_4, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_5, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_6, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_7, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_8, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_9, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_10, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_11, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_12, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_13, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_14, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_15, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_16, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_17, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_18, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_19, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_20, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_21, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_22, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_23, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_24, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_25, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_26, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_27, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_28, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_29, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_30, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_31, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_32, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGINT, {sa_handler=0xffff9bc0f0ec, sa_mask=[], sa_flags=SA_ONSTACK}, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
fstat(0, {st_mode=S_IFCHR|0620, st_rdev=makedev(0x88, 0), ...}) = 0
fcntl(0, F_GETFD)                       = 0
fstat(0, {st_mode=S_IFCHR|0620, st_rdev=makedev(0x88, 0), ...}) = 0
ioctl(0, TCGETS, {B38400 opost isig icanon echo ...}) = 0
lseek(0, 0, SEEK_CUR)                   = -1 ESPIPE (Illegal seek)
ioctl(0, TCGETS, {B38400 opost isig icanon echo ...}) = 0
fcntl(1, F_GETFD)                       = 0
fstat(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(0x88, 0), ...}) = 0
ioctl(1, TCGETS, {B38400 opost isig icanon echo ...}) = 0
lseek(1, 0, SEEK_CUR)                   = -1 ESPIPE (Illegal seek)
ioctl(1, TCGETS, {B38400 opost isig icanon echo ...}) = 0
fcntl(2, F_GETFD)                       = 0
fstat(2, {st_mode=S_IFREG|0644, st_size=23193, ...}) = 0
ioctl(2, TCGETS, 0xffffc883ea30)        = -1 ENOSYS (Function not implemented)
lseek(2, 0, SEEK_CUR)                   = 23340
ioctl(2, TCGETS, 0xffffc883edb0)        = -1 ENOSYS (Function not implemented)
lseek(2, 0, SEEK_CUR)                   = 23467
newfstatat(AT_FDCWD, "/usr/local/bin/pyvenv.cfg", 0xffffc883e3f0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/pyvenv.cfg", 0xffffc883e3f0, 0) = -1 ENOENT (No such file or directory)
geteuid()                               = 0
getuid()                                = 0
getegid()                               = 0
getgid()                                = 0
newfstatat(AT_FDCWD, "/root/.local/lib/python3.11/site-packages", 0xffffc883e3f0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
fstat(3, {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
getdents64(3, 0xaaaacce4d870 /* 12 entries */, 32768) = 432
getdents64(3, 0xaaaacce4d870 /* 0 entries */, 32768) = 0
close(3)                                = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/distutils-precedence.pth", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=151, ...}) = 0
ioctl(3, TCGETS, 0xffffc883dff0)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
read(3, "import os; var = 'SETUPTOOLS_USE"..., 8192) = 151
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/lib-dynload", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/lib-dynload", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/lib-dynload", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/lib-dynload", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 4
fstat(4, {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
getdents64(4, 0xaaaacce57f40 /* 78 entries */, 32768) = 5000
getdents64(4, 0xaaaacce57f40 /* 0 entries */, 32768) = 0
close(4)                                = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 4
fstat(4, {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
getdents64(4, 0xaaaacce57f40 /* 12 entries */, 32768) = 432
getdents64(4, 0xaaaacce57f40 /* 0 entries */, 32768) = 0
close(4)                                = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__init__.cpython-311-aarch64-linux-gnu.so", 0xffffc883db80, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__init__.abi3.so", 0xffffc883db80, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__init__.so", 0xffffc883db80, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__init__.py", {st_mode=S_IFREG|0644, st_size=6128, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__init__.py", {st_mode=S_IFREG|0644, st_size=6128, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__pycache__/__init__.cpython-311.pyc", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__init__.py", O_RDONLY|O_CLOEXEC) = 4
fstat(4, {st_mode=S_IFREG|0644, st_size=6128, ...}) = 0
ioctl(4, TCGETS, 0xffffc883d780)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(4, 0, SEEK_CUR)                   = 0
lseek(4, 0, SEEK_CUR)                   = 0
fstat(4, {st_mode=S_IFREG|0644, st_size=6128, ...}) = 0
read(4, "# don't import any costly module"..., 6129) = 6128
read(4, "", 1)                          = 0
close(4)                                = 0
brk(0xaaaaccea4000)                     = 0xaaaaccea4000
brk(0xaaaacce9d000)                     = 0xaaaacce9d000
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__init__.py", {st_mode=S_IFREG|0644, st_size=6128, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__pycache__", 0xffffc883db80, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
mkdirat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__pycache__", 0777) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__pycache__/__init__.cpython-311.pyc.281473290225680", O_WRONLY|O_CREAT|O_EXCL|O_CLOEXEC, 0644) = 4
fstat(4, {st_mode=S_IFREG|0644, st_size=0, ...}) = 0
write(4, "\247\r\r\n\0\0\0\0\373\354\37c\360\27\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\6\0\0"..., 11164) = 11164
close(4)                                = 0
renameat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__pycache__/__init__.cpython-311.pyc.281473290225680", AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__pycache__/__init__.cpython-311.pyc") = 0
read(3, "", 8192)                       = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/lib-dynload", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/lib-dynload", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/app/hello_world.py", {st_mode=S_IFREG|0644, st_size=110, ...}, 0) = 0
openat(AT_FDCWD, "/app/hello_world.py", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=110, ...}) = 0
ioctl(3, TCGETS, 0xffffc883ea30)        = -1 ENOSYS (Function not implemented)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, -22, SEEK_END)                 = 88
lseek(3, 0, SEEK_CUR)                   = 88
read(3, "_main__\":\n    hello()\n", 4096) = 22
lseek(3, 0, SEEK_END)                   = 110
lseek(3, 0, SEEK_CUR)                   = 110
lseek(3, 0, SEEK_SET)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
fstat(3, {st_mode=S_IFREG|0644, st_size=110, ...}) = 0
read(3, "def hello():\n    # This is a com"..., 111) = 110
read(3, "", 1)                          = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/app/hello_world.py", {st_mode=S_IFREG|0644, st_size=110, ...}, 0) = 0
readlinkat(AT_FDCWD, "hello_world.py", 0xffffc882e2e0, 4096) = -1 EINVAL (Invalid argument)
getcwd("/app", 4096)                    = 5
newfstatat(AT_FDCWD, "/app/hello_world.py", {st_mode=S_IFREG|0644, st_size=110, ...}, AT_SYMLINK_NOFOLLOW) = 0
openat(AT_FDCWD, "/app/hello_world.py", O_RDONLY) = 3
ioctl(3, FIOCLEX)                       = 0
fstat(3, {st_mode=S_IFREG|0644, st_size=110, ...}) = 0
ioctl(3, TCGETS, 0xffffc883f230)        = -1 ENOSYS (Function not implemented)
lseek(3, 0, SEEK_CUR)                   = 0
fstat(3, {st_mode=S_IFREG|0644, st_size=110, ...}) = 0
read(3, "def hello():\n    # This is a com"..., 4096) = 110
lseek(3, 0, SEEK_SET)                   = 0
read(3, "def hello():\n    # This is a com"..., 4096) = 110
read(3, "", 4096)                       = 0
close(3)                                = 0
write(1, "Hello, world!\n", 14)         = 14
rt_sigaction(SIGINT, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=SA_ONSTACK}, {sa_handler=0xffff9bc0f0ec, sa_mask=[], sa_flags=SA_ONSTACK}, 8) = 0
munmap(0xffff9b746000, 1048576)         = 0
munmap(0xffff9b6e0000, 16384)           = 0
exit_group(0)                           = ?
+++ exited with 0 +++
```
