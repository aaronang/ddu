## Commons Text

Commons Text has been chosen mainly due to its _extremely_ high code coverage, namely `96%`.
This, in particular, is interesting because the results clearly show that a high code coverage does not result in a high DDU value.


### Coverage

Code coverage generated with IntelliJ.

|class %|method %|line %|
|---|---|---|
|97% (67/69)|95% (520/544)|96% (3035/3148)|


### Class-package granularity

|parent|number_of_components|number_of_tests|unit_tests|integration_tests|density|normalized_density|diversity|uniqueness|ddu|
|---|---|---|---|---|---|---|---|---|---|
|org.apache.commons.text.beta|49|465|271|194|0.040245775729646695|0.08049155145929343|0.8920189098998887|0.8367346938775511|0.06007753929680936|
|org.apache.commons.text.beta.translate|15|56|6|50|0.22976190476190475|0.45952380952380945|0.951948051948052|1.0|0.4374427952999381|
|org.apache.commons.text.beta.similarity|16|105|83|22|0.07678571428571429|0.15357142857142858|0.7978021978021979|0.8125|0.09954719387755104|
|org.apache.commons.text.beta.diff|7|5|0|5|0.9142857142857143|0.17142857142857149|0.6|0.2857142857142857|0.029387755102040822|

The DDU of `commons-text` is low using when computed using the class-granularity, namely `0.0600`.

For the package `org.apache.commons.text.beta`, i.e. the complete codebase, it is difficult to achieve a balanced density because unit tests easily result in a sparse activity matrix.
This effect becomes more apparent when the number of components increases.

`org.apache.text.beta.translate` is tested by 6 unit tests and 50 integration tests.
Interestingly, although the integration tests cover similar components, the diversity is still _high_.
Assuming that the 20 integration tests have the same activity, and that the remaining tests have dissimilar activities.
The Gini-Simpson index is computed as follows.
```
diversity = 1 - (20 * 19) / (56 * 55) = 0.876
```
This also explains why the diversity of `org.apache.commons.text.beta.diff` isn't that _low_ either.
Due to the fact that each test is covered by at least one unit test and a couple of integration tests, component ambiguity is not present, thus a uniqueness of `1`.

The density of `org.apache.commons.text.beta.similarity` is low for two reasons; (1) the number of components is _high_, and (2) many test cases are unit tests.
This results in a sparse matrix.
The more components a package contains, the more difficult it is to get a balanced density of `0.5`.
Diversity is a forgiving metric but is relative lower than the other packages.
The reason for this is that each class is covered by multiple unit tests, and therefore the activity matrix has _many_ test executions with identical activity.
Although the diversity and uniqueness are _okay_, the DDU is still low due to the low normalized density.

The DDU for `org.apache.commons.text.beta.diff` is low because every test, that covers the components of this package, covers almost all components.
In other words, the tests written for this package are all integration tests, covering most components.
This results in no test diversity and components ambiguity groups, i.e. low diversity and low uniqueness.


### Method-package granularity

|parent|number_of_components|number_of_tests|unit_tests|integration_tests|density|normalized_density|diversity|uniqueness|ddu|
|---|---|---|---|---|---|---|---|---|---|
|org.apache.commons.text.beta|537|464|37|427|0.0230767995890323|0.04615359917806461|0.9916213599463767|0.6759776536312849|0.030937398149653968|
|org.apache.commons.text.beta.similarity|60|105|29|76|0.04523809523809524|0.09047619047619049|0.854029304029304|0.5333333333333333|0.04121030292458864|
|org.apache.commons.text.beta.translate|57|56|4|52|0.10432330827067669|0.2086466165413534|0.974025974025974|0.7719298245614035|0.15687715529425067|
|org.apache.commons.text.beta.diff|28|5|0|5|0.7857142857142857|0.4285714285714286|0.9|0.17857142857142858|0.06887755102040817|


Similar to the class-granularity explanation, `org.apache.commons.text.beta.diff` has a high density due to integration tests but slightly lower because there are more components to cover.
This results in test executions to have more variety in activity and thus a higher diversity.
I expected that the uniqueness at method-granularity would be higher.
A possible reason for the low uniqueness could be that certain methods are likely to be executed together and therefore resulting in identical columns in the activity matrix.
**This needs to be examined more thoroughly.**

`org.apache.commons.text.beta.similarity` consisted mostly of unit tests and therefore suffers from sparseness of the activity matrix.
The components have increased and thus the impact of unit tests on the sparseness of the activity matrix becomes more apparent.
Compared to the class granularity, test diversity has improved as there are more components to cover.
Though, we still observe that it is relatively lower than the other packages; probably due to the same reason as mentioned before for class granularity.
The uniqueness is low compared to class granularity for this package. This means that certain methods are always executed together.

We observe similar consequences for `org.apache.commons.text.beta.translate`, mainly due to the increase in number of components.

