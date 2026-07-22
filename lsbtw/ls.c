#include <dirent.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
  char *path = (argc > 1) ? argv[1] : ".";

  DIR *dir = opendir(path); // DIR is called an opaque pointer
  if (!dir) {
    perror("opendir");
    return 1;
  }
  struct dirent *entry;
  while ((entry = readdir(dir)) != NULL) {
    if (entry->d_name[0] == '.')
      continue;
    printf("%s\n", entry->d_name);
  }
  closedir(dir);
  return 0;
}
