Last login: Mon Sep 28 09:32:00 on ttys000
☁  ~  git config --list    
☁  ~  cd Desktop 
☁  Desktop [master] ⚡ git config --list
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
remote.origin.url=https://github.com/brianaguirre/AndroidGame.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.master.remote=origin
branch.master.merge=refs/heads/master
☁  Desktop [master] ⚡ git config --global user.name "Brian Aguirre"
☁  Desktop [master] ⚡ git config --global user.email "ba5bx@virginia.edu" 
☁  Desktop [master] ⚡ git config user.name
Brian Aguirre
☁  Desktop [master] ⚡ git config --global user.name "ba5bx"              
☁  Desktop [master] ⚡ git config user.name                 
ba5bx
☁  Desktop [master] ⚡ cd..
zsh: command not found: cd..
☁  Desktop [master] ⚡ cd
☁  ~  cd Documents/School/UVA/Fall2015/CS3240 
☁  CS3240  ls
08-25-2015.pages 09-01-2015.pages 09-03-2015.pages Homework
☁  CS3240  mkdir labs
☁  CS3240  cd labs 
☁  labs  mkdir lab5
☁  labs  git clone https://github.com/ba5bx/cs3240-labdemo.git 
Cloning into 'cs3240-labdemo'...
remote: Counting objects: 5, done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (5/5), done.
Checking connectivity... done.
☁  labs  ls      
cs3240-labdemo lab5
☁  labs  cd cs3240-labdemo 
☁  cs3240-labdemo [master] ⚡ ls 
LICENSE   README.md hello.py
☁  cs3240-labdemo [master] ⚡ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	hello.py

nothing added to commit but untracked files present (use "git add" to track)
☁  cs3240-labdemo [master] ⚡ git add hello.py 
☁  cs3240-labdemo [master] ⚡ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   hello.py

☁  cs3240-labdemo [master] ⚡ git commit -m "Initial commit"
[master a9cf369] Initial commit
 1 file changed, 3 insertions(+)
 create mode 100644 hello.py
☁  cs3240-labdemo [master] git push
warning: push.default is unset; its implicit value has changed in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the traditional behavior, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

Since Git 2.0, Git defaults to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

remote: Permission to ba5bx/cs3240-labdemo.git denied to brianaguirre.
fatal: unable to access 'https://github.com/ba5bx/cs3240-labdemo.git/': The requested URL returned error: 403
☁  cs3240-labdemo [master] git config -l
user.name=ba5bx
user.email=ba5bx@virginia.edu
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
remote.origin.url=https://github.com/ba5bx/cs3240-labdemo.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.master.remote=origin
branch.master.merge=refs/heads/master
☁  cs3240-labdemo [master] git push     
warning: push.default is unset; its implicit value has changed in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the traditional behavior, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

Since Git 2.0, Git defaults to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

remote: Permission to ba5bx/cs3240-labdemo.git denied to brianaguirre.
fatal: unable to access 'https://github.com/ba5bx/cs3240-labdemo.git/': The requested URL returned error: 403
☁  cs3240-labdemo [master] git config --global user.name "ba5bx"
☁  cs3240-labdemo [master] git config --global user.email ba5bx@virginia.edu
☁  cs3240-labdemo [master] git config -l                                    
user.name=ba5bx
user.email=ba5bx@virginia.edu
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
remote.origin.url=https://github.com/ba5bx/cs3240-labdemo.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.master.remote=origin
branch.master.merge=refs/heads/master
☁  cs3240-labdemo [master] git push                                         
warning: push.default is unset; its implicit value has changed in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the traditional behavior, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

Since Git 2.0, Git defaults to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

remote: Permission to ba5bx/cs3240-labdemo.git denied to brianaguirre.
fatal: unable to access 'https://github.com/ba5bx/cs3240-labdemo.git/': The requested URL returned error: 403
☁  cs3240-labdemo [master] git remote set-url origin git@github.com:ba5bx/cs3240-labdemo.git
☁  cs3240-labdemo [master] git push
warning: push.default is unset; its implicit value has changed in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the traditional behavior, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

