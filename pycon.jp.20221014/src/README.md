```sh
$ cat hello_world.py
def hello():
    # This is a comment line
    print("Hello, world")


if __name__ == "__main__":
    hello()
```

```sh
$ docker build -t helloworld:pyconjp-2022 .

$ docker run -it -v $(pwd):/app helloworld:pyconjp-2022 python3 hello_world.py
Hello, world

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
3,10-3,24:          STRING         '"Hello, world"'
3,24-3,25:          OP             ')'            
3,25-3,26:          NEWLINE        '\n'           
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
                     Constant(value='Hello, world')],
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

  1           2 LOAD_CONST               0 (<code object hello at 0xffffa122f9f0, file "hello_world.py", line 1>)
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

Disassembly of <code object hello at 0xffffa122f9f0, file "hello_world.py", line 1>:
  1           0 RESUME                   0

  3           2 LOAD_GLOBAL              1 (NULL + print)
             14 LOAD_CONST               1 ('Hello, world')
             16 PRECALL                  1
             20 CALL                     1
             30 POP_TOP
             32 LOAD_CONST               0 (None)
             34 RETURN_VALUE

$ docker run -it -v $(pwd):/app helloworld:pyconjp-2022 python3 -m compileall hello_world.py
Compiling 'hello_world.py'...

$ xxd __pycache__/hello_world.cpython-311.pyc
00000000: a70d 0d0a 0000 0000 fa1f 3e63 6d00 0000  ..........>cm...
00000010: e300 0000 0000 0000 0000 0000 0002 0000  ................
00000020: 0000 0000 00f3 3000 0000 9700 6400 8400  ......0.....d...
00000030: 5a00 6501 6401 6b02 0000 0000 720c 0200  Z.e.d.k.....r...
00000040: 6500 a600 0000 ab00 0000 0000 0000 0000  e...............
00000050: 0100 6402 5300 6402 5300 2903 6300 0000  ..d.S.d.S.).c...
00000060: 0000 0000 0000 0000 0003 0000 0003 0000  ................
00000070: 00f3 2400 0000 9700 7401 0000 0000 0000  ..$.....t.......
00000080: 0000 0000 6401 a601 0000 ab01 0000 0000  ....d...........
00000090: 0000 0000 0100 6400 5300 2902 4e7a 0c48  ......d.S.).Nz.H
000000a0: 656c 6c6f 2c20 776f 726c 6429 01da 0570  ello, world)...p
000000b0: 7269 6e74 a900 f300 0000 00fa 0e68 656c  rint.........hel
000000c0: 6c6f 5f77 6f72 6c64 2e70 79da 0568 656c  lo_world.py..hel
000000d0: 6c6f 7207 0000 0001 0000 0073 1600 0000  lor........s....
000000e0: 8000 e504 0988 2ed1 0419 d404 19d0 0419  ................
000000f0: d004 19d0 0419 7205 0000 00da 085f 5f6d  ......r......__m
00000100: 6169 6e5f 5f4e 2902 7207 0000 00da 085f  ain__N).r......_
00000110: 5f6e 616d 655f 5f72 0400 0000 7205 0000  _name__r....r...
00000120: 0072 0600 0000 fa08 3c6d 6f64 756c 653e  .r......<module>
00000130: 720a 0000 0001 0000 0073 3c00 0000 f003  r........s<.....
00000140: 0101 01f0 0202 011a f000 0201 1af0 0002  ................
00000150: 011a f00a 0004 0c88 7ad2 0319 f000 0101  ........z.......
00000160: 0cd8 0409 8045 8147 8447 8047 8047 8047  .....E.G.G.G.G.G
00000170: f003 0101 0cf0 0001 010c 7205 0000 00    ..........r....
```

