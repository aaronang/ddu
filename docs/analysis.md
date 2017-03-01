# Case Study

In this case study, we will look at a couple real projects.
The projects are chosen because they are popular, have a working test suite, are working with the DDU maven plugin


## Commons Text

Commons Text has been chosen mainly due to its _extremely_ high code coverage.
This, in particular, is interesting because the results clearly show that a high code coverage does not result in a high DDU value.


### Coverage

|class %|method %|line %|
|---|---|---|
|97% (67/69)|95% (520/544)|96% (3035/3148)|


### Class granularity

|package|number_of_components|number_of_tests|unit_vs_integration|density|normalized_density|diversity|uniqueness|ddu|
|---|---|---|---|---|---|---|---|---|
|org.apache.commons.text.beta.diff|7|5|0.0|0.9142857142857143|0.17142857142857149|0.6|0.2857142857142857|0.029387755102040822|
|org.apache.commons.text.beta.similarity|16|105|3.772727272727273|0.07678571428571429|0.15357142857142858|0.7978021978021979|0.8125|0.09954719387755104|
|org.apache.commons.text.beta.translate|15|56|0.12|0.22976190476190475|0.45952380952380945|0.951948051948052|1.0|0.4374427952999381|
|org.apache.commons.text.beta|49|465|1.3969072164948453|0.040245775729646695|0.08049155145929343|0.8920189098998887|0.8367346938775511|0.06007753929680936|

The DDU of `commons-text` is low using when computed using the class-granularity, namely `0.0600`.

The DDU for `org.apache.commons.text.beta.diff` is low because every test, that covers the components of this package, covers almost all components.
In other words, the tests written for this package are all integration tests, covering most components.
This results in no test diversity and components ambiguity groups, i.e. low diversity and low uniqueness.

The density of `org.apache.commons.text.beta.similarity` is low for two reasons; (1) the number of components is _high_, and (2) all test cases are unit tests.
This results in a sparse matrix.
The more components a package contains, the more difficult it is to get a balanced density of `0.5`.
Because the test suite for this package consists of unit tests only, the diversity and uniqueness are higher.
Although the diversity and uniqueness are _okay_, the DDU is still low due to the low normalized density.

`org.apache.text.beta.translate` is tested by approximately 39 unit tests and 17 integration tests.
Interestingly, although the integration tests cover similar components, the diversity is still _high_.
Assuming that the 17 integration tests have the same activity, and that the 39 unit tests have dissimilar activities.
The Gini-Simpson index is computed as follows.
```
diversity = 1 - (17 * 16) / (56 * 55) = 0.911688
```
This also explains why the diversity of `org.apache.commons.text.beta.diff` isn't that _low_ either.
Due to the fact that each test is covered by at least one unit test and a couple of integration tests, component ambiguity is not present, thus a uniqueness of `1`.

For the package `org.apache.commons.text.beta`, i.e. the complete codebase, it is difficult to achieve a balanced density because unit tests easily result in a sparse activity matrix.
This effect becomes more apparent when the number of components increases.


### Method granularity

|package|number_of_components|number_of_tests|unit_vs_integration|density|normalized_density|diversity|uniqueness|ddu|
|---|---|---|---|---|---|---|---|---|
|org.apache.commons.text.beta.diff|28|5|0.0|0.7857142857142857|0.4285714285714286|0.9|0.17857142857142858|0.06887755102040817|
|org.apache.commons.text.beta.similarity|60|105|0.3815789473684211|0.04523809523809524|0.09047619047619049|0.854029304029304|0.5333333333333333|0.04121030292458864|
|org.apache.commons.text.beta.translate|57|56|0.07692307692307693|0.10432330827067669|0.2086466165413534|0.974025974025974|0.7719298245614035|0.15687715529425067|
|org.apache.commons.text.beta|537|464|0.08665105386416862|0.0230767995890323|0.04615359917806461|0.9916213599463767|0.6759776536312849|0.030937398149653968|


