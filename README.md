# DDU Guidance

## Questions

1. Do we want to display the DDU value? Or do we want to hide the DDU concept?

2. If we hide the notion of DDU, what are the possibilities to guide the developer in improving the DDU.

3. DDU approximates entropy. However, entropy is not the necessarily the optimal solution because it does not take into account the inherent dependencies in code, which may be impossible to test in isolation. Could we improve DDU to take this into account?

4. Even when we visualize the component combinations that should be tested in isolation, I think it is important that the developer knows why these recommendations are made. Thus, the developer should understand the underlying idea of DDU. Would good documentation be sufficient?

## DDU Value Visualization

DDU visualization requires the developer to know about the DDU concept.
Ultimately, the developer should know how DDU is computed such that the developer knows how DDU can be improved for a particular program entity, e.g. package, class.

Aspects that should be taken into account when visualizing DDU:

* Amount of data shown at a time.
* Pick scope of interest.
* Improvements are easy to observe.
* Provide context, i.e. structure of code.
* Easy to navigate.
* Components linked to code.

Potential DDU visualizations:

* [Zoomable Circle Packing](http://bl.ocks.org/mbostock/7607535)
* [Zoomable Sunburst](http://bl.ocks.org/mbostock/4348373)
* [Zoomable Icicle](http://bl.ocks.org/mbostock/1005873)
* [Zoomable Treemap](https://bost.ocks.org/mike/treemap/)
* [Collapsible Tree Layout](http://mbostock.github.io/d3/talk/20111018/tree.html)

Zooming in and out makes it possible to hide unnecessary data, which could be easier on the eyes.
Additionally, this allows the developer to pick the scope of interest, i.e. package or class-level.
To ensure that critical components are easily visible, visualization can make use of **color codes**, **size**, or both.
As we can observe, the potential visualization are hierarchical and thus is able to visualize the tree-like code structure.

Possibilities:

* Visualize the DDU value by means of color codes or node size. This way, the developer knows which nodes can be improved.

Counterarguments:

* Class-level is probably the smallest granularity when displaying DDU values.
Classes can consists of many methods, resulting in the developer not knowing how to improve the DDU of a particular class.

Conclusion:

* DDU value visualization does probably not provide enough guidance in writing tests.
However, it could be used to guide developers at higher levels, i.e. package and class-level.
**This should be verified.**

## DDU Guidance

Aside from visualizations, we could output recommendations by means of text or a report.

Possibilities:

* Display the DDU values of the scope of interest and sort them in ascending order.
* Display component combinations that should be tested in isolation.
* An analytics platform, e.g. SonarQube plugin.


## DDU Guidance Visualization

Aspects that should be taken into account when visualizing DDU guidance:

* Show different component combinations to test.
* Due to structure of code, some combinations are inherently not possible to test in isolation. If possible, these combinations should be filtered out, or maybe the DDU computation can be improved regarding this?

Potential visualizations remain the same because we would like to display the structure of the code.
To the best of my knowledge, a tree-like structure is the only way of keeping the structure of the code intact.

Possibilities to show potential test cases:

* Zoomable Sunburst:
  * Select nodes: method
  * Select scope of interest: package, class
  * Select granularity of DDU analysis: method, block, line
  * Given selection: show combinations to test in isolation
  * Given no selection: show DDU of package, class
