## Commons CSV

Commons CSV has been chosen mainly due to its high code coverage and its small codebase.


### Coverage

Code coverage generated with IntelliJ.

|class %|method %|line %|
|---|---|---|
|100% (15/15)|97% (169/174)|93% (741/795)|


### Class-package granularity

|parent|number_of_components|number_of_tests|unit_tests|integration_tests|density|normalized_density|diversity|uniqueness|ddu|
|---|---|---|---|---|---|---|---|---|---|
|org.apache.commons.csv|12|259|74|185|0.32142857142857145|0.6428571428571429|0.8264942683547335|1.0|0.5313177439423287|

Similar to Guice, the `org.apache.commons.csv` package has a relative high number of test cases compared to the number of components.
This has the effect that it is unlikely to have component ambiguity and thus the package has a high uniqueness.
Although it seems that there is "good" balance between unit and integration tests, the density is still on the low side and thus causing the normalized density to be "low".
Note that an integration test is a test that hits two or more components.
To improve the density, one could either reduce the number of unit tests, or write more integration tests that hit "a lot" of components.
It is debatable though if the tests make any sense if one would write integration tests that randomly hits many components that might have nothing to do with each other.

### Method-package granularity


### Method-class granularity


## Observations
