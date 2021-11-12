Last login: Sun Oct 31 20:12:23 on ttys000
users-MBP:~ user$ 1s
-bash: 1s: command not found
users-MBP:~ user$ ls
Applications				Music
Desktop					Output5 income and bar chart.spv
Documents				Pictures
Downloads				Public
Library					Sites
Movies					scatterchart.xml
users-MBP:~ user$ cd downloads
users-MBP:downloads user$ cd Downloads
-bash: cd: Downloads: No such file or directory
users-MBP:downloads user$ cd ~
users-MBP:~ user$ cd ../desktop
-bash: cd: ../desktop: No such file or directory
users-MBP:~ user$ git --version
xcode-select: note: no developer tools were found at '/Applications/Xcode.app', requesting install. Choose an option in the dialog to download the command line developer tools.
users-MBP:~ user$ brew install git-lfs
-bash: brew: command not found
users-MBP:~ user$ brew upgrade git
-bash: brew: command not found
users-MBP:~ user$ git --version
git version 2.20.1 (Apple Git-117)
users-MBP:~ user$ brew install git-lfs
-bash: brew: command not found
users-MBP:~ user$ exit()
> 
> cd ~
-bash: syntax error near unexpected token `cd'
users-MBP:~ user$ gitclone https://github.com/bevjenkins7/Election_Analysis.git
-bash: gitclone: command not found
users-MBP:~ user$ gitcode https://github.com/bevjenkins7/Election_Analysis.git
-bash: gitcode: command not found
users-MBP:~ user$ gitclone
-bash: gitclone: command not found
users-MBP:~ user$ gitclone
-bash: gitclone: command not found
users-MBP:~ user$ gitclone
-bash: gitclone: command not found
users-MBP:~ user$ 
users-MBP:~ user$ pwd
/Users/user
users-MBP:~ user$ ls
Applications				Music
Desktop					Output5 income and bar chart.spv
Documents				Pictures
Downloads				Public
Library					Sites
Movies					scatterchart.xml
users-MBP:~ user$ gitclone gh repo clone bevjenkins7/Election_Analysis
-bash: gitclone: command not found
users-MBP:~ user$ cd
users-MBP:~ user$ cd desktop
users-MBP:desktop user$ pwd
/Users/user/desktop
users-MBP:desktop user$ cd class
-bash: cd: class: No such file or directory
users-MBP:desktop user$ git clone gh repo clone bevjenkins7/Election_Analysis
fatal: Too many arguments.

usage: git clone [<options>] [--] <repo> [<dir>]

    -v, --verbose         be more verbose
    -q, --quiet           be more quiet
    --progress            force progress reporting
    -n, --no-checkout     don't create a checkout
    --bare                create a bare repository
    --mirror              create a mirror repository (implies bare)
    -l, --local           to clone from a local repository
    --no-hardlinks        don't use local hardlinks, always copy
    -s, --shared          setup as shared repository
    --recurse-submodules[=<pathspec>]
                          initialize submodules in the clone
    -j, --jobs <n>        number of submodules cloned in parallel
    --template <template-directory>
                          directory from which templates will be used
    --reference <repo>    reference repository
    --reference-if-able <repo>
                          reference repository
    --dissociate          use --reference only while cloning
    -o, --origin <name>   use <name> instead of 'origin' to track upstream
    -b, --branch <branch>
                          checkout <branch> instead of the remote's HEAD
    -u, --upload-pack <path>
                          path to git-upload-pack on the remote
    --depth <depth>       create a shallow clone of that depth
    --shallow-since <time>
                          create a shallow clone since a specific time
    --shallow-exclude <revision>
                          deepen history of shallow clone, excluding rev
    --single-branch       clone only one branch, HEAD or --branch
    --no-tags             don't clone any tags, and make later fetches not to follow them
    --shallow-submodules  any cloned submodules will be shallow
    --separate-git-dir <gitdir>
                          separate git dir from working tree
    -c, --config <key=value>
                          set config inside the new repository
    -4, --ipv4            use IPv4 addresses only
    -6, --ipv6            use IPv6 addresses only
    --filter <args>       object filtering

users-MBP:desktop user$ Python3
Python 3.10.0 (v3.10.0:b494f5935c, Oct  4 2021, 14:59:20) [Clang 12.0.5 (clang-1205.0.22.11)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> python3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'python3' is not defined
>>> type(3)
<class 'int'>
>>> type(ballots)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ballots' is not defined
>>> type(ballots) <calss
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ballots' is not defined
>>> type(73.81)
<class 'float'>
>>> type("Hello World")
<class 'str'>
>>> COUNTINES=["Arapahoe", "Denver", "Jefferson"]
>>> counties = [Arapahoe", "Denver", "Jefferson"]
  File "<stdin>", line 1
    counties = [Arapahoe", "Denver", "Jefferson"]
                        ^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> counties = ["Arapahoe",  "Denver", "Jefferson"]
>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> counties[0]
'Arapahoe'
>>> print(counties[-1])
Jefferson
>>> counties[0:3]
['Arapahoe', 'Denver', 'Jefferson']
>>> counties[1:3]
['Denver', 'Jefferson']
>>> counties[1:]
['Denver', 'Jefferson']
>>> counties.append("El Paso")
>>> counties.append("El Paso)
  File "<stdin>", line 1
    counties.append("El Paso)
                    ^
SyntaxError: unterminated string literal (detected at line 1)
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> list.insert(index, obj)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'index' is not defined
>>> couties
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'couties' is not defined. Did you mean: 'counties'?
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties.insert(2, "El Paso)
  File "<stdin>", line 1
    counties.insert(2, "El Paso)
                       ^
SyntaxError: unterminated string literal (detected at line 1)
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties.insert(2, "El Paso")
>>> counties
['Arapahoe', 'Denver', 'El Paso', 'Jefferson', 'El Paso']
>>> counties.pop(3)
'Jefferson'
>>> counties.pop(-1)
'El Paso'
>>> counties_dict
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'counties_dict' is not defined
>>> counties_dict
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'counties_dict' is not defined
>>> cd ~
  File "<stdin>", line 1
    cd ~
       ^
SyntaxError: invalid syntax
>>> counties_dict
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'counties_dict' is not defined
>>> counties_dict
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'counties_dict' is not defined
>>> cd downloads/Mod 3 python/3-1-Student-Resources/Python_practice.py
  File "<stdin>", line 1
    cd downloads/Mod 3 python/3-1-Student-Resources/Python_practice.py
       ^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> my_dictionary = {}
>>> counties_dict = {}
>>> counties_dict
{}
>>> counties_dict = {}
>>> counties_dict["Arapahoe"] = 422829
>>> counties_dict
{'Arapahoe': 422829}
>>> counties_["Denver"] = 463353
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'counties_' is not defined. Did you mean: 'counties'?
>>> counties_dict["Denver"] = 463353
>>> counties_dict["Denver"] = 463353
>>> counties_dict
{'Arapahoe': 422829, 'Denver': 463353}
>>> counties_dict
{'Arapahoe': 422829, 'Denver': 463353}
>>> counties_dict["Jefferson"] = 432438
>>> counties_dict
{'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
>>> len(counties_dict)
3
>>> counties_dict.keys()
dict_keys(['Arapahoe', 'Denver', 'Jefferson'])
>>> counties_dict.values()
dict_values([422829, 463353, 432438])
>>> counties_dict.get("Denver")
463353
>>> voting_data.append({"county":"Arapahoe", "registered_voters":})
  File "<stdin>", line 1
    voting_data.append({"county":"Arapahoe", "registered_voters":})
                                                                ^
SyntaxError: expression expected after dictionary key and ':'
>>> voting_data = []
>>> voting_data.append({"ccounty":"Arapahoe", "registered_voters":})
  File "<stdin>", line 1
    voting_data.append({"ccounty":"Arapahoe", "registered_voters":})
                                                                 ^
SyntaxError: expression expected after dictionary key and ':'
>>> voting_data = []
>>> voting_data.append({"county":"Arapahoe", "registered_voters":
... voting_data = []
  File "<stdin>", line 2
    voting_data = []
                ^
SyntaxError: invalid syntax
>>> voting_data.append({"county":"Denver", "registered_voters":})
  File "<stdin>", line 1
    voting_data.append({"county":"Denver", "registered_voters":})
                                                              ^
SyntaxError: expression expected after dictionary key and ':'
>>> voting_data.append({"county":"Jefferson", "registered_voters":})
  File "<stdin>", line 1
    voting_data.append({"county":"Jefferson", "registered_voters":})
                                                                 ^
SyntaxError: expression expected after dictionary key and ':'
>>> voting_data
[]
>>> [{'county': "Denver', 'registered_voters':}, {'county': 'Denver', '
  File "<stdin>", line 1
    [{'county': "Denver', 'registered_voters':}, {'county': 'Denver', '
                ^
SyntaxError: unterminated string literal (detected at line 1)
>>> 
