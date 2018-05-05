# How Do I Work With You?

# Get setup

1. create a directory name t25
  - *(this is for everyone's convenience in finding the repo after it's been downloaded)*
1. Log into your git account
1. navigate to [here](https://github.com/mobycoder001/Wi2018-Classroom)
1. cd to your t25 directory
1. clone this repository
  - *(it looks alot like the class repository (go to the next step))*
1. cd to t25/Wi2018-Classroom/students/mark/ProjectProposals/
  - Look for the README.md file (this is the project summary file)
1. checkout the branch currentproject (this has all the thing we are working on, make your changes here)
  > - **alternate** *(skip this section if it sounds complex, just make changes in the branch **currentproject** )*
    > - checkout the branch currentproject
    > - from currentproject, create a branch with "your_name"
    > - do a git branch -a -v (you'll see you have the same hash number for your branch and the currentproject branch)
    > - checkout your branch: git checkout "your_name"
    > - make changes, commit, change, push pull, whatever 'till your heart is content
    > - git checkout currentproject
    > - git merge currentproject (fix any merge conflicts)
    > - git push when merge conflicts are resolved
    > - git checkout "your_name"
1. how to submit code to this repo?  Create a pull request from your currentproject branch **note I think once I add you to this project you won't have to fork it, so get me your "git name"!

### How to we submit code to the class repo?
1. The build master will merge the *currentproject* branch into the master branch, at regular intervals the master branch will be submitted to the class repository via a pull request and Instructor1 and Instructor2 will be asked to take a look at it (we all have copies of this code on our machines)
1. Instructor1 and Instructor2 can also see all of our code on a direct link to this repo or via a cloning of the repository to thier local machines

*notes:
* we all haove both repos, we will see our published changes in the class repo and our working changes in the currentproject in this repo
* This seems complex?  Why do it this way?
  - By doing this in a separate fork/repository, we can commit and share code as often as we like without waiting for a pull request to see each others commits (if we use the class repo, we're going to be waiting on a pull request, we use our own repos, it's going to be extremely difficult to review each others changes)


# I'm excited to get going and conribute code! What's next?
- send me an @username slack message with your git ID and asking to be added to the mobycoder001 storage
- "Hi my name is "your_name_here" and my git ID is "git_id", I' like to join and contribute to your project, please add me to your org
-


# environment setup
- see environment setup in this repo / 00_env_setup/README.md

Am I working on environment setup or just munging data files?
- That's up to you where you contribue, some people will pull data, some will munge data, some will present data, we can do it!