Since Git 2.0, Git defaults to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

The authenticity of host 'github.com (192.30.252.129)' can't be established.
RSA key fingerprint is 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,192.30.252.129' (RSA) to the list of known hosts.
Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
☁  cs3240-labdemo [master] machine github.com
machine: no arguments accepted
       login <user>                                                             
☁  cs3240-labdemo [master]        login <user>
zsh: parse error near `\n'
☁  cs3240-labdemo [master]        password <password>
zsh: parse error near `\n'
☁  cs3240-labdemo [master] git
usage: git [--version] [--help] [-C <path>] [-c name=value]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p|--paginate|--no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

The most commonly used git commands are:
   add        Add file contents to the index
   bisect     Find by binary search the change that introduced a bug
   branch     List, create, or delete branches
   checkout   Checkout a branch or paths to the working tree
   clone      Clone a repository into a new directory
   commit     Record changes to the repository
   diff       Show changes between commits, commit and working tree, etc
   fetch      Download objects and refs from another repository
   grep       Print lines matching a pattern
   init       Create an empty Git repository or reinitialize an existing one
   log        Show commit logs
   merge      Join two or more development histories together
   mv         Move or rename a file, a directory, or a symlink
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects
   rebase     Forward-port local commits to the updated upstream head
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index
   show       Show various types of objects
   status     Show the working tree status
   tag        Create, list, delete or verify a tag object signed with GPG

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
☁  cs3240-labdemo [master] sudo git push
Password:
warning: push.default is unset; its implicit value has changed in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the traditional behavior, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

Since Git 2.0, Git defaults to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

The authenticity of host 'github.com (192.30.252.131)' can't be established.
RSA key fingerprint is 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,192.30.252.131' (RSA) to the list of known hosts.
Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
☁  cs3240-labdemo [master] git config --global push.default simple
☁  cs3240-labdemo [master] git push
Warning: Permanently added the RSA host key for IP address '192.30.252.131' to the list of known hosts.
Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
☁  cs3240-labdemo [master] git config --global user.name "ba5bx"     
☁  cs3240-labdemo [master] git config --global user.email "ba5bx@virginia.edu"
☁  cs3240-labdemo [master] git credential-osxkeychain
usage: git credential-osxkeychain <get|store|erase>
☁  cs3240-labdemo [master] get
zsh: command not found: get
☁  cs3240-labdemo [master] sudo mv git-credential-osxkeychain \
> "$(dirname $(which git))/git-credential-osxkeychain"
mv: rename git-credential-osxkeychain to /usr/bin/git-credential-osxkeychain: No such file or directory
☁  cs3240-labdemo [master] git credential-osxkeychain
usage: git credential-osxkeychain <get|store|erase>
☁  cs3240-labdemo [master] curl -s -O \
> https://github-media-downloads.s3.amazonaws.com/osx/git-credential-osxkeychain
☁  cs3240-labdemo [master] ⚡ chmod u+x git-credential-osxkeychain
☁  cs3240-labdemo [master] ⚡ sudo mv git-credential-osxkeychain \
> "$(dirname $(which git))/git-credential-osxkeychain"
☁  cs3240-labdemo [master] git config --global credential.helper osxkeychain
☁  cs3240-labdemo [master] 
☁  cs3240-labdemo [master] git credential-osxkeychain
usage: git credential-osxkeychain <get|store|erase>
☁  cs3240-labdemo [master] git credential-osxkeychain get

password=Helen0408
username=brianaguirre
☁  cs3240-labdemo [master] git credential-osxkeychain ba5bx
Helen0408
bad input: Helen0408
☁  cs3240-labdemo [master] git credential-osxkeychain
usage: git credential-osxkeychain <get|store|erase>
☁  cs3240-labdemo [master] git credential-osxkeychain 
usage: git credential-osxkeychain <get|store|erase>
☁  cs3240-labdemo [master] 
☁  cs3240-labdemo [master] git credential-osxkeychain erase
brianaguirre
bad input: brianaguirre
☁  cs3240-labdemo [master] git credential-osxkeychain
usage: git credential-osxkeychain <get|store|erase>
☁  cs3240-labdemo [master] git credential-osxkeychain get

