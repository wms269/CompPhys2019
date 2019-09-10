Helpful macro for only adding files that are already in the repo, but
need to be updated.

alias gitadd='for fil in $(git diff --name-only --relative); do git add $fil; done'