|class|number_of_components|number_of_tests|unit_vs_integration|density|normalized_density|diversity|uniqueness|ddu|
|---|---|---|---|---|---|---|---|---|
|org.apache.commons.text.beta.AlphabetConverter|14|12|0.0|0.5595238095238095|0.8809523809523809|0.8484848484848485|0.5714285714285714|0.42712842712842713|
|org.apache.commons.text.beta.CharacterPredicates|4|1|0.0|0.5|1.0|0|0.5|0.0|
|org.apache.commons.text.beta.CompositeFormat|6|2|0.0|0.75|0.5|1.0|0.5|0.25|
|org.apache.commons.text.beta.diff.DeleteCommand|2|5|0.6666666666666666|0.8|0.3999999999999999|0.6|1.0|0.23999999999999994|
|org.apache.commons.text.beta.diff.EditCommand|2|5|0.6666666666666666|0.8|0.3999999999999999|0.6|1.0|0.23999999999999994|
|org.apache.commons.text.beta.diff.EditScript|7|5|0.0|0.7142857142857143|0.5714285714285714|0.7|0.5714285714285714|0.22857142857142854|
|org.apache.commons.text.beta.diff.InsertCommand|2|5|0.6666666666666666|0.8|0.3999999999999999|0.6|1.0|0.23999999999999994|
|org.apache.commons.text.beta.diff.KeepCommand|2|5|0.6666666666666666|0.8|0.3999999999999999|0.6|1.0|0.23999999999999994|
|org.apache.commons.text.beta.diff.ReplacementsFinder|4|2|0.0|1.0|0.0|0.0|0.25|0.0|
|org.apache.commons.text.beta.diff.StringsComparator|9|5|0.0|1.0|0.0|0.0|0.1111111111111111|0.0|
|org.apache.commons.text.beta.ExtendedMessageFormat|21|14|0.0|0.3741496598639456|0.7482993197278912|0.9560439560439561|0.6190476190476191|0.44287102596140504|
|org.apache.commons.text.beta.FormattableUtils|6|7|0.75|0.2619047619047619|0.5238095238095238|0.9523809523809523|1.0|0.4988662131519274|
|org.apache.commons.text.beta.similarity.CosineDistance|2|1|-1|0.5|1.0|0|1.0|0.0|
|org.apache.commons.text.beta.similarity.CosineSimilarity|4|1|0.0|0.75|0.5|0|0.5|0.0|
|org.apache.commons.text.beta.similarity.Counter|2|1|-1|0.5|1.0|0|1.0|0.0|
|org.apache.commons.text.beta.similarity.EditDistanceFrom|4|13|0.08333333333333333|0.4807692307692308|0.9615384615384616|0.15384615384615385|0.75|0.11094674556213019|
|org.apache.commons.text.beta.similarity.FuzzyScore|3|5|-1|0.3333333333333333|0.6666666666666666|0.4|1.0|0.26666666666666666|
|org.apache.commons.text.beta.similarity.HammingDistance|2|6|-1|0.5|1.0|0.0|1.0|0.0|
|org.apache.commons.text.beta.similarity.JaccardDistance|2|4|-1|0.5|1.0|0.0|1.0|0.0|
|org.apache.commons.text.beta.similarity.JaccardSimilarity|3|5|1.5|0.4666666666666667|0.9333333333333333|0.6|1.0|0.5599999999999999|
|org.apache.commons.text.beta.similarity.JaroWinklerDistance|3|7|0.75|0.5238095238095238|0.9523809523809523|0.5714285714285714|1.0|0.5442176870748299|
|org.apache.commons.text.beta.similarity.LevenshteinDetailedDistance|8|10|0.1111111111111111|0.3875|0.775|0.8|0.875|0.5425000000000001|
|org.apache.commons.text.beta.similarity.LevenshteinDistance|7|53|0.019230769230769232|0.39892183288409705|0.7978436657681941|0.4390420899854862|0.8571428571428571|0.3002459575718997|
|org.apache.commons.text.beta.similarity.LevenshteinResults|8|5|0.0|0.4|0.8|0.9|0.625|0.45000000000000007|
|org.apache.commons.text.beta.similarity.LongestCommonSubsequence|6|12|3.0|0.25|0.5|0.8636363636363636|0.8333333333333334|0.35984848484848486|
|org.apache.commons.text.beta.similarity.LongestCommonSubsequenceDistance|2|4|-1|0.5|1.0|0.0|1.0|0.0|
|org.apache.commons.text.beta.similarity.RegexTokenizer|2|1|-1|0.5|1.0|0|1.0|0.0|
|org.apache.commons.text.beta.similarity.SimilarityScoreFrom|4|4|0.0|0.5|1.0|0.0|0.5|0.0|
|org.apache.commons.text.beta.StrBuilder|166|230|0.0|0.05502881089575694|0.1100576217915139|0.9680653123220049|0.8072289156626506|0.08600456292617197|
|org.apache.commons.text.beta.StringEscapeUtils|27|27|2.0|0.05486968449931413|0.10973936899862824|0.9658119658119658|0.6666666666666666|0.07065839713301988|
|org.apache.commons.text.beta.StrLookup|7|41|0.0|0.5331010452961672|0.9337979094076656|0.4536585365853658|0.8571428571428571|0.3631074797557333|
|org.apache.commons.text.beta.StrMatcher|20|128|0.04065040650406504|0.208984375|0.41796875|0.9190452755905512|0.95|0.3649255947803888|
|org.apache.commons.text.beta.StrSubstitutor|55|41|0.0|0.4270509977827051|0.8541019955654102|0.9158536585365854|0.6181818181818182|0.4835618703939509|
|org.apache.commons.text.beta.StrTokenizer|66|59|0.0|0.25783256291730866|0.5156651258346173|0.9877264757451782|0.7121212121212122|0.3627090390613646|
|org.apache.commons.text.beta.translate.AggregateTranslator|2|24|7.0|0.5625|0.875|0.3007246376811594|1.0|0.2631340579710145|
|org.apache.commons.text.beta.translate.CharSequenceTranslator|5|51|0.10869565217391304|0.4666666666666667|0.9333333333333333|0.6486274509803922|1.0|0.6053856209150328|
|org.apache.commons.text.beta.translate.CodePointTranslator|2|21|1.1|0.7380952380952381|0.5238095238095237|0.6095238095238096|1.0|0.31927437641723355|
|org.apache.commons.text.beta.translate.CsvTranslators|4|5|0.25|0.65|0.7|0.4|0.5|0.13999999999999999|
|org.apache.commons.text.beta.translate.EntityArrays|2|2|-1|0.5|1.0|1.0|1.0|1.0|
|org.apache.commons.text.beta.translate.JavaUnicodeEscaper|6|7|0.4|0.38095238095238093|0.7619047619047619|0.9523809523809523|1.0|0.7256235827664398|
|org.apache.commons.text.beta.translate.LookupTranslator|2|25|7.333333333333333|0.56|0.8799999999999999|0.29000000000000004|1.0|0.2552|
|org.apache.commons.text.beta.translate.NumericEntityEscaper|7|7|0.4|0.3673469387755102|0.7346938775510204|0.9523809523809523|1.0|0.6997084548104956|
|org.apache.commons.text.beta.translate.NumericEntityUnescaper|6|12|1.4|0.2638888888888889|0.5277777777777778|0.6666666666666667|0.8333333333333334|0.29320987654320996|
|org.apache.commons.text.beta.translate.OctalUnescaper|4|4|0.3333333333333333|0.5625|0.875|0.8333333333333334|0.75|0.546875|
|org.apache.commons.text.beta.translate.SingleLookupTranslator|2|2|1.0|0.75|0.5|1.0|1.0|0.5|
|org.apache.commons.text.beta.translate.SinglePassTranslator|3|7|6.0|0.38095238095238093|0.7619047619047619|0.5238095238095238|1.0|0.39909297052154197|
|org.apache.commons.text.beta.translate.UnicodeEscaper|8|15|1.5|0.21666666666666667|0.43333333333333335|0.7619047619047619|0.875|0.28888888888888886|
|org.apache.commons.text.beta.translate.UnicodeUnescaper|2|6|1.0|0.75|0.5|0.7333333333333334|1.0|0.3666666666666667|
|org.apache.commons.text.beta.translate.UnicodeUnpairedSurrogateRemover|2|5|-1|0.5|1.0|0.4|1.0|0.4|