password=Helen0408
username=brianaguirre
☁  cs3240-labdemo [master] git credential-osxkeychain store
Brian aguirre
bad input: Brian aguirre
☁  cs3240-labdemo [master] git config credential.helper
osxkeychain
☁  cs3240-labdemo [master] git config --global credential.helper osxkeychain
☁  cs3240-labdemo [master] git config --global credential.helper osxkeychain
☁  cs3240-labdemo [master] git config credential-osxkeychain 
error: key does not contain a section: credential-osxkeychain
☁  cs3240-labdemo [master] git config --global credential-osxkeychain
error: key does not contain a section: credential-osxkeychain
☁  cs3240-labdemo [master] git config --global credential.helper 
osxkeychain
☁  cs3240-labdemo [master] git config user.name "ba5bx"    
☁  cs3240-labdemo [master] git config user.email "ba5bx@virginia.edu"
☁  cs3240-labdemo [master] git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
nothing to commit, working directory clean
☁  cs3240-labdemo [master] git push
Warning: Permanently added the RSA host key for IP address '192.30.252.128' to the list of known hosts.
Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
☁  cs3240-labdemo [master] ls        
LICENSE   README.md hello.py
☁  cs3240-labdemo [master] git commit -m 
error: switch `m' requires a value
usage: git commit [options] [--] <pathspec>...

    -q, --quiet           suppress summary after successful commit
    -v, --verbose         show diff in commit message template

Commit message options
    -F, --file <file>     read message from file
    --author <author>     override author for commit
    --date <date>         override date for commit
    -m, --message <message>
                          commit message
    -c, --reedit-message <commit>
                          reuse and edit message from specified commit
    -C, --reuse-message <commit>
                          reuse message from specified commit
    --fixup <commit>      use autosquash formatted message to fixup specified commit
    --squash <commit>     use autosquash formatted message to squash specified commit
    --reset-author        the commit is authored by me now (used with -C/-c/--amend)
    -s, --signoff         add Signed-off-by:
    -t, --template <file>
                          use specified template file
    -e, --edit            force edit of commit
    --cleanup <default>   how to strip spaces and #comments from message
    --status              include status in commit message template
    -S, --gpg-sign[=<key-id>]
                          GPG sign commit

Commit contents options
    -a, --all             commit all changed files
    -i, --include         add specified files to index for commit
    --interactive         interactively add files
    -p, --patch           interactively add changes
    -o, --only            commit only specified files
    -n, --no-verify       bypass pre-commit hook
    --dry-run             show what would be committed
    --short               show status concisely
    --branch              show branch information
    --porcelain           machine-readable output
    --long                show status in long format (default)
    -z, --null            terminate entries with NUL
    --amend               amend previous commit
    --no-post-rewrite     bypass post-rewrite hook
    -u, --untracked-files[=<mode>]
                          show untracked files, optional modes: all, normal, no. (Default: all)

☁  cs3240-labdemo [master] git commit -m hello.py
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
nothing to commit, working directory clean
☁  cs3240-labdemo [master] git add hello.py
☁  cs3240-labdemo [master] git push
Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
☁  cs3240-labdemo [master] cd .git 
☁  .git [master] vim config 
☁  .git [master] ..
☁  cs3240-labdemo [master] la
total 32
drwxr-xr-x  14 BrianAguirre  staff   476B Sep 28 11:38 .git
-rw-r--r--   1 BrianAguirre  staff   702B Sep 28 09:49 .gitignore
-rw-r--r--   1 BrianAguirre  staff   1.0K Sep 28 09:49 LICENSE
-rw-r--r--   1 BrianAguirre  staff    17B Sep 28 09:49 README.md
-rw-r--r--   1 BrianAguirre  staff    45B Sep 28 10:13 hello.py
☁  cs3240-labdemo [master] cd .git 
☁  .git [master] la
total 48
-rw-r--r--   1 BrianAguirre  staff     9B Sep 28 11:37 COMMIT_EDITMSG
-rw-r--r--   1 BrianAguirre  staff    23B Sep 28 09:49 HEAD
drwxr-xr-x   2 BrianAguirre  staff    68B Sep 28 09:49 branches
-rw-r--r--   1 BrianAguirre  staff   358B Sep 28 11:36 config
-rw-r--r--   1 BrianAguirre  staff    73B Sep 28 09:49 description
drwxr-xr-x  11 BrianAguirre  staff   374B Sep 28 09:49 hooks
-rw-r--r--   1 BrianAguirre  staff   361B Sep 28 10:14 index
drwxr-xr-x   3 BrianAguirre  staff   102B Sep 28 09:49 info
drwxr-xr-x   4 BrianAguirre  staff   136B Sep 28 09:49 logs
drwxr-xr-x  12 BrianAguirre  staff   408B Sep 28 10:14 objects
-rw-r--r--   1 BrianAguirre  staff   107B Sep 28 09:49 packed-refs
drwxr-xr-x   5 BrianAguirre  staff   170B Sep 28 09:49 refs
☁  .git [master] vim config 
☁  .git [master] ..
☁  cs3240-labdemo [master] l
total 32
drwxr-xr-x   7 BrianAguirre  staff   238B Sep 28 10:38 .
drwxr-xr-x   4 BrianAguirre  staff   136B Sep 28 09:49 ..
drwxr-xr-x  14 BrianAguirre  staff   476B Sep 28 11:39 .git
-rw-r--r--   1 BrianAguirre  staff   702B Sep 28 09:49 .gitignore
-rw-r--r--   1 BrianAguirre  staff   1.0K Sep 28 09:49 LICENSE
-rw-r--r--   1 BrianAguirre  staff    17B Sep 28 09:49 README.md
-rw-r--r--   1 BrianAguirre  staff    45B Sep 28 10:13 hello.py
☁  cs3240-labdemo [master] gp
Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
☁  cs3240-labdemo [master] gp -f
Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
☁  cs3240-labdemo [master] git remote -v 
origin	git@github.com:ba5bx/cs3240-labdemo.git (fetch)
origin	git@github.com:ba5bx/cs3240-labdemo.git (push)
☁  cs3240-labdemo [master] git credential-osxkeychain
usage: git credential-osxkeychain <get|store|erase>
☁  cs3240-labdemo [master] curl -s -O \
> https://github-media-downloads.s3.amazonaws.com/osx/git-credential-osxkeychain
☁  cs3240-labdemo [master] ⚡ chmod u+x git-credential-osxkeychain
☁  cs3240-labdemo [master] ⚡ sudo mv git-credential-osxkeychain \
> "$(dirname $(which git))/git-credential-osxkeychain"
Password:
☁  cs3240-labdemo [master] git config --global credential.helper osxkeychain
☁  cs3240-labdemo [master] gp
Warning: Permanently added the RSA host key for IP address '192.30.252.130' to the list of known hosts.
Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
☁  cs3240-labdemo [master] git remote -v
origin	git@github.com:ba5bx/cs3240-labdemo.git (fetch)
origin	git@github.com:ba5bx/cs3240-labdemo.git (push)
☁  cs3240-labdemo [master] sudo git push                                    
Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
☁  cs3240-labdemo [master] sudo mv git-credential-osxkeychain \             
"$(dirname $(which git))/git-credential-osxkeychain"
mv: git-credential-osxkeychain: No such file or directory
☁  cs3240-labdemo [master] sudo mv git-credential-osxkeychain \
"$(dirname $(which git))/git-credential-osxkeychain"
mv: git-credential-osxkeychain: No such file or directory
☁  cs3240-labdemo [master] git credential-osxkeychain
usage: git credential-osxkeychain <get|store|erase>
☁  cs3240-labdemo [master] git credential-osxkeychain
usage: git credential-osxkeychain <get|store|erase>
☁  cs3240-labdemo [master] sudo mv git-credential-osxkeychain \
> "$(dirname $(which git))/git-credential-osxkeychain"
mv: git-credential-osxkeychain: No such file or directory
☁  cs3240-labdemo [master] chmod u+x git-credential-osxkeychain
chmod: git-credential-osxkeychain: No such file or directory
☁  cs3240-labdemo [master] git credential-osxkeychain                     
usage: git credential-osxkeychain <get|store|erase>
☁  cs3240-labdemo [master] curl -s -O \
> https://github-media-downloads.s3.amazonaws.com/osx/git-credential-osxkeychain
☁  cs3240-labdemo [master] ⚡ chmod u+x git-credential-osxkeychain
☁  cs3240-labdemo [master] ⚡ sudo mv git-credential-osxkeychain \
> "$(dirname $(which git))/git-credential-osxkeychain"
☁  cs3240-labdemo [master] sudo mv git-credential-osxkeychain \
"$(dirname $(which git))/git-credential-osxkeychain"
mv: git-credential-osxkeychain: No such file or directory
☁  cs3240-labdemo [master] git pugh                            
git: 'pugh' is not a git command. See 'git --help'.

Did you mean this?
	push
☁  cs3240-labdemo [master] y
zsh: command not found: y
☁  cs3240-labdemo [master] git push
Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
☁  cs3240-labdemo [master] ..
☁  labs  git clone git@github.com:ba5bx/cs3240-labdemo.git
fatal: destination path 'cs3240-labdemo' already exists and is not an empty directory.
☁  labs  git clone git@github.com:ba5bx/cs3240-labdemo.git
Cloning into 'cs3240-labdemo'...
Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
☁  labs  cd lab5 
☁  lab5  git clone git@github.com:ba5bx/cs3240-labdemo.git
Cloning into 'cs3240-labdemo'...
Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
☁  lab5  git clone https://github.com/ba5bx/cs3240-labdemo.git
Cloning into 'cs3240-labdemo'...
remote: Counting objects: 5, done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (5/5), done.
Checking connectivity... done.
☁  lab5  cd cs3240-labdemo 
☁  cs3240-labdemo [master] git add hello.py 
☁  cs3240-labdemo [master] ⚡ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   hello.py

☁  cs3240-labdemo [master] ⚡ git commit -m "Initial commit"
[master de1772d] Initial commit
 1 file changed, 3 insertions(+)
 create mode 100644 hello.py
☁  cs3240-labdemo [master] git push
remote: Permission to ba5bx/cs3240-labdemo.git denied to brianaguirre.
fatal: unable to access 'https://github.com/ba5bx/cs3240-labdemo.git/': The requested URL returned error: 403
☁  cs3240-labdemo [master] git config user.name "ba5bx"
☁  cs3240-labdemo [master] git config user.email ba5bx@virginia.edu
☁  cs3240-labdemo [master] git push
remote: Permission to ba5bx/cs3240-labdemo.git denied to brianaguirre.
fatal: unable to access 'https://github.com/ba5bx/cs3240-labdemo.git/': The requested URL returned error: 403
☁  cs3240-labdemo [master] git credential-osxkeychain
usage: git credential-osxkeychain <get|store|erase>
☁  cs3240-labdemo [master] git config --global credential.helper osxkeychain
☁  cs3240-labdemo [master] git push                                         
remote: Permission to ba5bx/cs3240-labdemo.git denied to brianaguirre.
fatal: unable to access 'https://github.com/ba5bx/cs3240-labdemo.git/': The requested URL returned error: 403
☁  cs3240-labdemo [master] ssh-add -d ~/.ssh/old_key_file
Bad key file /Users/BrianAguirre/.ssh/old_key_file
☁  cs3240-labdemo [master] ..  
☁  lab5  git clone https://github.com/brianaguirre/cs3240-labdemo.git
fatal: destination path 'cs3240-labdemo' already exists and is not an empty directory.
☁  lab5  git clone https://github.com/brianaguirre/cs3240-labdemo.git
Cloning into 'cs3240-labdemo'...
remote: Counting objects: 5, done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (5/5), done.
Checking connectivity... done.
☁  lab5  cd cs3240-labdemo 
☁  cs3240-labdemo [master]           
