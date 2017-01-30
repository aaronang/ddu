# DDU Guidance

Note that I am just writing down thoughts, which might not be logically organized.


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

### Recommendation

We experienced during the development of visualizations that the _right_ hierarchy-like visualization might not be the most important factor.
In fact, we think that interactivity or recommendation will be playing a greater role in determining the usefulness of the tool.
Additionally, it is _quite easy_ to switch between hierarchy-like D3.js visualizations.

In this section, we will focus on how we can suggest test cases to the developer.

* Enable the developer to select the class of interest and show which methods and combinations of methods are tested.
We could show the combinations by using color codes, an external visualization, or a table.

* Maybe we could use some other data sources, e.g. static analysis, dynamic analysis, to create a recommendation system for test cases.
* Since we are running test cases, maybe we can make use of static or dynamic call graphs to prevent false positive recommendations.
* Are there heuristics that can rank suggested test cases, such that the highest ranked suggested test cases will improve the diagnosability of the test suite more than lower ranked test cases?

## Concepts

I just decided to write down concepts because trying to document subsolutions to a problem is quite difficult.
Note that for discussing concepts I will be assuming a circle packing visualization because I like it the most.
However, the concepts that I will be discussing probably will be applicable to any hierarchy-like visualization.

### Concept 1

We might just want to show everything up until class-level, i.e. no methods are shown.
This will probably reduce information greatly and, therefore, will be easier to consume by the developer.
At these levels --- packages and classes --- the developer is able to see the higher-level code structure.
At this point, we would like to indicate which classes should be tested, for example, by means of color coding the DDU.
If we are hiding the methods, we do want to show the size of packages and classes.

## Questions

1. Do we want to display the DDU value? Or do we want to hide the DDU concept?

1. If we hide the notion of DDU, what are the possibilities to guide the developer in improving the DDU.

1. DDU approximates entropy. However, entropy is not the necessarily the optimal solution because it does not take into account the inherent dependencies in code, which may be impossible to test in isolation. Could we improve DDU to take this into account?

1. Even when we visualize the component combinations that should be tested in isolation, I think it is important that the developer knows why these recommendations are made. Thus, the developer should understand the underlying idea of DDU. Would good documentation be sufficient?

1. What do developers prefer? Suggestion for tests that involve multiple classes or a single class? **SURVEY!**
