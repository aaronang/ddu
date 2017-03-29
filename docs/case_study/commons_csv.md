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
It is debatable though if the tests would make any sense if one would write integration tests that randomly hits many components that might have nothing to do with each other.
As seen previously in Commons Text, the diversity is "quite high" because it doesn't penalize hard.
By looking at the diversity, it seems that "many" test cases share identical activity.

### Method-package granularity

|parent|number_of_components|number_of_tests|unit_tests|integration_tests|density|normalized_density|diversity|uniqueness|ddu|
|---|---|---|---|---|---|---|---|---|---|
|org.apache.commons.csv|184|259|3|256|0.1478722511331207|0.2957445022662414|0.9941336685522733|0.7717391304347826|0.2268986875699938|

Similar to Commons Text, we observe that the uniqueness decreases when examining a smaller granularity.
**This really might indicate that certain methods are always executed together due to design of software.**


### Method-class granularity

|parent|number_of_components|number_of_tests|unit_tests|integration_tests|density|normalized_density|diversity|uniqueness|ddu|
|---|---|---|---|---|---|---|---|---|---|
|org.apache.commons.csv.Assertions|2|157|157|0|0.5|1.0|0.0|1.0|0.0|
|org.apache.commons.csv.Constants|1|0|0|0|0|0.0|0|0|0.0|
|org.apache.commons.csv.CSVFormat|77|223|1|222|0.18554539630772815|0.3710907926154563|0.9838403425847372|0.8961038961038961|0.3271622387667717|
|org.apache.commons.csv.CSVParser|23|88|9|79|0.383399209486166|0.766798418972332|0.9177115987460815|0.8695652173913043|0.6119128721661448|
|org.apache.commons.csv.CSVPrinter|12|75|2|73|0.2877777777777778|0.5755555555555556|0.76|1.0|0.43742222222222227|
|org.apache.commons.csv.CSVRecord|18|91|7|84|0.13797313797313798|0.27594627594627597|0.8898656898656898|0.9444444444444444|0.23191317192131192|
|org.apache.commons.csv.ExtendedBufferedReader|10|110|0|110|0.5809090909090909|0.8381818181818181|0.9164303586321935|1.0|0.7681352642353476|
|org.apache.commons.csv.Lexer|20|105|0|105|0.690952380952381|0.618095238095238|0.9278388278388279|0.65|0.37277029478458046|
|org.apache.commons.csv.QuoteMode|3|2|2|0|0.3333333333333333|0.6666666666666666|1.0|1.0|0.6666666666666666|
|org.apache.commons.csv.Token|16|111|4|107|0.19313063063063063|0.38626126126126126|0.49172809172809173|0.5625|0.1068387260110233|
|org.apache.commons.csv.TokenMatchers|10|29|0|29|0.5241379310344828|0.9517241379310344|0.5788177339901478|0.6|0.3305248853405809|
|org.apache.commons.csv.Utils|2|8|8|0|0.5|1.0|0.0|1.0|0.0|

`org.apache.commons.csv.ExtendedBufferedReader` has a very high DDU.
The normalized density of this class is "quite good", namely `0.838`.
Based on the kind of test cases, we observe that there is no unit test, i.e. a test that hits only one method of class, and the average components hit is slightly higher than `50%` per test.


## Observations

- Density could guide the user in whether to write an integration test or unit test. What does a good density mean in practice? Does it imply anything?
- Would visualizing the activity matrix be interesting? I would argue that the developer could identify certain patterns in the activity matrix that could indicate how to test or design software?
