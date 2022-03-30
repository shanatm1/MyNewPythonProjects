# copyfile() = copies content of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (files creation and modification time)

import shutil
shutil.copyfile('test.txt','copy.txt')   #sameway we can create copy file in different location by giving
                                         # path here
                                         