### Method-class granularity

|parent|number_of_components|number_of_tests|unit_tests|integration_tests|density|normalized_density|diversity|uniqueness|ddu|
|---|---|---|---|---|---|---|---|---|---|
|org.apache.commons.text.beta.AlphabetConverter|14|12|0|12|0.5595238095238095|0.8809523809523809|0.8484848484848485|0.5714285714285714|0.42712842712842713|
|org.apache.commons.text.beta.CharacterPredicates|4|1|0|1|0.5|1.0|0|0.5|0.0|
|org.apache.commons.text.beta.CompositeFormat|6|2|0|2|0.75|0.5|1.0|0.5|0.25|
|org.apache.commons.text.beta.diff.DeleteCommand|2|5|2|3|0.8|0.3999999999999999|0.6|1.0|0.23999999999999994|
|org.apache.commons.text.beta.diff.EditCommand|2|5|2|3|0.8|0.3999999999999999|0.6|1.0|0.23999999999999994|
|org.apache.commons.text.beta.diff.EditScript|7|5|0|5|0.7142857142857143|0.5714285714285714|0.7|0.5714285714285714|0.22857142857142854|
|org.apache.commons.text.beta.diff.InsertCommand|2|5|2|3|0.8|0.3999999999999999|0.6|1.0|0.23999999999999994|
|org.apache.commons.text.beta.diff.KeepCommand|2|5|2|3|0.8|0.3999999999999999|0.6|1.0|0.23999999999999994|
|org.apache.commons.text.beta.diff.ReplacementsFinder|4|2|0|2|1.0|0.0|0.0|0.25|0.0|
|org.apache.commons.text.beta.diff.StringsComparator|9|5|0|5|1.0|0.0|0.0|0.1111111111111111|0.0|
|org.apache.commons.text.beta.ExtendedMessageFormat|21|14|0|14|0.3741496598639456|0.7482993197278912|0.9560439560439561|0.6190476190476191|0.44287102596140504|
|org.apache.commons.text.beta.FormattableUtils|6|7|3|4|0.2619047619047619|0.5238095238095238|0.9523809523809523|1.0|0.4988662131519274|
|org.apache.commons.text.beta.similarity.CosineDistance|2|1|1|0|0.5|1.0|0|1.0|0.0|
|org.apache.commons.text.beta.similarity.CosineSimilarity|4|1|0|1|0.75|0.5|0|0.5|0.0|
|org.apache.commons.text.beta.similarity.Counter|2|1|1|0|0.5|1.0|0|1.0|0.0|
|org.apache.commons.text.beta.similarity.EditDistanceFrom|4|13|1|12|0.4807692307692308|0.9615384615384616|0.15384615384615385|0.75|0.11094674556213019|
|org.apache.commons.text.beta.similarity.FuzzyScore|3|5|5|0|0.3333333333333333|0.6666666666666666|0.4|1.0|0.26666666666666666|
|org.apache.commons.text.beta.similarity.HammingDistance|2|6|6|0|0.5|1.0|0.0|1.0|0.0|
|org.apache.commons.text.beta.similarity.JaccardDistance|2|4|4|0|0.5|1.0|0.0|1.0|0.0|
|org.apache.commons.text.beta.similarity.JaccardSimilarity|3|5|3|2|0.4666666666666667|0.9333333333333333|0.6|1.0|0.5599999999999999|
|org.apache.commons.text.beta.similarity.JaroWinklerDistance|3|7|3|4|0.5238095238095238|0.9523809523809523|0.5714285714285714|1.0|0.5442176870748299|
|org.apache.commons.text.beta.similarity.LevenshteinDetailedDistance|8|10|1|9|0.3875|0.775|0.8|0.875|0.5425000000000001|
|org.apache.commons.text.beta.similarity.LevenshteinDistance|7|53|1|52|0.39892183288409705|0.7978436657681941|0.4390420899854862|0.8571428571428571|0.3002459575718997|
|org.apache.commons.text.beta.similarity.LevenshteinResults|8|5|0|5|0.4|0.8|0.9|0.625|0.45000000000000007|
|org.apache.commons.text.beta.similarity.LongestCommonSubsequence|6|12|9|3|0.25|0.5|0.8636363636363636|0.8333333333333334|0.35984848484848486|
|org.apache.commons.text.beta.similarity.LongestCommonSubsequenceDistance|2|4|4|0|0.5|1.0|0.0|1.0|0.0|
|org.apache.commons.text.beta.similarity.RegexTokenizer|2|1|1|0|0.5|1.0|0|1.0|0.0|
|org.apache.commons.text.beta.similarity.SimilarityScoreFrom|4|4|0|4|0.5|1.0|0.0|0.5|0.0|
|org.apache.commons.text.beta.StrBuilder|166|230|0|230|0.05502881089575694|0.1100576217915139|0.9680653123220049|0.8072289156626506|0.08600456292617197|
|org.apache.commons.text.beta.StringEscapeUtils|27|27|18|9|0.05486968449931413|0.10973936899862824|0.9658119658119658|0.6666666666666666|0.07065839713301988|
|org.apache.commons.text.beta.StrLookup|7|41|0|41|0.5331010452961672|0.9337979094076656|0.4536585365853658|0.8571428571428571|0.3631074797557333|
|org.apache.commons.text.beta.StrMatcher|20|128|5|123|0.208984375|0.41796875|0.9190452755905512|0.95|0.3649255947803888|
|org.apache.commons.text.beta.StrSubstitutor|55|41|0|41|0.4270509977827051|0.8541019955654102|0.9158536585365854|0.6181818181818182|0.4835618703939509|
|org.apache.commons.text.beta.StrTokenizer|66|59|0|59|0.25783256291730866|0.5156651258346173|0.9877264757451782|0.7121212121212122|0.3627090390613646|
|org.apache.commons.text.beta.translate.AggregateTranslator|2|24|21|3|0.5625|0.875|0.3007246376811594|1.0|0.2631340579710145|
|org.apache.commons.text.beta.translate.CharSequenceTranslator|5|51|5|46|0.4666666666666667|0.9333333333333333|0.6486274509803922|1.0|0.6053856209150328|
|org.apache.commons.text.beta.translate.CodePointTranslator|2|21|11|10|0.7380952380952381|0.5238095238095237|0.6095238095238096|1.0|0.31927437641723355|
|org.apache.commons.text.beta.translate.CsvTranslators|4|5|1|4|0.65|0.7|0.4|0.5|0.13999999999999999|
|org.apache.commons.text.beta.translate.EntityArrays|2|2|2|0|0.5|1.0|1.0|1.0|1.0|
|org.apache.commons.text.beta.translate.JavaUnicodeEscaper|6|7|2|5|0.38095238095238093|0.7619047619047619|0.9523809523809523|1.0|0.7256235827664398|
|org.apache.commons.text.beta.translate.LookupTranslator|2|25|22|3|0.56|0.8799999999999999|0.29000000000000004|1.0|0.2552|
|org.apache.commons.text.beta.translate.NumericEntityEscaper|7|7|2|5|0.3673469387755102|0.7346938775510204|0.9523809523809523|1.0|0.6997084548104956|
|org.apache.commons.text.beta.translate.NumericEntityUnescaper|6|12|7|5|0.2638888888888889|0.5277777777777778|0.6666666666666667|0.8333333333333334|0.29320987654320996|
|org.apache.commons.text.beta.translate.OctalUnescaper|4|4|1|3|0.5625|0.875|0.8333333333333334|0.75|0.546875|
|org.apache.commons.text.beta.translate.SingleLookupTranslator|2|2|1|1|0.75|0.5|1.0|1.0|0.5|
|org.apache.commons.text.beta.translate.SinglePassTranslator|3|7|6|1|0.38095238095238093|0.7619047619047619|0.5238095238095238|1.0|0.39909297052154197|
|org.apache.commons.text.beta.translate.UnicodeEscaper|8|15|9|6|0.21666666666666667|0.43333333333333335|0.7619047619047619|0.875|0.28888888888888886|
|org.apache.commons.text.beta.translate.UnicodeUnescaper|2|6|3|3|0.75|0.5|0.7333333333333334|1.0|0.3666666666666667|
|org.apache.commons.text.beta.translate.UnicodeUnpairedSurrogateRemover|2|5|5|0|0.5|1.0|0.4|1.0|0.4|


`org.apache.commons.text.beta.translate.JavaUnicodeEscaper` has a DDU value of `0.7256`; the highest DDU value of all classes.
Yet, this class has a line coverage of `88%`, while most classes have `100%` line coverage.
Why does this class have a good DDU value?
Interestingly enough, this class is tested mostly by integration tests that do *not* cover all methods.
Besides this, couple of its methods are involved in larger integration tests.
Other example classes that have a DDU higher than `0.5` are: `org.apache.commons.text.beta.translate.NumericEntityEscaper`, `org.apache.commons.text.beta.translate.CharSequenceTranslator`, `org.apache.commons.text.beta.translate.OctalUnescaper`, `org.apache.commons.text.beta.similarity.JaccardSimilarity`.
`org.apache.commons.text.beta.translate.CharSequenceTranslator` has a high density but suffers from low diversity.
We observe a large number of tests that have similar activities.
The uniqueness is high as there is no component ambiguity.
The reason for an optimal uniqueness is that the ratio between number of tests and number of methods is large, and thus component ambiguity is less likely.


## Observations

- Uniqueness can possibly find components that are always executed together.
- A high density becomes more difficult to obtain, the higher the number of components.
- Diversity is a forgiving metric.
