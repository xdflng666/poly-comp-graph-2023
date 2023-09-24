# poly-comp-graph-2023
## Setup
Install the freeglut3-dev package using the command:
```bash
sudo apt install freeglut3-dev
```

Now you can create a new C++ file and include the GLUT library using the following command:
```cpp
#include <GL/glut.h>
```

## Build
```bash
g++ -o output_file input_file.cpp -lglut -lGLU -lGL
```	