```sh
$ docker run -it -v $(pwd):/app helloworld:pyconjp-2022 bash -c 'strace python3 hello_world.py 2>strace_log.txt'
Hello, world

$ cat strace_log.txt
execve("/usr/local/bin/python3", ["python3", "hello_world.py"], 0xffffca9e3188 /* 14 vars */) = 0
--- SIGWINCH {si_signo=SIGWINCH, si_code=SI_KERNEL} ---
brk(NULL)                               = 0xaaab0b4ee000
faccessat(AT_FDCWD, "/etc/ld.so.preload", R_OK) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=11071, ...}) = 0
mmap(NULL, 11071, PROT_READ, MAP_PRIVATE, 3, 0) = 0xffffb04ae000
close(3)                                = 0
openat(AT_FDCWD, "/usr/local/lib/libpython3.11.so.1.0", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0\267\0\1\0\0\0\340\374\16\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=5596952, ...}) = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffffb04ac000
mmap(NULL, 5932624, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xffffafeda000
mprotect(0xffffb02df000, 65536, PROT_NONE) = 0
mmap(0xffffb02ef000, 1380352, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x405000) = 0xffffb02ef000
mmap(0xffffb0440000, 271952, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0xffffb0440000
close(3)                                = 0
openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0\267\0\1\0\0\0`\17\2\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=1455120, ...}) = 0
mmap(NULL, 1527752, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xffffafd65000
mprotect(0xffffafec2000, 61440, PROT_NONE) = 0
mmap(0xffffafed1000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x15c000) = 0xffffafed1000
mmap(0xffffafed7000, 12232, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0xffffafed7000
close(3)                                = 0
openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libpthread.so.0", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0\267\0\1\0\0\0 a\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=160200, ...}) = 0
mmap(NULL, 197632, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xffffafd34000
mprotect(0xffffafd50000, 61440, PROT_NONE) = 0
mmap(0xffffafd5f000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1b000) = 0xffffafd5f000
mmap(0xffffafd61000, 13312, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0xffffafd61000
close(3)                                = 0
openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libdl.so.2", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0\267\0\1\0\0\0P\17\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=14560, ...}) = 0
mmap(NULL, 78080, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xffffafd20000
mprotect(0xffffafd23000, 61440, PROT_NONE) = 0
mmap(0xffffafd32000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x2000) = 0xffffafd32000
close(3)                                = 0
openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libutil.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0\267\0\1\0\0\0000\20\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=14672, ...}) = 0
mmap(NULL, 78112, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xffffafd0c000
mprotect(0xffffafd0e000, 65536, PROT_NONE) = 0
mmap(0xffffafd1e000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x2000) = 0xffffafd1e000
close(3)                                = 0
openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libm.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0\267\0\1\0\0\0000\273\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=633000, ...}) = 0
mmap(NULL, 696448, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xffffafc61000
mprotect(0xffffafcfa000, 65536, PROT_NONE) = 0
mmap(0xffffafd0a000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x99000) = 0xffffafd0a000
close(3)                                = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffffb04aa000
mprotect(0xffffafed1000, 16384, PROT_READ) = 0
mprotect(0xffffafd0a000, 4096, PROT_READ) = 0
mprotect(0xffffafd1e000, 4096, PROT_READ) = 0
mprotect(0xffffafd32000, 4096, PROT_READ) = 0
mprotect(0xffffafd5f000, 4096, PROT_READ) = 0
mprotect(0xffffb02ef000, 188416, PROT_READ) = 0
mprotect(0xaaaad69f0000, 4096, PROT_READ) = 0
mprotect(0xffffb04b4000, 4096, PROT_READ) = 0
munmap(0xffffb04ae000, 11071)           = 0
set_tid_address(0xffffb04aae00)         = 10
set_robust_list(0xffffb04aae10, 24)     = 0
rt_sigaction(SIGRTMIN, {sa_handler=0xffffafd39b94, sa_mask=[], sa_flags=SA_SIGINFO}, NULL, 8) = 0
rt_sigaction(SIGRT_1, {sa_handler=0xffffafd39c50, sa_mask=[], sa_flags=SA_RESTART|SA_SIGINFO}, NULL, 8) = 0
rt_sigprocmask(SIG_UNBLOCK, [RTMIN RT_1], NULL, 8) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
brk(NULL)                               = 0xaaab0b4ee000
brk(0xaaab0b50f000)                     = 0xaaab0b50f000
openat(AT_FDCWD, "/usr/lib/locale/locale-archive", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/share/locale/locale.alias", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/locale/C.UTF-8/LC_CTYPE", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=346132, ...}) = 0
mmap(NULL, 346132, PROT_READ, MAP_PRIVATE, 3, 0) = 0xffffafc0c000
close(3)                                = 0
openat(AT_FDCWD, "/usr/lib/aarch64-linux-gnu/gconv/gconv-modules.cache", O_RDONLY) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=27004, ...}) = 0
mmap(NULL, 27004, PROT_READ, MAP_SHARED, 3, 0) = 0xffffafc05000
close(3)                                = 0
futex(0xffffafed6864, FUTEX_WAKE_PRIVATE, 2147483647) = 0
getcwd("/app", 4096)                    = 5
getrandom("\xab\xf5\x60\x50\x0a\x54\xb4\x53\x2e\x1a\x91\x07\x64\x86\x96\xfa\x98\x7c\xfc\x21\x7e\xfe\x7a\xa4", 24, GRND_NONBLOCK) = 24
gettid()                                = 10
mmap(NULL, 1048576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffffafb05000
mmap(NULL, 266240, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffffafac4000
mmap(NULL, 135168, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffffafaa3000
mmap(NULL, 16384, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffffb04a6000
brk(0xaaab0b530000)                     = 0xaaab0b530000
newfstatat(AT_FDCWD, "/usr/local/bin/python3", {st_mode=S_IFREG|0755, st_size=6168, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/pyvenv.cfg", O_RDONLY) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/local/bin/pyvenv.cfg", O_RDONLY) = -1 ENOENT (No such file or directory)
readlinkat(AT_FDCWD, "/usr/local/bin/python3", "python3.11", 4096) = 10
readlinkat(AT_FDCWD, "/usr/local/bin/python3.11", 0xfffff60bde10, 4096) = -1 EINVAL (Invalid argument)
openat(AT_FDCWD, "/usr/local/bin/python3._pth", O_RDONLY) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/local/bin/python3.11._pth", O_RDONLY) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/local/bin/pybuilddir.txt", O_RDONLY) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/bin/Modules/Setup.local", 0xfffff60c2de0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/bin/lib/python311.zip", 0xfffff60c2b60, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python311.zip", 0xfffff60c2b60, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/lib/python311.zip", 0xfffff60c2b60, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/bin/lib/python3.11/os.py", 0xfffff60c29b0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/bin/lib/python3.11/os.pyc", 0xfffff60c29b0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/os.py", {st_mode=S_IFREG|0644, st_size=39461, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/bin/lib/python3.11/lib-dynload", 0xfffff60c2b60, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/lib-dynload", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
sysinfo({uptime=150871, loads=[896, 1536, 0], totalram=16763854848, freeram=13988184064, sharedram=343830528, bufferram=169230336, totalswap=1073737728, freeswap=1073737728, procs=490, totalhigh=0, freehigh=0, mem_unit=1}) = 0
openat(AT_FDCWD, "/etc/localtime", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=118, ...}) = 0
fstat(3, {st_mode=S_IFREG|0644, st_size=118, ...}) = 0
read(3, "TZif2\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\1\0\0\0\0"..., 4096) = 118
lseek(3, -62, SEEK_CUR)                 = 56
read(3, "TZif2\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1\0\0\0\1\0\0\0\0"..., 4096) = 62
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python311.zip", 0xfffff60c2580, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python311.zip", 0xfffff60c2850, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
fstat(3, {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
getdents64(3, 0xaaab0b523010 /* 207 entries */, 32768) = 6880
getdents64(3, 0xaaab0b523010 /* 0 entries */, 32768) = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__init__.cpython-311-aarch64-linux-gnu.so", 0xfffff60c2850, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__init__.abi3.so", 0xfffff60c28b0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__init__.so", 0xfffff60c28b0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__init__.py", {st_mode=S_IFREG|0644, st_size=5884, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__init__.py", {st_mode=S_IFREG|0644, st_size=5884, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/__init__.cpython-311.pyc", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__init__.py", O_RDONLY|O_CLOEXEC) = 3
fcntl(3, F_GETFD)                       = 0x1 (flags FD_CLOEXEC)
fstat(3, {st_mode=S_IFREG|0644, st_size=5884, ...}) = 0
ioctl(3, TCGETS, 0xfffff60c2450)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
fstat(3, {st_mode=S_IFREG|0644, st_size=5884, ...}) = 0
read(3, "\"\"\" Standard \"encodings\" Package"..., 5885) = 5884
read(3, "", 1)                          = 0
close(3)                                = 0
brk(0xaaab0b562000)                     = 0xaaab0b562000
brk(0xaaab0b583000)                     = 0xaaab0b583000
mmap(NULL, 1048576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffffaf9a3000
brk(0xaaab0b5a5000)                     = 0xaaab0b5a5000
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__init__.py", {st_mode=S_IFREG|0644, st_size=5884, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/__init__.cpython-311.pyc.281473629934256", O_WRONLY|O_CREAT|O_EXCL|O_CLOEXEC, 0644) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=0, ...}) = 0
write(3, "\247\r\r\n\0\0\0\0\347U=c\374\26\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\6\0\0"..., 6571) = 6571
close(3)                                = 0
renameat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/__init__.cpython-311.pyc.281473629934256", AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/__init__.cpython-311.pyc") = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/encodings", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
fstat(3, {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
getdents64(3, 0xaaab0b58a870 /* 125 entries */, 32768) = 4224
getdents64(3, 0xaaab0b58a870 /* 0 entries */, 32768) = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/aliases.py", {st_mode=S_IFREG|0644, st_size=15677, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/aliases.py", {st_mode=S_IFREG|0644, st_size=15677, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/aliases.cpython-311.pyc", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/aliases.py", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=15677, ...}) = 0
ioctl(3, TCGETS, 0xfffff60c1860)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
fstat(3, {st_mode=S_IFREG|0644, st_size=15677, ...}) = 0
read(3, "\"\"\" Encoding Aliases Support\n\n  "..., 15678) = 15677
read(3, "", 1)                          = 0
close(3)                                = 0
brk(0xaaab0b5c6000)                     = 0xaaab0b5c6000
brk(0xaaab0b5e8000)                     = 0xaaab0b5e8000
brk(0xaaab0b611000)                     = 0xaaab0b611000
brk(0xaaab0b60c000)                     = 0xaaab0b60c000
brk(0xaaab0b602000)                     = 0xaaab0b602000
brk(0xaaab0b5f0000)                     = 0xaaab0b5f0000
brk(0xaaab0b5dd000)                     = 0xaaab0b5dd000
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/aliases.py", {st_mode=S_IFREG|0644, st_size=15677, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/aliases.cpython-311.pyc.281473630253232", O_WRONLY|O_CREAT|O_EXCL|O_CLOEXEC, 0644) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=0, ...}) = 0
write(3, "\247\r\r\n\0\0\0\0\347U=c==\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\5\0\0"..., 12653) = 12653
close(3)                                = 0
renameat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/aliases.cpython-311.pyc.281473630253232", AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/aliases.cpython-311.pyc") = 0
brk(0xaaab0b5c0000)                     = 0xaaab0b5c0000
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/utf_8.py", {st_mode=S_IFREG|0644, st_size=1005, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/utf_8.py", {st_mode=S_IFREG|0644, st_size=1005, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/utf_8.cpython-311.pyc", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/utf_8.py", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=1005, ...}) = 0
ioctl(3, TCGETS, 0xfffff60c24b0)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
fstat(3, {st_mode=S_IFREG|0644, st_size=1005, ...}) = 0
read(3, "\"\"\" Python 'utf-8' Codec\n\n\nWritt"..., 1006) = 1005
read(3, "", 1)                          = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/utf_8.py", {st_mode=S_IFREG|0644, st_size=1005, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/utf_8.cpython-311.pyc.281473629933616", O_WRONLY|O_CREAT|O_EXCL|O_CLOEXEC, 0644) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=0, ...}) = 0
write(3, "\247\r\r\n\0\0\0\0\347U=c\355\3\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\5\0\0"..., 2322) = 2322
close(3)                                = 0
renameat(AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/utf_8.cpython-311.pyc.281473629933616", AT_FDCWD, "/usr/local/lib/python3.11/encodings/__pycache__/utf_8.cpython-311.pyc") = 0
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
rt_sigaction(SIGINT, {sa_handler=0xffffaffd50ec, sa_mask=[], sa_flags=SA_ONSTACK}, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
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
fstat(2, {st_mode=S_IFREG|0644, st_size=23239, ...}) = 0
ioctl(2, TCGETS, 0xfffff60c2c60)        = -1 ENOSYS (Function not implemented)
lseek(2, 0, SEEK_CUR)                   = 23386
ioctl(2, TCGETS, 0xfffff60c2fe0)        = -1 ENOSYS (Function not implemented)
lseek(2, 0, SEEK_CUR)                   = 23513
newfstatat(AT_FDCWD, "/usr/local/bin/pyvenv.cfg", 0xfffff60c2620, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/pyvenv.cfg", 0xfffff60c2620, 0) = -1 ENOENT (No such file or directory)
geteuid()                               = 0
getuid()                                = 0
getegid()                               = 0
getgid()                                = 0
newfstatat(AT_FDCWD, "/root/.local/lib/python3.11/site-packages", 0xfffff60c2620, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
fstat(3, {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
getdents64(3, 0xaaab0b58a870 /* 12 entries */, 32768) = 432
getdents64(3, 0xaaab0b58a870 /* 0 entries */, 32768) = 0
close(3)                                = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/distutils-precedence.pth", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=151, ...}) = 0
ioctl(3, TCGETS, 0xfffff60c2220)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
read(3, "import os; var = 'SETUPTOOLS_USE"..., 8192) = 151
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/lib-dynload", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/lib-dynload", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/lib-dynload", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/lib-dynload", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 4
fstat(4, {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
getdents64(4, 0xaaab0b594f40 /* 78 entries */, 32768) = 5000
getdents64(4, 0xaaab0b594f40 /* 0 entries */, 32768) = 0
close(4)                                = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 4
fstat(4, {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
getdents64(4, 0xaaab0b594f40 /* 12 entries */, 32768) = 432
getdents64(4, 0xaaab0b594f40 /* 0 entries */, 32768) = 0
close(4)                                = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__init__.cpython-311-aarch64-linux-gnu.so", 0xfffff60c1db0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__init__.abi3.so", 0xfffff60c1db0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__init__.so", 0xfffff60c1db0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__init__.py", {st_mode=S_IFREG|0644, st_size=6128, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__init__.py", {st_mode=S_IFREG|0644, st_size=6128, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__pycache__/__init__.cpython-311.pyc", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__init__.py", O_RDONLY|O_CLOEXEC) = 4
fstat(4, {st_mode=S_IFREG|0644, st_size=6128, ...}) = 0
ioctl(4, TCGETS, 0xfffff60c19b0)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(4, 0, SEEK_CUR)                   = 0
lseek(4, 0, SEEK_CUR)                   = 0
fstat(4, {st_mode=S_IFREG|0644, st_size=6128, ...}) = 0
read(4, "# don't import any costly module"..., 6129) = 6128
read(4, "", 1)                          = 0
close(4)                                = 0
brk(0xaaab0b5e1000)                     = 0xaaab0b5e1000
brk(0xaaab0b5da000)                     = 0xaaab0b5da000
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__init__.py", {st_mode=S_IFREG|0644, st_size=6128, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__pycache__", 0xfffff60c1db0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
mkdirat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__pycache__", 0777) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__pycache__/__init__.cpython-311.pyc.281473629702160", O_WRONLY|O_CREAT|O_EXCL|O_CLOEXEC, 0644) = 4
fstat(4, {st_mode=S_IFREG|0644, st_size=0, ...}) = 0
write(4, "\247\r\r\n\0\0\0\0\10V=c\360\27\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\6\0\0"..., 11164) = 11164
close(4)                                = 0
renameat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__pycache__/__init__.cpython-311.pyc.281473629702160", AT_FDCWD, "/usr/local/lib/python3.11/site-packages/_distutils_hack/__pycache__/__init__.cpython-311.pyc") = 0
read(3, "", 8192)                       = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/lib-dynload", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/lib-dynload", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.11/site-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/app/hello_world.py", {st_mode=S_IFREG|0644, st_size=109, ...}, 0) = 0
openat(AT_FDCWD, "/app/hello_world.py", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=109, ...}) = 0
ioctl(3, TCGETS, 0xfffff60c2c60)        = -1 ENOSYS (Function not implemented)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, -22, SEEK_END)                 = 87
lseek(3, 0, SEEK_CUR)                   = 87
read(3, "_main__\":\n    hello()\n", 4096) = 22
lseek(3, 0, SEEK_END)                   = 109
lseek(3, 0, SEEK_CUR)                   = 109
lseek(3, 0, SEEK_SET)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
fstat(3, {st_mode=S_IFREG|0644, st_size=109, ...}) = 0
read(3, "def hello():\n    # This is a com"..., 110) = 109
read(3, "", 1)                          = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/app/hello_world.py", {st_mode=S_IFREG|0644, st_size=109, ...}, 0) = 0
readlinkat(AT_FDCWD, "hello_world.py", 0xfffff60b2510, 4096) = -1 EINVAL (Invalid argument)
getcwd("/app", 4096)                    = 5
newfstatat(AT_FDCWD, "/app/hello_world.py", {st_mode=S_IFREG|0644, st_size=109, ...}, AT_SYMLINK_NOFOLLOW) = 0
openat(AT_FDCWD, "/app/hello_world.py", O_RDONLY) = 3
ioctl(3, FIOCLEX)                       = 0
fstat(3, {st_mode=S_IFREG|0644, st_size=109, ...}) = 0
ioctl(3, TCGETS, 0xfffff60c3460)        = -1 ENOSYS (Function not implemented)
lseek(3, 0, SEEK_CUR)                   = 0
fstat(3, {st_mode=S_IFREG|0644, st_size=109, ...}) = 0
read(3, "def hello():\n    # This is a com"..., 4096) = 109
lseek(3, 0, SEEK_SET)                   = 0
read(3, "def hello():\n    # This is a com"..., 4096) = 109
read(3, "", 4096)                       = 0
close(3)                                = 0
write(1, "Hello, world\n", 13)          = 13
rt_sigaction(SIGINT, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=SA_ONSTACK}, {sa_handler=0xffffaffd50ec, sa_mask=[], sa_flags=SA_ONSTACK}, 8) = 0
munmap(0xffffafb05000, 1048576)         = 0
munmap(0xffffb04a6000, 16384)           = 0
exit_group(0)                           = ?
+++ exited with 0 +++
```

```sh
$ docker run -it -v $(pwd):/app helloworld:pyconjp-2022 ls -la /usr/local/bin/python3
lrwxrwxrwx 1 root root 10 Oct  5 10:01 /usr/local/bin/python3 -> python3.11

$ docker run -it -v $(pwd):/app helloworld:pyconjp-2022 readelf -h /usr/local/bin/python3.11
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00 
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              DYN (Shared object file)
  Machine:                           AArch64
  Version:                           0x1
  Entry point address:               0x880
  Start of program headers:          64 (bytes into file)
  Start of section headers:          4440 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           56 (bytes)
  Number of program headers:         9
  Size of section headers:           64 (bytes)
  Number of section headers:         27
  Section header string table index: 26

$ docker run -it -v $(pwd):/app helloworld:pyconjp-2022 objdump -D /usr/local/bin/python3.11

/usr/local/bin/python3.11:     file format elf64-littleaarch64


Disassembly of section .interp:

0000000000000238 <.interp>:
 238:	62696c2f 	.inst	0x62696c2f ; undefined
 23c:	2d646c2f 	ldp	s15, s27, [x1, #-224]
 240:	756e696c 	.inst	0x756e696c ; undefined
 244:	61612d78 	.inst	0x61612d78 ; undefined
 248:	36686372 	tbz	w18, #13, eb4 <_IO_stdin_used@@Base+0x470>
 24c:	6f732e34 	.inst	0x6f732e34 ; undefined
 250:	Address 0x0000000000000250 is out of bounds.


Disassembly of section .note.gnu.build-id:

0000000000000254 <.note.gnu.build-id>:
 254:	00000004 	udf	#4
 258:	00000014 	udf	#20
 25c:	00000003 	udf	#3
 260:	00554e47 	.inst	0x00554e47 ; undefined
 264:	9ffefebb 	.inst	0x9ffefebb ; undefined
 268:	12815aa8 	mov	w8, #0xfffff52a            	// #-2774
 26c:	74294ec6 	.inst	0x74294ec6 ; undefined
 270:	b0d8024a 	adrp	x10, ffffffffb0049000 <__bss_end__@@Base+0xffffffffb0037fc0>
 274:	2001309e 	.inst	0x2001309e ; undefined

Disassembly of section .note.ABI-tag:

0000000000000278 <.note.ABI-tag>:
 278:	00000004 	udf	#4
 27c:	00000010 	udf	#16
 280:	00000001 	udf	#1
 284:	00554e47 	.inst	0x00554e47 ; undefined
 288:	00000000 	udf	#0
 28c:	00000003 	udf	#3
 290:	00000007 	udf	#7
 294:	00000000 	udf	#0

Disassembly of section .gnu.hash:

0000000000000298 <.gnu.hash>:
 298:	00000003 	udf	#3
 29c:	0000000a 	udf	#10
 2a0:	00000002 	udf	#2
 2a4:	00000007 	udf	#7
 2a8:	40801091 	.inst	0x40801091 ; undefined
 2ac:	88342100 	stxp	w20, w0, w8, [x8]
 2b0:	4d040408 	.inst	0x4d040408 ; undefined
 2b4:	00400508 	.inst	0x00400508 ; undefined
 2b8:	0000000a 	udf	#10
 2bc:	0000000e 	udf	#14
 2c0:	00000014 	udf	#20
 2c4:	e834af00 	.inst	0xe834af00 ; undefined
 2c8:	ecd54542 	.inst	0xecd54542 ; undefined
 2cc:	d643096a 	.inst	0xd643096a ; undefined
 2d0:	7c92e3bb 	.inst	0x7c92e3bb ; undefined
 2d4:	0b973a0c 	add	w12, w16, w23, asr #14
 2d8:	1b57dabe 	.inst	0x1b57dabe ; undefined
 2dc:	c0e34bac 	.inst	0xc0e34bac ; undefined
 2e0:	9ee3cdda 	.inst	0x9ee3cdda ; undefined
 2e4:	eddb6232 	.inst	0xeddb6232 ; undefined
 2e8:	1c5871d9 	ldr	s25, b1120 <__bss_end__@@Base+0xa00e0>
 2ec:	9ee2140c 	.inst	0x9ee2140c ; undefined
 2f0:	943c5476 	bl	f154c8 <__bss_end__@@Base+0xf04488>
 2f4:	7997ef59 	ldrsh	x25, [x26, #3062]

Disassembly of section .dynsym:

00000000000002f8 <.dynsym>:
	...
 314:	000b0003 	.inst	0x000b0003 ; undefined
 318:	000007f0 	udf	#2032
	...
 32c:	00170003 	.inst	0x00170003 ; undefined
 330:	00011028 	.inst	0x00011028 ; undefined
	...
 340:	0000006d 	udf	#109
 344:	00000012 	udf	#18
	...
 358:	00000037 	udf	#55
 35c:	00000020 	udf	#32
	...
 370:	00000007 	udf	#7
 374:	00000022 	udf	#34
	...
 388:	00000016 	udf	#22
 38c:	00000012 	udf	#18
	...
 3a0:	00000028 	udf	#40
 3a4:	00000020 	udf	#32
	...
 3b8:	00000001 	udf	#1
 3bc:	00000012 	udf	#18
	...
 3d0:	00000053 	udf	#83
 3d4:	00000020 	udf	#32
	...
 3e8:	000000bf 	udf	#191
 3ec:	00180010 	.inst	0x00180010 ; undefined
 3f0:	00011040 	.inst	0x00011040 ; undefined
	...
 400:	000000b7 	udf	#183
 404:	00170010 	.inst	0x00170010 ; undefined
 408:	00011038 	.inst	0x00011038 ; undefined
	...
 418:	000000ca 	udf	#202
 41c:	00170010 	.inst	0x00170010 ; undefined
 420:	00011028 	.inst	0x00011028 ; undefined
	...
 430:	000000f6 	udf	#246
 434:	00180010 	.inst	0x00180010 ; undefined
 438:	00011040 	.inst	0x00011040 ; undefined
	...
 448:	000000cc 	udf	#204
 44c:	00170020 	.inst	0x00170020 ; undefined
 450:	00011028 	.inst	0x00011028 ; undefined
	...
 460:	000000be 	udf	#190
 464:	00180010 	.inst	0x00180010 ; undefined
 468:	00011040 	.inst	0x00011040 ; undefined
	...
 478:	000000d7 	udf	#215
 47c:	000f0011 	.inst	0x000f0011 ; undefined
 480:	00000a44 	udf	#2628
 484:	00000000 	udf	#0
 488:	00000004 	udf	#4
 48c:	00000000 	udf	#0
 490:	000000e6 	udf	#230
 494:	000d0012 	.inst	0x000d0012 ; undefined
 498:	000009b0 	udf	#2480
 49c:	00000000 	udf	#0
 4a0:	0000007c 	udf	#124
 4a4:	00000000 	udf	#0
 4a8:	000000d0 	udf	#208
 4ac:	000d0012 	.inst	0x000d0012 ; undefined
 4b0:	00000880 	udf	#2176
	...
 4c0:	00000103 	udf	#259
 4c4:	00180010 	.inst	0x00180010 ; undefined
 4c8:	00011038 	.inst	0x00011038 ; undefined
	...
 4d8:	00000099 	udf	#153
 4dc:	000d0012 	.inst	0x000d0012 ; undefined
 4e0:	00000a30 	udf	#2608
 4e4:	00000000 	udf	#0
 4e8:	00000004 	udf	#4
 4ec:	00000000 	udf	#0
 4f0:	000000a9 	udf	#169
 4f4:	00180010 	.inst	0x00180010 ; undefined
 4f8:	00011038 	.inst	0x00011038 ; undefined
	...
 508:	000000fb 	udf	#251
 50c:	00180010 	.inst	0x00180010 ; undefined
 510:	00011040 	.inst	0x00011040 ; undefined
	...

Disassembly of section .dynstr:

0000000000000520 <.dynstr>:
 520:	6f626100 	umlsl2	v0.4s, v8.8h, v2.h[2]
 524:	5f007472 	.inst	0x5f007472 ; undefined
 528:	6178635f 	.inst	0x6178635f ; undefined
 52c:	6e69665f 	umax	v31.8h, v18.8h, v9.8h
 530:	7a696c61 	.inst	0x7a696c61 ; undefined
 534:	5f5f0065 	.inst	0x5f5f0065 ; undefined
 538:	6362696c 	.inst	0x6362696c ; undefined
 53c:	6174735f 	.inst	0x6174735f ; undefined
 540:	6d5f7472 	ldp	d18, d29, [x3, #496]
 544:	006e6961 	.inst	0x006e6961 ; undefined
 548:	6d675f5f 	ldp	d31, d23, [x26, #-400]
 54c:	735f6e6f 	.inst	0x735f6e6f ; undefined
 550:	74726174 	.inst	0x74726174 ; undefined
 554:	5f005f5f 	.inst	0x5f005f5f ; undefined
 558:	5f4d5449 	shl	d9, d2, #13
 55c:	65726564 	fnmls	z4.h, p1/m, z11.h, z18.h
 560:	74736967 	.inst	0x74736967 ; undefined
 564:	4d547265 	.inst	0x4d547265 ; undefined
 568:	6e6f6c43 	umin	v3.8h, v2.8h, v15.8h
 56c:	62615465 	.inst	0x62615465 ; undefined
 570:	5f00656c 	.inst	0x5f00656c ; undefined
 574:	5f4d5449 	shl	d9, d2, #13
 578:	69676572 	ldpsw	x18, x25, [x11, #-200]
 57c:	72657473 	.inst	0x72657473 ; undefined
 580:	6c434d54 	ldnp	d20, d19, [x10, #48]
 584:	54656e6f 	b.nv	cb350 <__bss_end__@@Base+0xba310>
 588:	656c6261 	fnmls	z1.h, p0/m, z19.h, z12.h
 58c:	5f795000 	.inst	0x5f795000 ; undefined
 590:	65747942 	fnmls	z2.h, p6/m, z10.h, z20.h
 594:	69614d73 	.inst	0x69614d73 ; undefined
 598:	696c006e 	ldpsw	x14, x0, [x3, #-160]
 59c:	74797062 	.inst	0x74797062 ; undefined
 5a0:	336e6f68 	.inst	0x336e6f68 ; undefined
 5a4:	2e31312e 	usubw	v14.8h, v9.8h, v17.8b
 5a8:	312e6f73 	adds	w19, w27, #0xb9b
 5ac:	6c00302e 	stnp	d14, d12, [x1]
 5b0:	2e636269 	rsubhn	v9.4h, v19.4s, v3.4s
 5b4:	362e6f73 	tbz	w19, #5, ffffffffffffd3a0 <__bss_end__@@Base+0xfffffffffffec360>
 5b8:	6c5f5f00 	ldnp	d0, d23, [x24, #496]
 5bc:	5f636269 	.inst	0x5f636269 ; undefined
 5c0:	5f757363 	sqdmlsl	s3, h27, v5.h[3]
 5c4:	696e6966 	ldpsw	x6, x26, [x11, #-144]
 5c8:	625f5f00 	.inst	0x625f5f00 ; undefined
 5cc:	735f7373 	.inst	0x735f7373 ; undefined
 5d0:	74726174 	.inst	0x74726174 ; undefined
 5d4:	5f005f5f 	.inst	0x5f005f5f ; undefined
 5d8:	74616465 	.inst	0x74616465 ; undefined
 5dc:	5f5f0061 	.inst	0x5f5f0061 ; undefined
 5e0:	5f737362 	sqdmlsl	s2, h27, v3.h[3]
 5e4:	5f646e65 	.inst	0x5f646e65 ; undefined
 5e8:	5f5f005f 	.inst	0x5f5f005f ; undefined
 5ec:	61746164 	.inst	0x61746164 ; undefined
 5f0:	6174735f 	.inst	0x6174735f ; undefined
 5f4:	5f007472 	.inst	0x5f007472 ; undefined
 5f8:	735f4f49 	.inst	0x735f4f49 ; undefined
 5fc:	6e696474 	umax	v20.8h, v3.8h, v9.8h
 600:	6573755f 	fnmls	z31.h, p5/m, z10.h, z19.h
 604:	5f5f0064 	.inst	0x5f5f0064 ; undefined
 608:	6362696c 	.inst	0x6362696c ; undefined
 60c:	7573635f 	.inst	0x7573635f ; undefined
 610:	696e695f 	ldpsw	xzr, x26, [x10, #-144]
 614:	655f0074 	fadd	z20.h, z3.h, z31.h
 618:	5f00646e 	.inst	0x5f00646e ; undefined
 61c:	646e655f 	.inst	0x646e655f ; undefined
 620:	5f005f5f 	.inst	0x5f005f5f ; undefined
 624:	7373625f 	.inst	0x7373625f ; undefined
 628:	6174735f 	.inst	0x6174735f ; undefined
 62c:	47007472 	.inst	0x47007472 ; undefined
 630:	4342494c 	.inst	0x4342494c ; undefined
 634:	312e325f 	cmn	w18, #0xb8c
 638:	Address 0x0000000000000638 is out of bounds.


Disassembly of section .gnu.version:

000000000000063a <.gnu.version>:
	...
 642:	00020000 	.inst	0x00020000 ; undefined
 646:	00000002 	udf	#2
 64a:	00000002 	udf	#2
 64e:	00010001 	.inst	0x00010001 ; undefined
 652:	00010001 	.inst	0x00010001 ; undefined
 656:	00010001 	.inst	0x00010001 ; undefined
 65a:	00010001 	.inst	0x00010001 ; undefined
 65e:	00010001 	.inst	0x00010001 ; undefined
 662:	00010001 	.inst	0x00010001 ; undefined
 666:	Address 0x0000000000000666 is out of bounds.


Disassembly of section .gnu.version_r:

0000000000000668 <.gnu.version_r>:
 668:	00010001 	.inst	0x00010001 ; undefined
 66c:	0000008f 	udf	#143
 670:	00000010 	udf	#16
 674:	00000000 	udf	#0
 678:	06969197 	.inst	0x06969197 ; undefined
 67c:	00020000 	.inst	0x00020000 ; undefined
 680:	0000010f 	udf	#271
 684:	00000000 	udf	#0

Disassembly of section .rela.dyn:

0000000000000688 <.rela.dyn>:
 688:	00010da8 	.inst	0x00010da8 ; undefined
 68c:	00000000 	udf	#0
 690:	00000403 	udf	#1027
 694:	00000000 	udf	#0
 698:	00000990 	udf	#2448
 69c:	00000000 	udf	#0
 6a0:	00010db0 	.inst	0x00010db0 ; undefined
 6a4:	00000000 	udf	#0
 6a8:	00000403 	udf	#1027
 6ac:	00000000 	udf	#0
 6b0:	00000940 	udf	#2368
 6b4:	00000000 	udf	#0
 6b8:	00010fb0 	.inst	0x00010fb0 ; undefined
 6bc:	00000000 	udf	#0
 6c0:	00000403 	udf	#1027
 6c4:	00000000 	udf	#0
 6c8:	00000a30 	udf	#2608
 6cc:	00000000 	udf	#0
 6d0:	00010fd0 	.inst	0x00010fd0 ; undefined
 6d4:	00000000 	udf	#0
 6d8:	00000403 	udf	#1027
 6dc:	00000000 	udf	#0
 6e0:	000009b0 	udf	#2480
 6e4:	00000000 	udf	#0
 6e8:	00010fd8 	.inst	0x00010fd8 ; undefined
 6ec:	00000000 	udf	#0
 6f0:	00000403 	udf	#1027
 6f4:	00000000 	udf	#0
 6f8:	000009a0 	udf	#2464
 6fc:	00000000 	udf	#0
 700:	00011030 	.inst	0x00011030 ; undefined
 704:	00000000 	udf	#0
 708:	00000403 	udf	#1027
 70c:	00000000 	udf	#0
 710:	00011030 	.inst	0x00011030 ; undefined
 714:	00000000 	udf	#0
 718:	00010fb8 	.inst	0x00010fb8 ; undefined
 71c:	00000000 	udf	#0
 720:	00000401 	udf	#1025
 724:	00000004 	udf	#4
	...
 730:	00010fc0 	.inst	0x00010fc0 ; undefined
 734:	00000000 	udf	#0
 738:	00000401 	udf	#1025
 73c:	00000005 	udf	#5
	...
 748:	00010fc8 	.inst	0x00010fc8 ; undefined
 74c:	00000000 	udf	#0
 750:	00000401 	udf	#1025
 754:	00000007 	udf	#7
	...
 760:	00010fe0 	.inst	0x00010fe0 ; undefined
 764:	00000000 	udf	#0
 768:	00000401 	udf	#1025
 76c:	00000009 	udf	#9
	...

Disassembly of section .rela.plt:

0000000000000778 <.rela.plt>:
 778:	00011000 	.inst	0x00011000 ; undefined
 77c:	00000000 	udf	#0
 780:	00000402 	udf	#1026
 784:	00000003 	udf	#3
	...
 790:	00011008 	.inst	0x00011008 ; undefined
 794:	00000000 	udf	#0
 798:	00000402 	udf	#1026
 79c:	00000005 	udf	#5
	...
 7a8:	00011010 	.inst	0x00011010 ; undefined
 7ac:	00000000 	udf	#0
 7b0:	00000402 	udf	#1026
 7b4:	00000006 	udf	#6
	...
 7c0:	00011018 	.inst	0x00011018 ; undefined
 7c4:	00000000 	udf	#0
 7c8:	00000402 	udf	#1026
 7cc:	00000007 	udf	#7
	...
 7d8:	00011020 	.inst	0x00011020 ; undefined
 7dc:	00000000 	udf	#0
 7e0:	00000402 	udf	#1026
 7e4:	00000008 	udf	#8
	...

Disassembly of section .init:

00000000000007f0 <.init>:
 7f0:	a9bf7bfd 	stp	x29, x30, [sp, #-16]!
 7f4:	910003fd 	mov	x29, sp
 7f8:	94000030 	bl	8b8 <_start@@Base+0x38>
 7fc:	a8c17bfd 	ldp	x29, x30, [sp], #16
 800:	d65f03c0 	ret

Disassembly of section .plt:

0000000000000810 <Py_BytesMain@plt-0x20>:
 810:	a9bf7bf0 	stp	x16, x30, [sp, #-16]!
 814:	90000090 	adrp	x16, 10000 <_IO_stdin_used@@Base+0xf5bc>
 818:	f947fe11 	ldr	x17, [x16, #4088]
 81c:	913fe210 	add	x16, x16, #0xff8
 820:	d61f0220 	br	x17
 824:	d503201f 	nop
 828:	d503201f 	nop
 82c:	d503201f 	nop

0000000000000830 <Py_BytesMain@plt>:
 830:	b0000090 	adrp	x16, 11000 <Py_BytesMain>
 834:	f9400211 	ldr	x17, [x16]
 838:	91000210 	add	x16, x16, #0x0
 83c:	d61f0220 	br	x17

0000000000000840 <__cxa_finalize@plt>:
 840:	b0000090 	adrp	x16, 11000 <Py_BytesMain>
 844:	f9400611 	ldr	x17, [x16, #8]
 848:	91002210 	add	x16, x16, #0x8
 84c:	d61f0220 	br	x17

0000000000000850 <__libc_start_main@plt>:
 850:	b0000090 	adrp	x16, 11000 <Py_BytesMain>
 854:	f9400a11 	ldr	x17, [x16, #16]
 858:	91004210 	add	x16, x16, #0x10
 85c:	d61f0220 	br	x17

0000000000000860 <__gmon_start__@plt>:
 860:	b0000090 	adrp	x16, 11000 <Py_BytesMain>
 864:	f9400e11 	ldr	x17, [x16, #24]
 868:	91006210 	add	x16, x16, #0x18
 86c:	d61f0220 	br	x17

0000000000000870 <abort@plt>:
 870:	b0000090 	adrp	x16, 11000 <Py_BytesMain>
 874:	f9401211 	ldr	x17, [x16, #32]
 878:	91008210 	add	x16, x16, #0x20
 87c:	d61f0220 	br	x17

Disassembly of section .text:

0000000000000880 <_start@@Base>:
 880:	d280001d 	mov	x29, #0x0                   	// #0
 884:	d280001e 	mov	x30, #0x0                   	// #0
 888:	aa0003e5 	mov	x5, x0
 88c:	f94003e1 	ldr	x1, [sp]
 890:	910023e2 	add	x2, sp, #0x8
 894:	910003e6 	mov	x6, sp
 898:	90000080 	adrp	x0, 10000 <_IO_stdin_used@@Base+0xf5bc>
 89c:	f947ec00 	ldr	x0, [x0, #4056]
 8a0:	90000083 	adrp	x3, 10000 <_IO_stdin_used@@Base+0xf5bc>
 8a4:	f947e863 	ldr	x3, [x3, #4048]
 8a8:	90000084 	adrp	x4, 10000 <_IO_stdin_used@@Base+0xf5bc>
 8ac:	f947d884 	ldr	x4, [x4, #4016]
 8b0:	97ffffe8 	bl	850 <__libc_start_main@plt>
 8b4:	97ffffef 	bl	870 <abort@plt>
 8b8:	90000080 	adrp	x0, 10000 <_IO_stdin_used@@Base+0xf5bc>
 8bc:	f947e400 	ldr	x0, [x0, #4040]
 8c0:	b4000040 	cbz	x0, 8c8 <_start@@Base+0x48>
 8c4:	17ffffe7 	b	860 <__gmon_start__@plt>
 8c8:	d65f03c0 	ret
 8cc:	d503201f 	nop
 8d0:	b0000080 	adrp	x0, 11000 <Py_BytesMain>
 8d4:	9100e000 	add	x0, x0, #0x38
 8d8:	b0000081 	adrp	x1, 11000 <Py_BytesMain>
 8dc:	9100e021 	add	x1, x1, #0x38
 8e0:	eb00003f 	cmp	x1, x0
 8e4:	540000c0 	b.eq	8fc <_start@@Base+0x7c>  // b.none
 8e8:	90000081 	adrp	x1, 10000 <_IO_stdin_used@@Base+0xf5bc>
 8ec:	f947dc21 	ldr	x1, [x1, #4024]
 8f0:	b4000061 	cbz	x1, 8fc <_start@@Base+0x7c>
 8f4:	aa0103f0 	mov	x16, x1
 8f8:	d61f0200 	br	x16
 8fc:	d65f03c0 	ret
 900:	b0000080 	adrp	x0, 11000 <Py_BytesMain>
 904:	9100e000 	add	x0, x0, #0x38
 908:	b0000081 	adrp	x1, 11000 <Py_BytesMain>
 90c:	9100e021 	add	x1, x1, #0x38
 910:	cb000021 	sub	x1, x1, x0
 914:	d37ffc22 	lsr	x2, x1, #63
 918:	8b810c41 	add	x1, x2, x1, asr #3
 91c:	9341fc21 	asr	x1, x1, #1
 920:	b40000c1 	cbz	x1, 938 <_start@@Base+0xb8>
 924:	90000082 	adrp	x2, 10000 <_IO_stdin_used@@Base+0xf5bc>
 928:	f947f042 	ldr	x2, [x2, #4064]
 92c:	b4000062 	cbz	x2, 938 <_start@@Base+0xb8>
 930:	aa0203f0 	mov	x16, x2
 934:	d61f0200 	br	x16
 938:	d65f03c0 	ret
 93c:	d503201f 	nop
 940:	a9be7bfd 	stp	x29, x30, [sp, #-32]!
 944:	910003fd 	mov	x29, sp
 948:	f9000bf3 	str	x19, [sp, #16]
 94c:	b0000093 	adrp	x19, 11000 <Py_BytesMain>
 950:	3940e260 	ldrb	w0, [x19, #56]
 954:	35000140 	cbnz	w0, 97c <_start@@Base+0xfc>
 958:	90000080 	adrp	x0, 10000 <_IO_stdin_used@@Base+0xf5bc>
 95c:	f947e000 	ldr	x0, [x0, #4032]
 960:	b4000080 	cbz	x0, 970 <_start@@Base+0xf0>
 964:	b0000080 	adrp	x0, 11000 <Py_BytesMain>
 968:	f9401800 	ldr	x0, [x0, #48]
 96c:	97ffffb5 	bl	840 <__cxa_finalize@plt>
 970:	97ffffd8 	bl	8d0 <_start@@Base+0x50>
 974:	52800020 	mov	w0, #0x1                   	// #1
 978:	3900e260 	strb	w0, [x19, #56]
 97c:	f9400bf3 	ldr	x19, [sp, #16]
 980:	a8c27bfd 	ldp	x29, x30, [sp], #32
 984:	d65f03c0 	ret
 988:	d503201f 	nop
 98c:	d503201f 	nop
 990:	17ffffdc 	b	900 <_start@@Base+0x80>
 994:	d503201f 	nop
 998:	d503201f 	nop
 99c:	d503201f 	nop
 9a0:	17ffffa4 	b	830 <Py_BytesMain@plt>
 9a4:	d503201f 	nop
 9a8:	d503201f 	nop
 9ac:	d503201f 	nop

00000000000009b0 <__libc_csu_init@@Base>:
 9b0:	a9bc7bfd 	stp	x29, x30, [sp, #-64]!
 9b4:	910003fd 	mov	x29, sp
 9b8:	a90153f3 	stp	x19, x20, [sp, #16]
 9bc:	90000094 	adrp	x20, 10000 <_IO_stdin_used@@Base+0xf5bc>
 9c0:	9136c294 	add	x20, x20, #0xdb0
 9c4:	a9025bf5 	stp	x21, x22, [sp, #32]
 9c8:	90000095 	adrp	x21, 10000 <_IO_stdin_used@@Base+0xf5bc>
 9cc:	9136a2b5 	add	x21, x21, #0xda8
 9d0:	cb150294 	sub	x20, x20, x21
 9d4:	2a0003f6 	mov	w22, w0
 9d8:	a90363f7 	stp	x23, x24, [sp, #48]
 9dc:	aa0103f7 	mov	x23, x1
 9e0:	aa0203f8 	mov	x24, x2
 9e4:	9343fe94 	asr	x20, x20, #3
 9e8:	97ffff82 	bl	7f0 <Py_BytesMain@plt-0x40>
 9ec:	b4000174 	cbz	x20, a18 <__libc_csu_init@@Base+0x68>
 9f0:	d2800013 	mov	x19, #0x0                   	// #0
 9f4:	d503201f 	nop
 9f8:	f8737aa3 	ldr	x3, [x21, x19, lsl #3]
 9fc:	aa1803e2 	mov	x2, x24
 a00:	91000673 	add	x19, x19, #0x1
 a04:	aa1703e1 	mov	x1, x23
 a08:	2a1603e0 	mov	w0, w22
 a0c:	d63f0060 	blr	x3
 a10:	eb13029f 	cmp	x20, x19
 a14:	54ffff21 	b.ne	9f8 <__libc_csu_init@@Base+0x48>  // b.any
 a18:	a94153f3 	ldp	x19, x20, [sp, #16]
 a1c:	a9425bf5 	ldp	x21, x22, [sp, #32]
 a20:	a94363f7 	ldp	x23, x24, [sp, #48]
 a24:	a8c47bfd 	ldp	x29, x30, [sp], #64
 a28:	d65f03c0 	ret
 a2c:	d503201f 	nop

0000000000000a30 <__libc_csu_fini@@Base>:
 a30:	d65f03c0 	ret

Disassembly of section .fini:

0000000000000a34 <.fini>:
 a34:	a9bf7bfd 	stp	x29, x30, [sp, #-16]!
 a38:	910003fd 	mov	x29, sp
 a3c:	a8c17bfd 	ldp	x29, x30, [sp], #16
 a40:	d65f03c0 	ret

Disassembly of section .rodata:

0000000000000a44 <_IO_stdin_used@@Base>:
 a44:	00020001 	.inst	0x00020001 ; undefined

Disassembly of section .eh_frame_hdr:

0000000000000a48 <.eh_frame_hdr>:
 a48:	3b031b01 	.inst	0x3b031b01 ; undefined
 a4c:	00000044 	udf	#68
 a50:	00000007 	udf	#7
 a54:	fffffe88 	.inst	0xfffffe88 ; undefined
 a58:	0000005c 	udf	#92
 a5c:	fffffeb8 	.inst	0xfffffeb8 ; undefined
 a60:	00000070 	udf	#112
 a64:	fffffef8 	.inst	0xfffffef8 ; undefined
 a68:	00000084 	udf	#132
 a6c:	ffffff48 	.inst	0xffffff48 ; undefined
 a70:	000000a8 	udf	#168
 a74:	ffffff58 	.inst	0xffffff58 ; undefined
 a78:	000000c0 	udf	#192
 a7c:	ffffff68 	.inst	0xffffff68 ; undefined
 a80:	000000d8 	udf	#216
 a84:	ffffffe8 	.inst	0xffffffe8 ; undefined
 a88:	0000010c 	udf	#268

Disassembly of section .eh_frame:

0000000000000a90 <.eh_frame>:
 a90:	00000010 	udf	#16
 a94:	00000000 	udf	#0
 a98:	00527a01 	.inst	0x00527a01 ; undefined
 a9c:	011e7804 	.inst	0x011e7804 ; undefined
 aa0:	001f0c1b 	.inst	0x001f0c1b ; undefined
 aa4:	00000010 	udf	#16
 aa8:	00000018 	udf	#24
 aac:	fffffe24 	.inst	0xfffffe24 ; undefined
 ab0:	00000030 	udf	#48
 ab4:	00000000 	udf	#0
 ab8:	00000010 	udf	#16
 abc:	0000002c 	udf	#44
 ac0:	fffffe40 	.inst	0xfffffe40 ; undefined
 ac4:	0000003c 	udf	#60
 ac8:	00000000 	udf	#0
 acc:	00000020 	udf	#32
 ad0:	00000040 	udf	#64
 ad4:	fffffe6c 	.inst	0xfffffe6c ; undefined
 ad8:	00000048 	udf	#72
 adc:	200e4100 	.inst	0x200e4100 ; undefined
 ae0:	039e049d 	.inst	0x039e049d ; undefined
 ae4:	4e029342 	.inst	0x4e029342 ; undefined
 ae8:	0ed3ddde 	.inst	0x0ed3ddde ; undefined
 aec:	00000000 	udf	#0
 af0:	00000014 	udf	#20
 af4:	00000064 	udf	#100
 af8:	fffffe98 	.inst	0xfffffe98 ; undefined
 afc:	00000004 	udf	#4
	...
 b08:	00000014 	udf	#20
 b0c:	0000007c 	udf	#124
 b10:	fffffe90 	.inst	0xfffffe90 ; undefined
 b14:	00000004 	udf	#4
	...
 b20:	00000030 	udf	#48
 b24:	00000094 	udf	#148
 b28:	fffffe88 	.inst	0xfffffe88 ; undefined
 b2c:	0000007c 	udf	#124
 b30:	400e4100 	.inst	0x400e4100 ; undefined
 b34:	079e089d 	.inst	0x079e089d ; undefined
 b38:	94069342 	bl	1a5840 <__bss_end__@@Base+0x194800>
 b3c:	04954305 	mla	z5.s, p0/m, z24.s, z21.s
 b40:	97450396 	bl	fffffffffd141998 <__bss_end__@@Base+0xfffffffffd130958>
 b44:	53019802 	.inst	0x53019802 ; undefined
 b48:	d8d7ddde 	prfm	#0x1e, fffffffffffb0700 <__bss_end__@@Base+0xfffffffffff9f6c0>
 b4c:	d4d3d6d5 	.inst	0xd4d3d6d5 ; undefined
 b50:	0000000e 	udf	#14
 b54:	00000010 	udf	#16
 b58:	000000c8 	udf	#200
 b5c:	fffffed4 	.inst	0xfffffed4 ; undefined
 b60:	00000004 	udf	#4
	...

Disassembly of section .init_array:

0000000000010da8 <.init_array>:
   10da8:	00000990 	udf	#2448
   10dac:	00000000 	udf	#0

Disassembly of section .fini_array:

0000000000010db0 <.fini_array>:
   10db0:	00000940 	udf	#2368
   10db4:	00000000 	udf	#0

Disassembly of section .dynamic:

0000000000010db8 <.dynamic>:
   10db8:	00000001 	udf	#1
   10dbc:	00000000 	udf	#0
   10dc0:	0000007a 	udf	#122
   10dc4:	00000000 	udf	#0
   10dc8:	00000001 	udf	#1
   10dcc:	00000000 	udf	#0
   10dd0:	0000008f 	udf	#143
   10dd4:	00000000 	udf	#0
   10dd8:	0000000c 	udf	#12
   10ddc:	00000000 	udf	#0
   10de0:	000007f0 	udf	#2032
   10de4:	00000000 	udf	#0
   10de8:	0000000d 	udf	#13
   10dec:	00000000 	udf	#0
   10df0:	00000a34 	udf	#2612
   10df4:	00000000 	udf	#0
   10df8:	00000019 	udf	#25
   10dfc:	00000000 	udf	#0
   10e00:	00010da8 	.inst	0x00010da8 ; undefined
   10e04:	00000000 	udf	#0
   10e08:	0000001b 	udf	#27
   10e0c:	00000000 	udf	#0
   10e10:	00000008 	udf	#8
   10e14:	00000000 	udf	#0
   10e18:	0000001a 	udf	#26
   10e1c:	00000000 	udf	#0
   10e20:	00010db0 	.inst	0x00010db0 ; undefined
   10e24:	00000000 	udf	#0
   10e28:	0000001c 	udf	#28
   10e2c:	00000000 	udf	#0
   10e30:	00000008 	udf	#8
   10e34:	00000000 	udf	#0
   10e38:	6ffffef5 	.inst	0x6ffffef5 ; undefined
   10e3c:	00000000 	udf	#0
   10e40:	00000298 	udf	#664
   10e44:	00000000 	udf	#0
   10e48:	00000005 	udf	#5
   10e4c:	00000000 	udf	#0
   10e50:	00000520 	udf	#1312
   10e54:	00000000 	udf	#0
   10e58:	00000006 	udf	#6
   10e5c:	00000000 	udf	#0
   10e60:	000002f8 	udf	#760
   10e64:	00000000 	udf	#0
   10e68:	0000000a 	udf	#10
   10e6c:	00000000 	udf	#0
   10e70:	0000011a 	udf	#282
   10e74:	00000000 	udf	#0
   10e78:	0000000b 	udf	#11
   10e7c:	00000000 	udf	#0
   10e80:	00000018 	udf	#24
   10e84:	00000000 	udf	#0
   10e88:	00000015 	udf	#21
	...
   10e98:	00000003 	udf	#3
   10e9c:	00000000 	udf	#0
   10ea0:	00010fe8 	.inst	0x00010fe8 ; undefined
   10ea4:	00000000 	udf	#0
   10ea8:	00000002 	udf	#2
   10eac:	00000000 	udf	#0
   10eb0:	00000078 	udf	#120
   10eb4:	00000000 	udf	#0
   10eb8:	00000014 	udf	#20
   10ebc:	00000000 	udf	#0
   10ec0:	00000007 	udf	#7
   10ec4:	00000000 	udf	#0
   10ec8:	00000017 	udf	#23
   10ecc:	00000000 	udf	#0
   10ed0:	00000778 	udf	#1912
   10ed4:	00000000 	udf	#0
   10ed8:	00000007 	udf	#7
   10edc:	00000000 	udf	#0
   10ee0:	00000688 	udf	#1672
   10ee4:	00000000 	udf	#0
   10ee8:	00000008 	udf	#8
   10eec:	00000000 	udf	#0
   10ef0:	000000f0 	udf	#240
   10ef4:	00000000 	udf	#0
   10ef8:	00000009 	udf	#9
   10efc:	00000000 	udf	#0
   10f00:	00000018 	udf	#24
   10f04:	00000000 	udf	#0
   10f08:	6ffffffb 	.inst	0x6ffffffb ; undefined
   10f0c:	00000000 	udf	#0
   10f10:	08000000 	stxrb	w0, w0, [x0]
   10f14:	00000000 	udf	#0
   10f18:	6ffffffe 	.inst	0x6ffffffe ; undefined
   10f1c:	00000000 	udf	#0
   10f20:	00000668 	udf	#1640
   10f24:	00000000 	udf	#0
   10f28:	6fffffff 	.inst	0x6fffffff ; undefined
   10f2c:	00000000 	udf	#0
   10f30:	00000001 	udf	#1
   10f34:	00000000 	udf	#0
   10f38:	6ffffff0 	.inst	0x6ffffff0 ; undefined
   10f3c:	00000000 	udf	#0
   10f40:	0000063a 	udf	#1594
   10f44:	00000000 	udf	#0
   10f48:	6ffffff9 	.inst	0x6ffffff9 ; undefined
   10f4c:	00000000 	udf	#0
   10f50:	00000006 	udf	#6
	...

Disassembly of section .got:

0000000000010fa8 <.got>:
   10fa8:	00010db8 	.inst	0x00010db8 ; undefined
   10fac:	00000000 	udf	#0
   10fb0:	00000a30 	udf	#2608
	...
   10fd0:	000009b0 	udf	#2480
   10fd4:	00000000 	udf	#0
   10fd8:	000009a0 	udf	#2464
	...

Disassembly of section .got.plt:

0000000000010fe8 <.got.plt>:
	...
   11000:	00000810 	udf	#2064
   11004:	00000000 	udf	#0
   11008:	00000810 	udf	#2064
   1100c:	00000000 	udf	#0
   11010:	00000810 	udf	#2064
   11014:	00000000 	udf	#0
   11018:	00000810 	udf	#2064
   1101c:	00000000 	udf	#0
   11020:	00000810 	udf	#2064
   11024:	00000000 	udf	#0

Disassembly of section .data:

0000000000011028 <__data_start@@Base>:
	...
   11030:	00011030 	.inst	0x00011030 ; undefined
   11034:	00000000 	udf	#0

Disassembly of section .bss:

0000000000011038 <__bss_start@@Base>:
	...

Disassembly of section .comment:

0000000000000000 <.comment>:
   0:	3a434347 	ccmn	w26, w3, #0x7, mi  // mi = first
   4:	65442820 	fmaxnmv	h0, p2, z1.h
   8:	6e616962 	fcvtxn2	v2.4s, v11.2d
   c:	2e303120 	usubw	v0.8h, v9.8h, v16.8b
  10:	2d312e32 	stp	s18, s11, [x17, #-120]
  14:	31202936 	adds	w22, w9, #0x80a
  18:	2e322e30 	uqsub	v16.8b, v17.8b, v18.8b
  1c:	30322031 	adr	x17, 64421 <__bss_end__@@Base+0x533e1>
  20:	31303132 	adds	w18, w9, #0xc0c
  24:	Address 0x0000000000000024 is out of bounds.

```

### linux/x86_64


```sh
$ docker build --platform linux/x86_64 -t helloworld:pyconjp-2022.x86 .
$ docker run -it -v $(pwd):/app helloworld:pyconjp-2022.x86 readelf -h /usr/local/bin/python3.11
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00 
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              DYN (Shared object file)
  Machine:                           Advanced Micro Devices X86-64
  Version:                           0x1
  Entry point address:               0x1050
  Start of program headers:          64 (bytes into file)
  Start of section headers:          12624 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           56 (bytes)
  Number of program headers:         11
  Size of section headers:           64 (bytes)
  Number of section headers:         28
  Section header string table index: 27

$ docker run -it -v $(pwd):/app helloworld:pyconjp-2022.x86 objdump -D -M intel /usr/local/bin/python3.11
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested

/usr/local/bin/python3.11:     file format elf64-x86-64


Disassembly of section .interp:

00000000000002a8 <.interp>:
 2a8:	2f                   	(bad)  
 2a9:	6c                   	ins    BYTE PTR es:[rdi],dx
 2aa:	69 62 36 34 2f 6c 64 	imul   esp,DWORD PTR [rdx+0x36],0x646c2f34
 2b1:	2d 6c 69 6e 75       	sub    eax,0x756e696c
 2b6:	78 2d                	js     2e5 <Py_BytesMain@plt-0xd4b>
 2b8:	78 38                	js     2f2 <Py_BytesMain@plt-0xd3e>
 2ba:	36 2d 36 34 2e 73    	ss sub eax,0x732e3436
 2c0:	6f                   	outs   dx,DWORD PTR ds:[rsi]
 2c1:	2e 32 00             	xor    al,BYTE PTR cs:[rax]

Disassembly of section .note.gnu.build-id:

00000000000002c4 <.note.gnu.build-id>:
 2c4:	04 00                	add    al,0x0
 2c6:	00 00                	add    BYTE PTR [rax],al
 2c8:	14 00                	adc    al,0x0
 2ca:	00 00                	add    BYTE PTR [rax],al
 2cc:	03 00                	add    eax,DWORD PTR [rax]
 2ce:	00 00                	add    BYTE PTR [rax],al
 2d0:	47                   	rex.RXB
 2d1:	4e 55                	rex.WRX push rbp
 2d3:	00 b8 d2 6f f6 1a    	add    BYTE PTR [rax+0x1af66fd2],bh
 2d9:	85 d8                	test   eax,ebx
 2db:	c0 05 51 45 f7 f0 e9 	rol    BYTE PTR [rip+0xfffffffff0f74551],0xe9        # fffffffff0f74833 <_end@@Base+0xfffffffff0f707fb>
 2e2:	bd a8 6d 84 4f       	mov    ebp,0x4f846da8
 2e7:	2d                   	.byte 0x2d

Disassembly of section .note.ABI-tag:

00000000000002e8 <.note.ABI-tag>:
 2e8:	04 00                	add    al,0x0
 2ea:	00 00                	add    BYTE PTR [rax],al
 2ec:	10 00                	adc    BYTE PTR [rax],al
 2ee:	00 00                	add    BYTE PTR [rax],al
 2f0:	01 00                	add    DWORD PTR [rax],eax
 2f2:	00 00                	add    BYTE PTR [rax],al
 2f4:	47                   	rex.RXB
 2f5:	4e 55                	rex.WRX push rbp
 2f7:	00 00                	add    BYTE PTR [rax],al
 2f9:	00 00                	add    BYTE PTR [rax],al
 2fb:	00 03                	add    BYTE PTR [rbx],al
 2fd:	00 00                	add    BYTE PTR [rax],al
 2ff:	00 02                	add    BYTE PTR [rdx],al
 301:	00 00                	add    BYTE PTR [rax],al
 303:	00 00                	add    BYTE PTR [rax],al
 305:	00 00                	add    BYTE PTR [rax],al
	...

Disassembly of section .gnu.hash:

0000000000000308 <.gnu.hash>:
 308:	03 00                	add    eax,DWORD PTR [rax]
 30a:	00 00                	add    BYTE PTR [rax],al
 30c:	06                   	(bad)  
 30d:	00 00                	add    BYTE PTR [rax],al
 30f:	00 01                	add    BYTE PTR [rcx],al
 311:	00 00                	add    BYTE PTR [rax],al
 313:	00 06                	add    BYTE PTR [rsi],al
 315:	00 00                	add    BYTE PTR [rax],al
 317:	00 88 51 a1 05 20    	add    BYTE PTR [rax+0x2005a151],cl
 31d:	65 84 08             	test   BYTE PTR gs:[rax],cl
 320:	06                   	(bad)  
 321:	00 00                	add    BYTE PTR [rax],al
 323:	00 0a                	add    BYTE PTR [rdx],cl
 325:	00 00                	add    BYTE PTR [rax],al
 327:	00 0f                	add    BYTE PTR [rdi],cl
 329:	00 00                	add    BYTE PTR [rax],al
 32b:	00 42 45             	add    BYTE PTR [rdx+0x45],al
 32e:	d5                   	(bad)  
 32f:	ec                   	in     al,dx
 330:	6a 09                	push   0x9
 332:	43 d6                	rex.XB (bad) 
 334:	ba e3 92 7c d1       	mov    edx,0xd17c92e3
 339:	65 ce                	gs (bad) 
 33b:	6d                   	ins    DWORD PTR es:[rdi],dx
 33c:	0c 3a                	or     al,0x3a
 33e:	97                   	xchg   edi,eax
 33f:	0b ac 4b e3 c0 da cd 	or     ebp,DWORD PTR [rbx+rcx*2-0x32253f1d]
 346:	e3 9e                	jrcxz  2e6 <Py_BytesMain@plt-0xd4a>
 348:	32 62 db             	xor    ah,BYTE PTR [rdx-0x25]
 34b:	ed                   	in     eax,dx
 34c:	d9 71 58             	fnstenv [rcx+0x58]
 34f:	1c 0d                	sbb    al,0xd
 351:	14 e2                	adc    al,0xe2
 353:	9e                   	sahf   

Disassembly of section .dynsym:

0000000000000358 <.dynsym>:
	...
 370:	67 00 00             	add    BYTE PTR [eax],al
 373:	00 12                	add    BYTE PTR [rdx],dl
	...
 385:	00 00                	add    BYTE PTR [rax],al
 387:	00 31                	add    BYTE PTR [rcx],dh
 389:	00 00                	add    BYTE PTR [rax],al
 38b:	00 20                	add    BYTE PTR [rax],ah
	...
 39d:	00 00                	add    BYTE PTR [rax],al
 39f:	00 10                	add    BYTE PTR [rax],dl
 3a1:	00 00                	add    BYTE PTR [rax],al
 3a3:	00 12                	add    BYTE PTR [rdx],dl
	...
 3b5:	00 00                	add    BYTE PTR [rax],al
 3b7:	00 22                	add    BYTE PTR [rdx],ah
 3b9:	00 00                	add    BYTE PTR [rax],al
 3bb:	00 20                	add    BYTE PTR [rax],ah
	...
 3cd:	00 00                	add    BYTE PTR [rax],al
 3cf:	00 4d 00             	add    BYTE PTR [rbp+0x0],cl
 3d2:	00 00                	add    BYTE PTR [rax],al
 3d4:	20 00                	and    BYTE PTR [rax],al
	...
 3e6:	00 00                	add    BYTE PTR [rax],al
 3e8:	a3 00 00 00 10 00 18 	movabs ds:0x3000180010000000,eax
 3ef:	00 30 
 3f1:	40 00 00             	add    BYTE PTR [rax],al
	...
 400:	aa                   	stos   BYTE PTR es:[rdi],al
 401:	00 00                	add    BYTE PTR [rax],al
 403:	00 10                	add    BYTE PTR [rax],dl
 405:	00 18                	add    BYTE PTR [rax],bl
 407:	00 20                	add    BYTE PTR [rax],ah
 409:	40 00 00             	add    BYTE PTR [rax],al
	...
 418:	d6                   	(bad)  
 419:	00 00                	add    BYTE PTR [rax],al
 41b:	00 10                	add    BYTE PTR [rax],dl
 41d:	00 19                	add    BYTE PTR [rcx],bl
 41f:	00 38                	add    BYTE PTR [rax],bh
 421:	40 00 00             	add    BYTE PTR [rax],al
	...
 430:	01 00                	add    DWORD PTR [rax],eax
 432:	00 00                	add    BYTE PTR [rax],al
 434:	22 00                	and    al,BYTE PTR [rax]
	...
 446:	00 00                	add    BYTE PTR [rax],al
 448:	ac                   	lods   al,BYTE PTR ds:[rsi]
 449:	00 00                	add    BYTE PTR [rax],al
 44b:	00 20                	add    BYTE PTR [rax],ah
 44d:	00 18                	add    BYTE PTR [rax],bl
 44f:	00 20                	add    BYTE PTR [rax],ah
 451:	40 00 00             	add    BYTE PTR [rax],al
	...
 460:	b7 00                	mov    bh,0x0
 462:	00 00                	add    BYTE PTR [rax],al
 464:	11 00                	adc    DWORD PTR [rax],eax
 466:	10 00                	adc    BYTE PTR [rax],al
 468:	00 20                	add    BYTE PTR [rax],ah
 46a:	00 00                	add    BYTE PTR [rax],al
 46c:	00 00                	add    BYTE PTR [rax],al
 46e:	00 00                	add    BYTE PTR [rax],al
 470:	04 00                	add    al,0x0
 472:	00 00                	add    BYTE PTR [rax],al
 474:	00 00                	add    BYTE PTR [rax],al
 476:	00 00                	add    BYTE PTR [rax],al
 478:	c6 00 00             	mov    BYTE PTR [rax],0x0
 47b:	00 12                	add    BYTE PTR [rdx],dl
 47d:	00 0e                	add    BYTE PTR [rsi],cl
 47f:	00 50 11             	add    BYTE PTR [rax+0x11],dl
 482:	00 00                	add    BYTE PTR [rax],al
 484:	00 00                	add    BYTE PTR [rax],al
 486:	00 00                	add    BYTE PTR [rax],al
 488:	5d                   	pop    rbp
 489:	00 00                	add    BYTE PTR [rax],al
 48b:	00 00                	add    BYTE PTR [rax],al
 48d:	00 00                	add    BYTE PTR [rax],al
 48f:	00 b0 00 00 00 12    	add    BYTE PTR [rax+0x12000000],dh
 495:	00 0e                	add    BYTE PTR [rsi],cl
 497:	00 50 10             	add    BYTE PTR [rax+0x10],dl
 49a:	00 00                	add    BYTE PTR [rax],al
 49c:	00 00                	add    BYTE PTR [rax],al
 49e:	00 00                	add    BYTE PTR [rax],al
 4a0:	2b 00                	sub    eax,DWORD PTR [rax]
 4a2:	00 00                	add    BYTE PTR [rax],al
 4a4:	00 00                	add    BYTE PTR [rax],al
 4a6:	00 00                	add    BYTE PTR [rax],al
 4a8:	db 00                	fild   DWORD PTR [rax]
 4aa:	00 00                	add    BYTE PTR [rax],al
 4ac:	10 00                	adc    BYTE PTR [rax],al
 4ae:	19 00                	sbb    DWORD PTR [rax],eax
 4b0:	30 40 00             	xor    BYTE PTR [rax+0x0],al
	...
 4bf:	00 93 00 00 00 12    	add    BYTE PTR [rbx+0x12000000],dl
 4c5:	00 0e                	add    BYTE PTR [rsi],cl
 4c7:	00 b0 11 00 00 00    	add    BYTE PTR [rax+0x11],dh
 4cd:	00 00                	add    BYTE PTR [rax],al
 4cf:	00 01                	add    BYTE PTR [rcx],al
 4d1:	00 00                	add    BYTE PTR [rax],al
 4d3:	00 00                	add    BYTE PTR [rax],al
 4d5:	00 00                	add    BYTE PTR [rax],al
	...

Disassembly of section .dynstr:

00000000000004d8 <.dynstr>:
 4d8:	00 5f 5f             	add    BYTE PTR [rdi+0x5f],bl
 4db:	63 78 61             	movsxd edi,DWORD PTR [rax+0x61]
 4de:	5f                   	pop    rdi
 4df:	66 69 6e 61 6c 69    	imul   bp,WORD PTR [rsi+0x61],0x696c
 4e5:	7a 65                	jp     54c <Py_BytesMain@plt-0xae4>
 4e7:	00 5f 5f             	add    BYTE PTR [rdi+0x5f],bl
 4ea:	6c                   	ins    BYTE PTR es:[rdi],dx
 4eb:	69 62 63 5f 73 74 61 	imul   esp,DWORD PTR [rdx+0x63],0x6174735f
 4f2:	72 74                	jb     568 <Py_BytesMain@plt-0xac8>
 4f4:	5f                   	pop    rdi
 4f5:	6d                   	ins    DWORD PTR es:[rdi],dx
 4f6:	61                   	(bad)  
 4f7:	69 6e 00 5f 5f 67 6d 	imul   ebp,DWORD PTR [rsi+0x0],0x6d675f5f
 4fe:	6f                   	outs   dx,DWORD PTR ds:[rsi]
 4ff:	6e                   	outs   dx,BYTE PTR ds:[rsi]
 500:	5f                   	pop    rdi
 501:	73 74                	jae    577 <Py_BytesMain@plt-0xab9>
 503:	61                   	(bad)  
 504:	72 74                	jb     57a <Py_BytesMain@plt-0xab6>
 506:	5f                   	pop    rdi
 507:	5f                   	pop    rdi
 508:	00 5f 49             	add    BYTE PTR [rdi+0x49],bl
 50b:	54                   	push   rsp
 50c:	4d 5f                	rex.WRB pop r15
 50e:	64 65 72 65          	fs gs jb 577 <Py_BytesMain@plt-0xab9>
 512:	67 69 73 74 65 72 54 	imul   esi,DWORD PTR [ebx+0x74],0x4d547265
 519:	4d 
 51a:	43 6c                	rex.XB ins BYTE PTR es:[rdi],dx
 51c:	6f                   	outs   dx,DWORD PTR ds:[rsi]
 51d:	6e                   	outs   dx,BYTE PTR ds:[rsi]
 51e:	65 54                	gs push rsp
 520:	61                   	(bad)  
 521:	62                   	(bad)  
 522:	6c                   	ins    BYTE PTR es:[rdi],dx
 523:	65 00 5f 49          	add    BYTE PTR gs:[rdi+0x49],bl
 527:	54                   	push   rsp
 528:	4d 5f                	rex.WRB pop r15
 52a:	72 65                	jb     591 <Py_BytesMain@plt-0xa9f>
 52c:	67 69 73 74 65 72 54 	imul   esi,DWORD PTR [ebx+0x74],0x4d547265
 533:	4d 
 534:	43 6c                	rex.XB ins BYTE PTR es:[rdi],dx
 536:	6f                   	outs   dx,DWORD PTR ds:[rsi]
 537:	6e                   	outs   dx,BYTE PTR ds:[rsi]
 538:	65 54                	gs push rsp
 53a:	61                   	(bad)  
 53b:	62                   	(bad)  
 53c:	6c                   	ins    BYTE PTR es:[rdi],dx
 53d:	65 00 50 79          	add    BYTE PTR gs:[rax+0x79],dl
 541:	5f                   	pop    rdi
 542:	42 79 74             	rex.X jns 5b9 <Py_BytesMain@plt-0xa77>
 545:	65 73 4d             	gs jae 595 <Py_BytesMain@plt-0xa9b>
 548:	61                   	(bad)  
 549:	69 6e 00 6c 69 62 70 	imul   ebp,DWORD PTR [rsi+0x0],0x7062696c
 550:	79 74                	jns    5c6 <Py_BytesMain@plt-0xa6a>
 552:	68 6f 6e 33 2e       	push   0x2e336e6f
 557:	31 31                	xor    DWORD PTR [rcx],esi
 559:	2e 73 6f             	cs jae 5cb <Py_BytesMain@plt-0xa65>
 55c:	2e 31 2e             	xor    DWORD PTR cs:[rsi],ebp
 55f:	30 00                	xor    BYTE PTR [rax],al
 561:	6c                   	ins    BYTE PTR es:[rdi],dx
 562:	69 62 63 2e 73 6f 2e 	imul   esp,DWORD PTR [rdx+0x63],0x2e6f732e
 569:	36 00 5f 5f          	add    BYTE PTR ss:[rdi+0x5f],bl
 56d:	6c                   	ins    BYTE PTR es:[rdi],dx
 56e:	69 62 63 5f 63 73 75 	imul   esp,DWORD PTR [rdx+0x63],0x7573635f
 575:	5f                   	pop    rdi
 576:	66 69 6e 69 00 5f    	imul   bp,WORD PTR [rsi+0x69],0x5f00
 57c:	65 64 61             	gs fs (bad) 
 57f:	74 61                	je     5e2 <Py_BytesMain@plt-0xa4e>
 581:	00 5f 5f             	add    BYTE PTR [rdi+0x5f],bl
 584:	64 61                	fs (bad) 
 586:	74 61                	je     5e9 <Py_BytesMain@plt-0xa47>
 588:	5f                   	pop    rdi
 589:	73 74                	jae    5ff <Py_BytesMain@plt-0xa31>
 58b:	61                   	(bad)  
 58c:	72 74                	jb     602 <Py_BytesMain@plt-0xa2e>
 58e:	00 5f 49             	add    BYTE PTR [rdi+0x49],bl
 591:	4f 5f                	rex.WRXB pop r15
 593:	73 74                	jae    609 <Py_BytesMain@plt-0xa27>
 595:	64 69 6e 5f 75 73 65 	imul   ebp,DWORD PTR fs:[rsi+0x5f],0x64657375
 59c:	64 
 59d:	00 5f 5f             	add    BYTE PTR [rdi+0x5f],bl
 5a0:	6c                   	ins    BYTE PTR es:[rdi],dx
 5a1:	69 62 63 5f 63 73 75 	imul   esp,DWORD PTR [rdx+0x63],0x7573635f
 5a8:	5f                   	pop    rdi
 5a9:	69 6e 69 74 00 5f 65 	imul   ebp,DWORD PTR [rsi+0x69],0x655f0074
 5b0:	6e                   	outs   dx,BYTE PTR ds:[rsi]
 5b1:	64 00 5f 5f          	add    BYTE PTR fs:[rdi+0x5f],bl
 5b5:	62 73                	(bad)  
 5b7:	73 5f                	jae    618 <Py_BytesMain@plt-0xa18>
 5b9:	73 74                	jae    62f <Py_BytesMain@plt-0xa01>
 5bb:	61                   	(bad)  
 5bc:	72 74                	jb     632 <Py_BytesMain@plt-0x9fe>
 5be:	00 47 4c             	add    BYTE PTR [rdi+0x4c],al
 5c1:	49                   	rex.WB
 5c2:	42                   	rex.X
 5c3:	43 5f                	rex.XB pop r15
 5c5:	32 2e                	xor    ch,BYTE PTR [rsi]
 5c7:	32 2e                	xor    ch,BYTE PTR [rsi]
 5c9:	35                   	.byte 0x35
	...

Disassembly of section .gnu.version:

00000000000005cc <.gnu.version>:
 5cc:	00 00                	add    BYTE PTR [rax],al
 5ce:	00 00                	add    BYTE PTR [rax],al
 5d0:	00 00                	add    BYTE PTR [rax],al
 5d2:	02 00                	add    al,BYTE PTR [rax]
 5d4:	00 00                	add    BYTE PTR [rax],al
 5d6:	00 00                	add    BYTE PTR [rax],al
 5d8:	01 00                	add    DWORD PTR [rax],eax
 5da:	01 00                	add    DWORD PTR [rax],eax
 5dc:	01 00                	add    DWORD PTR [rax],eax
 5de:	02 00                	add    al,BYTE PTR [rax]
 5e0:	01 00                	add    DWORD PTR [rax],eax
 5e2:	01 00                	add    DWORD PTR [rax],eax
 5e4:	01 00                	add    DWORD PTR [rax],eax
 5e6:	01 00                	add    DWORD PTR [rax],eax
 5e8:	01 00                	add    DWORD PTR [rax],eax
 5ea:	01 00                	add    DWORD PTR [rax],eax

Disassembly of section .gnu.version_r:

00000000000005f0 <.gnu.version_r>:
 5f0:	01 00                	add    DWORD PTR [rax],eax
 5f2:	01 00                	add    DWORD PTR [rax],eax
 5f4:	89 00                	mov    DWORD PTR [rax],eax
 5f6:	00 00                	add    BYTE PTR [rax],al
 5f8:	10 00                	adc    BYTE PTR [rax],al
 5fa:	00 00                	add    BYTE PTR [rax],al
 5fc:	00 00                	add    BYTE PTR [rax],al
 5fe:	00 00                	add    BYTE PTR [rax],al
 600:	75 1a                	jne    61c <Py_BytesMain@plt-0xa14>
 602:	69 09 00 00 02 00    	imul   ecx,DWORD PTR [rcx],0x20000
 608:	e7 00                	out    0x0,eax
 60a:	00 00                	add    BYTE PTR [rax],al
 60c:	00 00                	add    BYTE PTR [rax],al
	...

Disassembly of section .rela.dyn:

0000000000000610 <.rela.dyn>:
 610:	d8 3d 00 00 00 00    	fdivr  DWORD PTR [rip+0x0]        # 616 <Py_BytesMain@plt-0xa1a>
 616:	00 00                	add    BYTE PTR [rax],al
 618:	08 00                	or     BYTE PTR [rax],al
 61a:	00 00                	add    BYTE PTR [rax],al
 61c:	00 00                	add    BYTE PTR [rax],al
 61e:	00 00                	add    BYTE PTR [rax],al
 620:	30 11                	xor    BYTE PTR [rcx],dl
 622:	00 00                	add    BYTE PTR [rax],al
 624:	00 00                	add    BYTE PTR [rax],al
 626:	00 00                	add    BYTE PTR [rax],al
 628:	e0 3d                	loopne 667 <Py_BytesMain@plt-0x9c9>
 62a:	00 00                	add    BYTE PTR [rax],al
 62c:	00 00                	add    BYTE PTR [rax],al
 62e:	00 00                	add    BYTE PTR [rax],al
 630:	08 00                	or     BYTE PTR [rax],al
 632:	00 00                	add    BYTE PTR [rax],al
 634:	00 00                	add    BYTE PTR [rax],al
 636:	00 00                	add    BYTE PTR [rax],al
 638:	f0 10 00             	lock adc BYTE PTR [rax],al
 63b:	00 00                	add    BYTE PTR [rax],al
 63d:	00 00                	add    BYTE PTR [rax],al
 63f:	00 28                	add    BYTE PTR [rax],ch
 641:	40 00 00             	add    BYTE PTR [rax],al
 644:	00 00                	add    BYTE PTR [rax],al
 646:	00 00                	add    BYTE PTR [rax],al
 648:	08 00                	or     BYTE PTR [rax],al
 64a:	00 00                	add    BYTE PTR [rax],al
 64c:	00 00                	add    BYTE PTR [rax],al
 64e:	00 00                	add    BYTE PTR [rax],al
 650:	28 40 00             	sub    BYTE PTR [rax+0x0],al
 653:	00 00                	add    BYTE PTR [rax],al
 655:	00 00                	add    BYTE PTR [rax],al
 657:	00 d8                	add    al,bl
 659:	3f                   	(bad)  
 65a:	00 00                	add    BYTE PTR [rax],al
 65c:	00 00                	add    BYTE PTR [rax],al
 65e:	00 00                	add    BYTE PTR [rax],al
 660:	06                   	(bad)  
 661:	00 00                	add    BYTE PTR [rax],al
 663:	00 02                	add    BYTE PTR [rdx],al
	...
 66d:	00 00                	add    BYTE PTR [rax],al
 66f:	00 e0                	add    al,ah
 671:	3f                   	(bad)  
 672:	00 00                	add    BYTE PTR [rax],al
 674:	00 00                	add    BYTE PTR [rax],al
 676:	00 00                	add    BYTE PTR [rax],al
 678:	06                   	(bad)  
 679:	00 00                	add    BYTE PTR [rax],al
 67b:	00 03                	add    BYTE PTR [rbx],al
	...
 685:	00 00                	add    BYTE PTR [rax],al
 687:	00 e8                	add    al,ch
 689:	3f                   	(bad)  
 68a:	00 00                	add    BYTE PTR [rax],al
 68c:	00 00                	add    BYTE PTR [rax],al
 68e:	00 00                	add    BYTE PTR [rax],al
 690:	06                   	(bad)  
 691:	00 00                	add    BYTE PTR [rax],al
 693:	00 04 00             	add    BYTE PTR [rax+rax*1],al
	...
 69e:	00 00                	add    BYTE PTR [rax],al
 6a0:	f0 3f                	lock (bad) 
 6a2:	00 00                	add    BYTE PTR [rax],al
 6a4:	00 00                	add    BYTE PTR [rax],al
 6a6:	00 00                	add    BYTE PTR [rax],al
 6a8:	06                   	(bad)  
 6a9:	00 00                	add    BYTE PTR [rax],al
 6ab:	00 05 00 00 00 00    	add    BYTE PTR [rip+0x0],al        # 6b1 <Py_BytesMain@plt-0x97f>
 6b1:	00 00                	add    BYTE PTR [rax],al
 6b3:	00 00                	add    BYTE PTR [rax],al
 6b5:	00 00                	add    BYTE PTR [rax],al
 6b7:	00 f8                	add    al,bh
 6b9:	3f                   	(bad)  
 6ba:	00 00                	add    BYTE PTR [rax],al
 6bc:	00 00                	add    BYTE PTR [rax],al
 6be:	00 00                	add    BYTE PTR [rax],al
 6c0:	06                   	(bad)  
 6c1:	00 00                	add    BYTE PTR [rax],al
 6c3:	00 09                	add    BYTE PTR [rcx],cl
	...

Disassembly of section .rela.plt:

00000000000006d0 <.rela.plt>:
 6d0:	18 40 00             	sbb    BYTE PTR [rax+0x0],al
 6d3:	00 00                	add    BYTE PTR [rax],al
 6d5:	00 00                	add    BYTE PTR [rax],al
 6d7:	00 07                	add    BYTE PTR [rdi],al
 6d9:	00 00                	add    BYTE PTR [rax],al
 6db:	00 01                	add    BYTE PTR [rcx],al
	...

Disassembly of section .init:

0000000000001000 <.init>:
    1000:	48 83 ec 08          	sub    rsp,0x8
    1004:	48 8b 05 dd 2f 00 00 	mov    rax,QWORD PTR [rip+0x2fdd]        # 3fe8 <__gmon_start__>
    100b:	48 85 c0             	test   rax,rax
    100e:	74 02                	je     1012 <Py_BytesMain@plt-0x1e>
    1010:	ff d0                	call   rax
    1012:	48 83 c4 08          	add    rsp,0x8
    1016:	c3                   	ret    

Disassembly of section .plt:

0000000000001020 <Py_BytesMain@plt-0x10>:
    1020:	ff 35 e2 2f 00 00    	push   QWORD PTR [rip+0x2fe2]        # 4008 <_IO_stdin_used@@Base+0x2008>
    1026:	ff 25 e4 2f 00 00    	jmp    QWORD PTR [rip+0x2fe4]        # 4010 <_IO_stdin_used@@Base+0x2010>
    102c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]

0000000000001030 <Py_BytesMain@plt>:
    1030:	ff 25 e2 2f 00 00    	jmp    QWORD PTR [rip+0x2fe2]        # 4018 <Py_BytesMain>
    1036:	68 00 00 00 00       	push   0x0
    103b:	e9 e0 ff ff ff       	jmp    1020 <Py_BytesMain@plt-0x10>

Disassembly of section .plt.got:

0000000000001040 <__cxa_finalize@plt>:
    1040:	ff 25 b2 2f 00 00    	jmp    QWORD PTR [rip+0x2fb2]        # 3ff8 <__cxa_finalize@GLIBC_2.2.5>
    1046:	66 90                	xchg   ax,ax

Disassembly of section .text:

0000000000001050 <_start@@Base>:
    1050:	31 ed                	xor    ebp,ebp
    1052:	49 89 d1             	mov    r9,rdx
    1055:	5e                   	pop    rsi
    1056:	48 89 e2             	mov    rdx,rsp
    1059:	48 83 e4 f0          	and    rsp,0xfffffffffffffff0
    105d:	50                   	push   rax
    105e:	54                   	push   rsp
    105f:	4c 8d 05 4a 01 00 00 	lea    r8,[rip+0x14a]        # 11b0 <__libc_csu_fini@@Base>
    1066:	48 8d 0d e3 00 00 00 	lea    rcx,[rip+0xe3]        # 1150 <__libc_csu_init@@Base>
    106d:	48 8d 3d cc 00 00 00 	lea    rdi,[rip+0xcc]        # 1140 <_start@@Base+0xf0>
    1074:	ff 15 66 2f 00 00    	call   QWORD PTR [rip+0x2f66]        # 3fe0 <__libc_start_main@GLIBC_2.2.5>
    107a:	f4                   	hlt    
    107b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]
    1080:	48 8d 3d a9 2f 00 00 	lea    rdi,[rip+0x2fa9]        # 4030 <__bss_start@@Base>
    1087:	48 8d 05 a2 2f 00 00 	lea    rax,[rip+0x2fa2]        # 4030 <__bss_start@@Base>
    108e:	48 39 f8             	cmp    rax,rdi
    1091:	74 15                	je     10a8 <_start@@Base+0x58>
    1093:	48 8b 05 3e 2f 00 00 	mov    rax,QWORD PTR [rip+0x2f3e]        # 3fd8 <_ITM_deregisterTMCloneTable>
    109a:	48 85 c0             	test   rax,rax
    109d:	74 09                	je     10a8 <_start@@Base+0x58>
    109f:	ff e0                	jmp    rax
    10a1:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    10a8:	c3                   	ret    
    10a9:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    10b0:	48 8d 3d 79 2f 00 00 	lea    rdi,[rip+0x2f79]        # 4030 <__bss_start@@Base>
    10b7:	48 8d 35 72 2f 00 00 	lea    rsi,[rip+0x2f72]        # 4030 <__bss_start@@Base>
    10be:	48 29 fe             	sub    rsi,rdi
    10c1:	48 89 f0             	mov    rax,rsi
    10c4:	48 c1 ee 3f          	shr    rsi,0x3f
    10c8:	48 c1 f8 03          	sar    rax,0x3
    10cc:	48 01 c6             	add    rsi,rax
    10cf:	48 d1 fe             	sar    rsi,1
    10d2:	74 14                	je     10e8 <_start@@Base+0x98>
    10d4:	48 8b 05 15 2f 00 00 	mov    rax,QWORD PTR [rip+0x2f15]        # 3ff0 <_ITM_registerTMCloneTable>
    10db:	48 85 c0             	test   rax,rax
    10de:	74 08                	je     10e8 <_start@@Base+0x98>
    10e0:	ff e0                	jmp    rax
    10e2:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]
    10e8:	c3                   	ret    
    10e9:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    10f0:	80 3d 39 2f 00 00 00 	cmp    BYTE PTR [rip+0x2f39],0x0        # 4030 <__bss_start@@Base>
    10f7:	75 2f                	jne    1128 <_start@@Base+0xd8>
    10f9:	55                   	push   rbp
    10fa:	48 83 3d f6 2e 00 00 	cmp    QWORD PTR [rip+0x2ef6],0x0        # 3ff8 <__cxa_finalize@GLIBC_2.2.5>
    1101:	00 
    1102:	48 89 e5             	mov    rbp,rsp
    1105:	74 0c                	je     1113 <_start@@Base+0xc3>
    1107:	48 8b 3d 1a 2f 00 00 	mov    rdi,QWORD PTR [rip+0x2f1a]        # 4028 <__data_start@@Base+0x8>
    110e:	e8 2d ff ff ff       	call   1040 <__cxa_finalize@plt>
    1113:	e8 68 ff ff ff       	call   1080 <_start@@Base+0x30>
    1118:	c6 05 11 2f 00 00 01 	mov    BYTE PTR [rip+0x2f11],0x1        # 4030 <__bss_start@@Base>
    111f:	5d                   	pop    rbp
    1120:	c3                   	ret    
    1121:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    1128:	c3                   	ret    
    1129:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    1130:	e9 7b ff ff ff       	jmp    10b0 <_start@@Base+0x60>
    1135:	66 2e 0f 1f 84 00 00 	nop    WORD PTR cs:[rax+rax*1+0x0]
    113c:	00 00 00 
    113f:	90                   	nop
    1140:	e9 eb fe ff ff       	jmp    1030 <Py_BytesMain@plt>
    1145:	66 2e 0f 1f 84 00 00 	nop    WORD PTR cs:[rax+rax*1+0x0]
    114c:	00 00 00 
    114f:	90                   	nop

0000000000001150 <__libc_csu_init@@Base>:
    1150:	41 57                	push   r15
    1152:	4c 8d 3d 7f 2c 00 00 	lea    r15,[rip+0x2c7f]        # 3dd8 <_IO_stdin_used@@Base+0x1dd8>
    1159:	41 56                	push   r14
    115b:	49 89 d6             	mov    r14,rdx
    115e:	41 55                	push   r13
    1160:	49 89 f5             	mov    r13,rsi
    1163:	41 54                	push   r12
    1165:	41 89 fc             	mov    r12d,edi
    1168:	55                   	push   rbp
    1169:	48 8d 2d 70 2c 00 00 	lea    rbp,[rip+0x2c70]        # 3de0 <_IO_stdin_used@@Base+0x1de0>
    1170:	53                   	push   rbx
    1171:	4c 29 fd             	sub    rbp,r15
    1174:	48 83 ec 08          	sub    rsp,0x8
    1178:	e8 83 fe ff ff       	call   1000 <Py_BytesMain@plt-0x30>
    117d:	48 c1 fd 03          	sar    rbp,0x3
    1181:	74 1b                	je     119e <__libc_csu_init@@Base+0x4e>
    1183:	31 db                	xor    ebx,ebx
    1185:	0f 1f 00             	nop    DWORD PTR [rax]
    1188:	4c 89 f2             	mov    rdx,r14
    118b:	4c 89 ee             	mov    rsi,r13
    118e:	44 89 e7             	mov    edi,r12d
    1191:	41 ff 14 df          	call   QWORD PTR [r15+rbx*8]
    1195:	48 83 c3 01          	add    rbx,0x1
    1199:	48 39 dd             	cmp    rbp,rbx
    119c:	75 ea                	jne    1188 <__libc_csu_init@@Base+0x38>
    119e:	48 83 c4 08          	add    rsp,0x8
    11a2:	5b                   	pop    rbx
    11a3:	5d                   	pop    rbp
    11a4:	41 5c                	pop    r12
    11a6:	41 5d                	pop    r13
    11a8:	41 5e                	pop    r14
    11aa:	41 5f                	pop    r15
    11ac:	c3                   	ret    
    11ad:	0f 1f 00             	nop    DWORD PTR [rax]

00000000000011b0 <__libc_csu_fini@@Base>:
    11b0:	c3                   	ret    

Disassembly of section .fini:

00000000000011b4 <.fini>:
    11b4:	48 83 ec 08          	sub    rsp,0x8
    11b8:	48 83 c4 08          	add    rsp,0x8
    11bc:	c3                   	ret    

Disassembly of section .rodata:

0000000000002000 <_IO_stdin_used@@Base>:
    2000:	01 00                	add    DWORD PTR [rax],eax
    2002:	02 00                	add    al,BYTE PTR [rax]

Disassembly of section .eh_frame_hdr:

0000000000002004 <.eh_frame_hdr>:
    2004:	01 1b                	add    DWORD PTR [rbx],ebx
    2006:	03 3b                	add    edi,DWORD PTR [rbx]
    2008:	38 00                	cmp    BYTE PTR [rax],al
    200a:	00 00                	add    BYTE PTR [rax],al
    200c:	06                   	(bad)  
    200d:	00 00                	add    BYTE PTR [rax],al
    200f:	00 1c f0             	add    BYTE PTR [rax+rsi*8],bl
    2012:	ff                   	(bad)  
    2013:	ff 84 00 00 00 3c f0 	inc    DWORD PTR [rax+rax*1-0xfc40000]
    201a:	ff                   	(bad)  
    201b:	ff ac 00 00 00 4c f0 	jmp    FWORD PTR [rax+rax*1-0xfb40000]
    2022:	ff                   	(bad)  
    2023:	ff 54 00 00          	call   QWORD PTR [rax+rax*1+0x0]
    2027:	00 3c f1             	add    BYTE PTR [rcx+rsi*8],bh
    202a:	ff                   	(bad)  
    202b:	ff c4                	inc    esp
    202d:	00 00                	add    BYTE PTR [rax],al
    202f:	00 4c f1 ff          	add    BYTE PTR [rcx+rsi*8-0x1],cl
    2033:	ff                   	(bad)  
    2034:	dc 00                	fadd   QWORD PTR [rax]
    2036:	00 00                	add    BYTE PTR [rax],al
    2038:	ac                   	lods   al,BYTE PTR ds:[rsi]
    2039:	f1                   	icebp  
    203a:	ff                   	(bad)  
    203b:	ff 24 01             	jmp    QWORD PTR [rcx+rax*1]
	...

Disassembly of section .eh_frame:

0000000000002040 <.eh_frame>:
    2040:	14 00                	adc    al,0x0
    2042:	00 00                	add    BYTE PTR [rax],al
    2044:	00 00                	add    BYTE PTR [rax],al
    2046:	00 00                	add    BYTE PTR [rax],al
    2048:	01 7a 52             	add    DWORD PTR [rdx+0x52],edi
    204b:	00 01                	add    BYTE PTR [rcx],al
    204d:	78 10                	js     205f <_IO_stdin_used@@Base+0x5f>
    204f:	01 1b                	add    DWORD PTR [rbx],ebx
    2051:	0c 07                	or     al,0x7
    2053:	08 90 01 07 10 14    	or     BYTE PTR [rax+0x14100701],dl
    2059:	00 00                	add    BYTE PTR [rax],al
    205b:	00 1c 00             	add    BYTE PTR [rax+rax*1],bl
    205e:	00 00                	add    BYTE PTR [rax],al
    2060:	f0 ef                	lock out dx,eax
    2062:	ff                   	(bad)  
    2063:	ff 2b                	jmp    FWORD PTR [rbx]
	...
    206d:	00 00                	add    BYTE PTR [rax],al
    206f:	00 14 00             	add    BYTE PTR [rax+rax*1],dl
    2072:	00 00                	add    BYTE PTR [rax],al
    2074:	00 00                	add    BYTE PTR [rax],al
    2076:	00 00                	add    BYTE PTR [rax],al
    2078:	01 7a 52             	add    DWORD PTR [rdx+0x52],edi
    207b:	00 01                	add    BYTE PTR [rcx],al
    207d:	78 10                	js     208f <_IO_stdin_used@@Base+0x8f>
    207f:	01 1b                	add    DWORD PTR [rbx],ebx
    2081:	0c 07                	or     al,0x7
    2083:	08 90 01 00 00 24    	or     BYTE PTR [rax+0x24000001],dl
    2089:	00 00                	add    BYTE PTR [rax],al
    208b:	00 1c 00             	add    BYTE PTR [rax+rax*1],bl
    208e:	00 00                	add    BYTE PTR [rax],al
    2090:	90                   	nop
    2091:	ef                   	out    dx,eax
    2092:	ff                   	(bad)  
    2093:	ff 20                	jmp    QWORD PTR [rax]
    2095:	00 00                	add    BYTE PTR [rax],al
    2097:	00 00                	add    BYTE PTR [rax],al
    2099:	0e                   	(bad)  
    209a:	10 46 0e             	adc    BYTE PTR [rsi+0xe],al
    209d:	18 4a 0f             	sbb    BYTE PTR [rdx+0xf],cl
    20a0:	0b 77 08             	or     esi,DWORD PTR [rdi+0x8]
    20a3:	80 00 3f             	add    BYTE PTR [rax],0x3f
    20a6:	1a 3b                	sbb    bh,BYTE PTR [rbx]
    20a8:	2a 33                	sub    dh,BYTE PTR [rbx]
    20aa:	24 22                	and    al,0x22
    20ac:	00 00                	add    BYTE PTR [rax],al
    20ae:	00 00                	add    BYTE PTR [rax],al
    20b0:	14 00                	adc    al,0x0
    20b2:	00 00                	add    BYTE PTR [rax],al
    20b4:	44 00 00             	add    BYTE PTR [rax],r8b
    20b7:	00 88 ef ff ff 08    	add    BYTE PTR [rax+0x8ffffef],cl
	...
    20c5:	00 00                	add    BYTE PTR [rax],al
    20c7:	00 14 00             	add    BYTE PTR [rax+rax*1],dl
    20ca:	00 00                	add    BYTE PTR [rax],al
    20cc:	5c                   	pop    rsp
    20cd:	00 00                	add    BYTE PTR [rax],al
    20cf:	00 70 f0             	add    BYTE PTR [rax-0x10],dh
    20d2:	ff                   	(bad)  
    20d3:	ff 05 00 00 00 00    	inc    DWORD PTR [rip+0x0]        # 20d9 <_IO_stdin_used@@Base+0xd9>
    20d9:	00 00                	add    BYTE PTR [rax],al
    20db:	00 00                	add    BYTE PTR [rax],al
    20dd:	00 00                	add    BYTE PTR [rax],al
    20df:	00 44 00 00          	add    BYTE PTR [rax+rax*1+0x0],al
    20e3:	00 74 00 00          	add    BYTE PTR [rax+rax*1+0x0],dh
    20e7:	00 68 f0             	add    BYTE PTR [rax-0x10],ch
    20ea:	ff                   	(bad)  
    20eb:	ff 5d 00             	call   FWORD PTR [rbp+0x0]
    20ee:	00 00                	add    BYTE PTR [rax],al
    20f0:	00 42 0e             	add    BYTE PTR [rdx+0xe],al
    20f3:	10 8f 02 49 0e 18    	adc    BYTE PTR [rdi+0x180e4902],cl
    20f9:	8e 03                	mov    es,WORD PTR [rbx]
    20fb:	45 0e                	rex.RB (bad) 
    20fd:	20 8d 04 45 0e 28    	and    BYTE PTR [rbp+0x280e4504],cl
    2103:	8c 05 44 0e 30 86    	mov    WORD PTR [rip+0xffffffff86300e44],es        # ffffffff86302f4d <_end@@Base+0xffffffff862fef15>
    2109:	06                   	(bad)  
    210a:	48 0e                	rex.W (bad) 
    210c:	38 83 07 47 0e 40    	cmp    BYTE PTR [rbx+0x400e4707],al
    2112:	6a 0e                	push   0xe
    2114:	38 41 0e             	cmp    BYTE PTR [rcx+0xe],al
    2117:	30 41 0e             	xor    BYTE PTR [rcx+0xe],al
    211a:	28 42 0e             	sub    BYTE PTR [rdx+0xe],al
    211d:	20 42 0e             	and    BYTE PTR [rdx+0xe],al
    2120:	18 42 0e             	sbb    BYTE PTR [rdx+0xe],al
    2123:	10 42 0e             	adc    BYTE PTR [rdx+0xe],al
    2126:	08 00                	or     BYTE PTR [rax],al
    2128:	10 00                	adc    BYTE PTR [rax],al
    212a:	00 00                	add    BYTE PTR [rax],al
    212c:	bc 00 00 00 80       	mov    esp,0x80000000
    2131:	f0 ff                	lock (bad) 
    2133:	ff 01                	inc    DWORD PTR [rcx]
	...

Disassembly of section .init_array:

0000000000003dd8 <.init_array>:
    3dd8:	30 11                	xor    BYTE PTR [rcx],dl
    3dda:	00 00                	add    BYTE PTR [rax],al
    3ddc:	00 00                	add    BYTE PTR [rax],al
	...

Disassembly of section .fini_array:

0000000000003de0 <.fini_array>:
    3de0:	f0 10 00             	lock adc BYTE PTR [rax],al
    3de3:	00 00                	add    BYTE PTR [rax],al
    3de5:	00 00                	add    BYTE PTR [rax],al
	...

Disassembly of section .dynamic:

0000000000003de8 <.dynamic>:
    3de8:	01 00                	add    DWORD PTR [rax],eax
    3dea:	00 00                	add    BYTE PTR [rax],al
    3dec:	00 00                	add    BYTE PTR [rax],al
    3dee:	00 00                	add    BYTE PTR [rax],al
    3df0:	74 00                	je     3df2 <_IO_stdin_used@@Base+0x1df2>
    3df2:	00 00                	add    BYTE PTR [rax],al
    3df4:	00 00                	add    BYTE PTR [rax],al
    3df6:	00 00                	add    BYTE PTR [rax],al
    3df8:	01 00                	add    DWORD PTR [rax],eax
    3dfa:	00 00                	add    BYTE PTR [rax],al
    3dfc:	00 00                	add    BYTE PTR [rax],al
    3dfe:	00 00                	add    BYTE PTR [rax],al
    3e00:	89 00                	mov    DWORD PTR [rax],eax
    3e02:	00 00                	add    BYTE PTR [rax],al
    3e04:	00 00                	add    BYTE PTR [rax],al
    3e06:	00 00                	add    BYTE PTR [rax],al
    3e08:	0c 00                	or     al,0x0
    3e0a:	00 00                	add    BYTE PTR [rax],al
    3e0c:	00 00                	add    BYTE PTR [rax],al
    3e0e:	00 00                	add    BYTE PTR [rax],al
    3e10:	00 10                	add    BYTE PTR [rax],dl
    3e12:	00 00                	add    BYTE PTR [rax],al
    3e14:	00 00                	add    BYTE PTR [rax],al
    3e16:	00 00                	add    BYTE PTR [rax],al
    3e18:	0d 00 00 00 00       	or     eax,0x0
    3e1d:	00 00                	add    BYTE PTR [rax],al
    3e1f:	00 b4 11 00 00 00 00 	add    BYTE PTR [rcx+rdx*1+0x0],dh
    3e26:	00 00                	add    BYTE PTR [rax],al
    3e28:	19 00                	sbb    DWORD PTR [rax],eax
    3e2a:	00 00                	add    BYTE PTR [rax],al
    3e2c:	00 00                	add    BYTE PTR [rax],al
    3e2e:	00 00                	add    BYTE PTR [rax],al
    3e30:	d8 3d 00 00 00 00    	fdivr  DWORD PTR [rip+0x0]        # 3e36 <_IO_stdin_used@@Base+0x1e36>
    3e36:	00 00                	add    BYTE PTR [rax],al
    3e38:	1b 00                	sbb    eax,DWORD PTR [rax]
    3e3a:	00 00                	add    BYTE PTR [rax],al
    3e3c:	00 00                	add    BYTE PTR [rax],al
    3e3e:	00 00                	add    BYTE PTR [rax],al
    3e40:	08 00                	or     BYTE PTR [rax],al
    3e42:	00 00                	add    BYTE PTR [rax],al
    3e44:	00 00                	add    BYTE PTR [rax],al
    3e46:	00 00                	add    BYTE PTR [rax],al
    3e48:	1a 00                	sbb    al,BYTE PTR [rax]
    3e4a:	00 00                	add    BYTE PTR [rax],al
    3e4c:	00 00                	add    BYTE PTR [rax],al
    3e4e:	00 00                	add    BYTE PTR [rax],al
    3e50:	e0 3d                	loopne 3e8f <_IO_stdin_used@@Base+0x1e8f>
    3e52:	00 00                	add    BYTE PTR [rax],al
    3e54:	00 00                	add    BYTE PTR [rax],al
    3e56:	00 00                	add    BYTE PTR [rax],al
    3e58:	1c 00                	sbb    al,0x0
    3e5a:	00 00                	add    BYTE PTR [rax],al
    3e5c:	00 00                	add    BYTE PTR [rax],al
    3e5e:	00 00                	add    BYTE PTR [rax],al
    3e60:	08 00                	or     BYTE PTR [rax],al
    3e62:	00 00                	add    BYTE PTR [rax],al
    3e64:	00 00                	add    BYTE PTR [rax],al
    3e66:	00 00                	add    BYTE PTR [rax],al
    3e68:	f5                   	cmc    
    3e69:	fe                   	(bad)  
    3e6a:	ff 6f 00             	jmp    FWORD PTR [rdi+0x0]
    3e6d:	00 00                	add    BYTE PTR [rax],al
    3e6f:	00 08                	add    BYTE PTR [rax],cl
    3e71:	03 00                	add    eax,DWORD PTR [rax]
    3e73:	00 00                	add    BYTE PTR [rax],al
    3e75:	00 00                	add    BYTE PTR [rax],al
    3e77:	00 05 00 00 00 00    	add    BYTE PTR [rip+0x0],al        # 3e7d <_IO_stdin_used@@Base+0x1e7d>
    3e7d:	00 00                	add    BYTE PTR [rax],al
    3e7f:	00 d8                	add    al,bl
    3e81:	04 00                	add    al,0x0
    3e83:	00 00                	add    BYTE PTR [rax],al
    3e85:	00 00                	add    BYTE PTR [rax],al
    3e87:	00 06                	add    BYTE PTR [rsi],al
    3e89:	00 00                	add    BYTE PTR [rax],al
    3e8b:	00 00                	add    BYTE PTR [rax],al
    3e8d:	00 00                	add    BYTE PTR [rax],al
    3e8f:	00 58 03             	add    BYTE PTR [rax+0x3],bl
    3e92:	00 00                	add    BYTE PTR [rax],al
    3e94:	00 00                	add    BYTE PTR [rax],al
    3e96:	00 00                	add    BYTE PTR [rax],al
    3e98:	0a 00                	or     al,BYTE PTR [rax]
    3e9a:	00 00                	add    BYTE PTR [rax],al
    3e9c:	00 00                	add    BYTE PTR [rax],al
    3e9e:	00 00                	add    BYTE PTR [rax],al
    3ea0:	f3 00 00             	repz add BYTE PTR [rax],al
    3ea3:	00 00                	add    BYTE PTR [rax],al
    3ea5:	00 00                	add    BYTE PTR [rax],al
    3ea7:	00 0b                	add    BYTE PTR [rbx],cl
    3ea9:	00 00                	add    BYTE PTR [rax],al
    3eab:	00 00                	add    BYTE PTR [rax],al
    3ead:	00 00                	add    BYTE PTR [rax],al
    3eaf:	00 18                	add    BYTE PTR [rax],bl
    3eb1:	00 00                	add    BYTE PTR [rax],al
    3eb3:	00 00                	add    BYTE PTR [rax],al
    3eb5:	00 00                	add    BYTE PTR [rax],al
    3eb7:	00 15 00 00 00 00    	add    BYTE PTR [rip+0x0],dl        # 3ebd <_IO_stdin_used@@Base+0x1ebd>
	...
    3ec5:	00 00                	add    BYTE PTR [rax],al
    3ec7:	00 03                	add    BYTE PTR [rbx],al
	...
    3ed1:	40 00 00             	add    BYTE PTR [rax],al
    3ed4:	00 00                	add    BYTE PTR [rax],al
    3ed6:	00 00                	add    BYTE PTR [rax],al
    3ed8:	02 00                	add    al,BYTE PTR [rax]
    3eda:	00 00                	add    BYTE PTR [rax],al
    3edc:	00 00                	add    BYTE PTR [rax],al
    3ede:	00 00                	add    BYTE PTR [rax],al
    3ee0:	18 00                	sbb    BYTE PTR [rax],al
    3ee2:	00 00                	add    BYTE PTR [rax],al
    3ee4:	00 00                	add    BYTE PTR [rax],al
    3ee6:	00 00                	add    BYTE PTR [rax],al
    3ee8:	14 00                	adc    al,0x0
    3eea:	00 00                	add    BYTE PTR [rax],al
    3eec:	00 00                	add    BYTE PTR [rax],al
    3eee:	00 00                	add    BYTE PTR [rax],al
    3ef0:	07                   	(bad)  
    3ef1:	00 00                	add    BYTE PTR [rax],al
    3ef3:	00 00                	add    BYTE PTR [rax],al
    3ef5:	00 00                	add    BYTE PTR [rax],al
    3ef7:	00 17                	add    BYTE PTR [rdi],dl
    3ef9:	00 00                	add    BYTE PTR [rax],al
    3efb:	00 00                	add    BYTE PTR [rax],al
    3efd:	00 00                	add    BYTE PTR [rax],al
    3eff:	00 d0                	add    al,dl
    3f01:	06                   	(bad)  
    3f02:	00 00                	add    BYTE PTR [rax],al
    3f04:	00 00                	add    BYTE PTR [rax],al
    3f06:	00 00                	add    BYTE PTR [rax],al
    3f08:	07                   	(bad)  
    3f09:	00 00                	add    BYTE PTR [rax],al
    3f0b:	00 00                	add    BYTE PTR [rax],al
    3f0d:	00 00                	add    BYTE PTR [rax],al
    3f0f:	00 10                	add    BYTE PTR [rax],dl
    3f11:	06                   	(bad)  
    3f12:	00 00                	add    BYTE PTR [rax],al
    3f14:	00 00                	add    BYTE PTR [rax],al
    3f16:	00 00                	add    BYTE PTR [rax],al
    3f18:	08 00                	or     BYTE PTR [rax],al
    3f1a:	00 00                	add    BYTE PTR [rax],al
    3f1c:	00 00                	add    BYTE PTR [rax],al
    3f1e:	00 00                	add    BYTE PTR [rax],al
    3f20:	c0 00 00             	rol    BYTE PTR [rax],0x0
    3f23:	00 00                	add    BYTE PTR [rax],al
    3f25:	00 00                	add    BYTE PTR [rax],al
    3f27:	00 09                	add    BYTE PTR [rcx],cl
    3f29:	00 00                	add    BYTE PTR [rax],al
    3f2b:	00 00                	add    BYTE PTR [rax],al
    3f2d:	00 00                	add    BYTE PTR [rax],al
    3f2f:	00 18                	add    BYTE PTR [rax],bl
    3f31:	00 00                	add    BYTE PTR [rax],al
    3f33:	00 00                	add    BYTE PTR [rax],al
    3f35:	00 00                	add    BYTE PTR [rax],al
    3f37:	00 fb                	add    bl,bh
    3f39:	ff                   	(bad)  
    3f3a:	ff 6f 00             	jmp    FWORD PTR [rdi+0x0]
    3f3d:	00 00                	add    BYTE PTR [rax],al
    3f3f:	00 00                	add    BYTE PTR [rax],al
    3f41:	00 00                	add    BYTE PTR [rax],al
    3f43:	08 00                	or     BYTE PTR [rax],al
    3f45:	00 00                	add    BYTE PTR [rax],al
    3f47:	00 fe                	add    dh,bh
    3f49:	ff                   	(bad)  
    3f4a:	ff 6f 00             	jmp    FWORD PTR [rdi+0x0]
    3f4d:	00 00                	add    BYTE PTR [rax],al
    3f4f:	00 f0                	add    al,dh
    3f51:	05 00 00 00 00       	add    eax,0x0
    3f56:	00 00                	add    BYTE PTR [rax],al
    3f58:	ff                   	(bad)  
    3f59:	ff                   	(bad)  
    3f5a:	ff 6f 00             	jmp    FWORD PTR [rdi+0x0]
    3f5d:	00 00                	add    BYTE PTR [rax],al
    3f5f:	00 01                	add    BYTE PTR [rcx],al
    3f61:	00 00                	add    BYTE PTR [rax],al
    3f63:	00 00                	add    BYTE PTR [rax],al
    3f65:	00 00                	add    BYTE PTR [rax],al
    3f67:	00 f0                	add    al,dh
    3f69:	ff                   	(bad)  
    3f6a:	ff 6f 00             	jmp    FWORD PTR [rdi+0x0]
    3f6d:	00 00                	add    BYTE PTR [rax],al
    3f6f:	00 cc                	add    ah,cl
    3f71:	05 00 00 00 00       	add    eax,0x0
    3f76:	00 00                	add    BYTE PTR [rax],al
    3f78:	f9                   	stc    
    3f79:	ff                   	(bad)  
    3f7a:	ff 6f 00             	jmp    FWORD PTR [rdi+0x0]
    3f7d:	00 00                	add    BYTE PTR [rax],al
    3f7f:	00 03                	add    BYTE PTR [rbx],al
	...

Disassembly of section .got:

0000000000003fd8 <.got>:
	...

Disassembly of section .got.plt:

0000000000004000 <.got.plt>:
    4000:	e8 3d 00 00 00       	call   4042 <_end@@Base+0xa>
	...
    4015:	00 00                	add    BYTE PTR [rax],al
    4017:	00 36                	add    BYTE PTR [rsi],dh
    4019:	10 00                	adc    BYTE PTR [rax],al
    401b:	00 00                	add    BYTE PTR [rax],al
    401d:	00 00                	add    BYTE PTR [rax],al
	...

Disassembly of section .data:

0000000000004020 <__data_start@@Base>:
	...
    4028:	28 40 00             	sub    BYTE PTR [rax+0x0],al
    402b:	00 00                	add    BYTE PTR [rax],al
    402d:	00 00                	add    BYTE PTR [rax],al
	...

Disassembly of section .bss:

0000000000004030 <__bss_start@@Base>:
	...

Disassembly of section .comment:

0000000000000000 <.comment>:
   0:	47                   	rex.RXB
   1:	43                   	rex.XB
   2:	43 3a 20             	rex.XB cmp spl,BYTE PTR [r8]
   5:	28 44 65 62          	sub    BYTE PTR [rbp+riz*2+0x62],al
   9:	69 61 6e 20 31 30 2e 	imul   esp,DWORD PTR [rcx+0x6e],0x2e303120
  10:	32 2e                	xor    ch,BYTE PTR [rsi]
  12:	31 2d 36 29 20 31    	xor    DWORD PTR [rip+0x31202936],ebp        # 3120294e <_end@@Base+0x311fe916>
  18:	30 2e                	xor    BYTE PTR [rsi],ch
  1a:	32 2e                	xor    ch,BYTE PTR [rsi]
  1c:	31 20                	xor    DWORD PTR [rax],esp
  1e:	32 30                	xor    dh,BYTE PTR [rax]
  20:	32 31                	xor    dh,BYTE PTR [rcx]
  22:	30 31                	xor    BYTE PTR [rcx],dh
  24:	31 30                	xor    DWORD PTR [rax],esi
	...
```
