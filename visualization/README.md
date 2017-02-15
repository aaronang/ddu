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

## Coverage Data

| Project | Artifact ID |Class % | Method % | Line % | Branch % | Density | Diversity | Uniqueness | DDU |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Commons Text](https://github.com/apache/commons-text) | commons-text |  |  | 96% (3036/3152)* | 91% (1487/1623)* | | | | |
| [Commons CLI](https://github.com/apache/commons-cli) | commons-cli |  |  | 96% (1127/1171)* | 93% (653/698)* | | | | |
| [Commons Numbers](https://github.com/apache/commons-numbers) | commons-numbers-core |  |  | 96% (327/338)* | 87% (277/315)* | | | | |
| [Commons Lang**](https://github.com/apache/commons-lang) | commons-lang3 |  |  | 94% (14143/14970)* | 90% (8876/9799)* | 0.0050 | 0.9863 | 0.5066 | 0.0050 |
| [Commons CSV**](https://github.com/apache/commons-csv) | commons-csv |  |  | 93% (741/795)* | 88% (501/569)* | | | | |
| [Commons Math](https://github.com/apache/commons-math) | commons-math |  |  | 90% (40660/45155)* | 84% (16625/19588)* | | | | |
| [Commons IO](https://github.com/apache/commons-io) | commons-io |  |  | 90% (4691/5200)* | 86% (2251/2610)* | | | | |
| [Guice**](https://github.com/google/guice) | core | |  | 90% (6472/7149)* | 83% (2095/2513)* | | | | |
| [JUnit 4**](https://github.com/junit-team/junit4) | junit |  |  | 86% (4136/4771)* | 84% (1246/1472)* | 0.0554 | 0.9991 | 0.3344 | 0.0370 |
| [Retrofit**](https://github.com/square/retrofit) | retrofit | 94% (50/53) | 85% (200/233) | 86% (1197/1376)* | 76% (581/756)* | 0.0631 | 0.9945 | 0.2439 | 0.0306 |
| [Spring Boot](https://github.com/spring-projects/spring-boot) | spring-boot |  |  | 85% (8220/9577)* | 79% (2522/3192)* | | | | |
| [Commons Collections**](https://github.com/apache/commons-collections) | commons-collections |  |  | 85% (11217/13161)* | 78% (4763/6087)* | | | | |
| [ZXing**](https://github.com/zxing/zxing) | core | 94% (248/262) | 86% (1409/1629) | 84% (10015/11854)* | 73% (5199/7045)* | | | | |
| [Commons Compress](https://github.com/apache/commons-compress) | commons-compress |  |  | 83% (10254/12228)* | 72% (4115/5644)* | | | | |
| [Auto**](https://github.com/google/auto) | auto-common |  |  | 83% (774/932)* | 78% (357/456)* | 0.0401 | 0.9914 | 0.1407 | 0.0112 |
| [jsoup**](https://github.com/jhy/jsoup) | jsoup |  |  | 77% (5327/6893)* | 72% (2548/3494)* | 0.1177 | 0.9997 | 0.4411 | 0.1038 |
| [Commons Validator](https://github.com/apache/commons-validator) | commons-validator |  |  | 77% (2370/3041)* | 75% (1258/1665)* | | | | |
| [Commons FileUpload](https://github.com/apache/commons-fileupload) | commons-upload |  |  | 76% (888/1162)* | 76% (348/452)* | | | | |
| [Wicket](https://github.com/apache/wicket) | wicket-core |  |  | 72% (22539/31191)* | 66% (8552/12803)* | | | | |
| [Spark](https://github.com/perwendel/spark) | spark-core |  |  | 68% (1817/2654)* | 56% (569/1002)* | | | | |
| [Flink](https://github.com/apache/flink) | flink-core |  |  | 51% (10021/19468)* | 40% (4496/11163)* | | | | |
| [Dagger](https://github.com/google/dagger) | core |  |  | 48% (122/252)* | 43% (51/116)* | | | | |
| [Maven](https://github.com/apache/maven) | maven-core |  |  | 48% (5183/10742)* | 36%	(1603/4405)* | | | | |
| [libGDX](https://github.com/libgdx/libgdx) | gdx | 2% (26/961) | 1% (140/10076) | 1% (689/55041) | | | | | |
| [Netty](https://github.com/netty/netty) | common | 48% (137/283) | 37% (822/2202) | 31% (3599/11330) | | | | | |
| [Dubbo](https://github.com/alibaba/dubbo) | dubbo-common | 55% (174/315) | 41% (942/2285) | 43% (6369/14630) | | | | | |
| [Fastjson](https://github.com/alibaba/fastjson) | fastjson |  |  |  | | | | | |
| [Commons Net](https://github.com/apache/commons-net) | commons-net |  |  | 30% (2824/9395)* | 26% (978/3735)* | | | | | |

\* Cobertura coverage, default coverage is generated by IntelliJ<br>
** Done with DDU

## Observations
The above table shows the DDU values using the method-granularity.
We observe that even in well-tested software, the DDU value is extremely low.

### Density
The density term seems to be impacting the DDU considerably.
A high density is nearly impossible to achieve when the system grows larger.
Actually, the density metric favors writing integration tests instead of unit tests because unit tests contribute to the sparseness of the activity matrix.
This sparseness contribution becomes a larger problem when a system consists of a larger number of classes.

### Diversity
Diversity seems to be almost always optimal.
Do we really need this term?
From the theoretical perspective, it seems like a beautiful metric.
However, based on our observations from real-world projects, the diversity is almost always optimal.

### Uniqueness
It makes sense to not have the same components being activated together in every single test, this reduces the diagnosability.
If a fault would occur, it would be difficult to identify which of the two is really responsible for the fault.
