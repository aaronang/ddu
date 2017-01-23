Basically, the goal of my thesis: **creating (improving) a tool that guides the developer in creating tests such that the diagnosability of the test suite improves**. Therefore, I am currently exploring the possibilities to convey the concept of DDU to the developer.

1. Explore and implement visualizations. In this stage, it is important to take the following into account:

  * Amount of data shown at a time. The information should be easy to digest.
  * Change scope of interest. For example, the developer should be capable of selecting the package or class of interest.
  * Improvements are easy to observe. The developer should be able to see immediately what parts of the test suite can be improved or extended.
  * Provide context, i.e. structure of code. The visualization should reflect the structure of the code, thus, most likely a tree-like visualization.
  * Easy to navigate.
  * Components linked to code, i.e. IDE integration. This is not yet important but would be useful for evaluation.

  **2 - 3 WEEKS**

2. Create a framework that allows us (or the developer) to easily switch visualizations.

  Potential DDU visualizations:

  * [Zoomable Circle Packing](http://bl.ocks.org/mbostock/7607535)
  * [Zoomable Sunburst](http://bl.ocks.org/mbostock/4348373)
  * [Zoomable Icicle](http://bl.ocks.org/mbostock/1005873)
  * [Zoomable Treemap](https://bost.ocks.org/mike/treemap/)
  * [Collapsible Tree Layout](http://mbostock.github.io/d3/talk/20111018/tree.html)

  What about using multiple visualizations?

  **2 WEEKS**

3. Evaluate the visualizations. We first thought of a case study because it definitely has less confounding factors as opposed to a user study. However, we didn't immediately see how we could evaluate the tool in a case study. **Do you maybe have any suggestions on how to evaluate the tool?**

  **6 WEEKS**

4. Remaining weeks will be spent on writing a paper/report.
