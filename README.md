Hello! This is my library of **mathematical** and **numerical tools** for **scientific computing** which I utilize in my work
and teaching activities in **computational physics**. The library represents the foundation for using **modular programming technique**
in **Python-based** scientific computing and helps in solving variety of problems connected with mathematical modeling and simulation

# Modular programming: why I use it?

[Modular programming](https://en.wikipedia.org/wiki/Modular_programming) is an extremely helpful technique that helps to breake down
any large program into smaller modules or subprograms, saving time and effort when developing new scientific applications.

- **Focuses on reusability** - every existing module can be used multiple times in future projects.
  Even if you create a new module, you can be confident that it will likely be reused again in other projects.
  So, it **helps avoiding redundant work** and **promoting code consistency** across different applications.
- **Helps maintainability** and **flexibility.** By separating concerns into distinct modules, it becomes easier to maintain,
  debug, and update specific parts of the code without affecting the entire program.
- **Facilitates collaboration** and **organization** among developers or researchers, helps in **leading** and
  **reviewing the whole project** and supports **time management** and **self-organization** for individuals.
  Different team members can work on separate modules concurrently, divide tasks and then easily integrate their work.
- **Supports testing and verification**. Modular programming allows researchers to develop and test individual components
  of a computational model before combining them into a complete simulation.

# How I designed my library?

Following listed modular programming benefits I designed my library as a **systematized set of functions, algorithms,**
and **other utilities** that are sorted according to their **main purposes**. The library does not intend to cover the whole
variety of functions and methods in scientific computing or its particular branch; instead, it takes a more personalized approach,
helps current projects, and is undergoing continuous development.

- The library consists of **python modules** (functions) which are not independent projects themselves but rather **building blocks**
  that can be reused in multiple contexts or applications.
- In general, the library include different **working tools** for **manipulating**, **generating** and **representing mathematical objects**
  within different areas of numerical computing and also **algorithms** or its parts for solving complex mathematical problems,
  for example, differential equation problems.
- All tools are structured into several general topics which may also have their own **system of categories**.
  The whole tree of topics can be found below with their own descriptions.
- Each module has **similar code structure** and includes **short description**, sometimes with **references** or **additional info**.
- Additionally, some of the modules also have **examples** of how they can be used as separate functions which provide good **templates**
  and allow quick testing.

# Overview by sections

### ArrayTransform

Involves tools for **manipulating vectors**, **sets of vectors**, and related **discrete mathematical objects**
(functions, curves, surfaces, fields, etc.), relying primarily on rules and operations in **linear algebra**,
**analytical geometry** and **vector field theory.**

For example, modules in this section include:

- Basic transformations of coordinate systems for sets of points in geometrical spaces such as rotations, translations,
  compression and expansion, images
- Transition to curvilinear coordinates, work in curvilinear coordinates
- Alternatives or extensions for general linear algebra operations
- Generators of discrete periodic mathematical and geometric structures

### PlotVisualize

The majority of scientific computing problems require good **visualization** during the entire development and programming process,
and especially during the final **demonstration**. Practically, the task of visualizing is highly complicated
due to the variety of mathematical objects and its computer representations that must be shown. This section contains
different tools for **plotting** and **visualizing** for different kinds of objects.

For example: 

- Two-dimentional sets of functions and curves, sets of points
- Three-dimentional objects such as sets of points, curves, surfaces
- Sets of vectors, vector and scalar fields

### NumMethods

Contains wide range of **numerical** and **statistical algorithms** and related computing tools.

For example:

- Numerical differentiation and integration
- Solving equations and systems of equations
- Solving problems for ordinary differential equations
- Solving problems for partial differential equations
- Regression algorithms

### PointGenerators

It is common for scientific modeling tasks to involve functions, **geometric structures** and related mathematical objects that
can be represented as sets of points in space placed according to a rule. Objects such as curves and surfaces can be considered
to be this rule as well as any kind of periodic structures such as lattices. This section involves algorithms that generate
**ordered collections of points in a space** according to mentioned rules and taking several input parameters

### RandomDistribValues

Contains tools connected with random values and probability distributions

For example:

- Scalar generators with mean, Gauss or other distributions
- Vector generators (random directions or lengths), random rotations and coordinate systems
- Operations on other mathematical objects which are connected with random values and distributions such as adding noises and distortions

### SetsSeriesSequences

Numerical sequence generators and related tools
