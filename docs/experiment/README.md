# Experiment

The goal of this experiment is to verify that DDU does indeed result in a better fault diagnosis.


## Approach

1. Select activity matrices with varying DDU values.
1. For each matrix:
    1. Generate multiple candidate sets with a particular cardinality.
    1. For each candidate set:
        1. Generate modify error vector where health probability equals `0`.
        1. Generate activity matrix for Barinel.
        1. Compute effort.
    1. Average effort.

To compare the wasted effort among different scenarios, we select classes with particular values for the individual terms; low and high.
The scenarios of interest:

- `goodness = 0`
    - Low: density, diversity, uniqueness (DDU)

        class|normalized_density|diversity|uniqueness|ddu
        ---|---|---|---|---
        com.google.inject.internal.ConstructorInjectorStore|0.3297746144721234|0.02119979664463645|0.3333333333333333|0.0023303849217908
        com.google.inject.spi.InterceptorBinding|0.30666666666666664|0.15333333333333332|0.3333333333333333|0.01567407407407407

    - High: density, diversity, uniqueness (DDU)

        class|normalized_density|diversity|uniqueness|ddu
        ---|---|---|---|---
        com.google.inject.internal.Scoping|0.9174501261178629|0.911087828317497|0.9285714285714286|0.7761720970661705
        com.google.inject.spi.TypeConverterBinding|0.9666666666666667|0.8222222222222222|0.8333333333333334|0.6623456790123456
        com.google.inject.TypeLiteral|0.8920430107526882|0.9297090939401517|0.9444444444444444|0.7832660271001641
        org.apache.commons.csv.ExtendedBufferedReader|0.9313131313131313|0.9164303586321935|1.0|0.853483626928164
        org.jsoup.safety.Whitelist|0.9266862170087976|0.9526881720430107|0.9090909090909091|0.8025845437632401

    - Low: density, high: diversity, uniqueness

        class|normalized_density|diversity|uniqueness|ddu
        ---|---|---|---|---
        com.google.inject.AbstractModule|0.24961119751166405|0.8713875282820501|1.0|0.21750808443121156
        com.google.inject.internal.BindingBuilder|0.32384879725085913|0.8654511374286444|0.9333333333333333|0.2615902892732775
        org.apache.commons.text.beta.StrBuilder|0.09023081052066562|0.9675716726789444|0.8024691358024691|0.07005938835892254
        org.apache.commons.text.beta.StringEscapeUtils|0.11538461538461542|0.963076923076923|0.7083333333333334|0.07871301775147932

    - Low diversity, high: density, uniqueness

        class|normalized_density|diversity|uniqueness|ddu
        ---|---|---|---|---
        com.google.inject.internal.PrivateElementProcessor|0.9317803660565724|0.12734331669439825|1.0|0.11865600224436443
        org.jsoup.parser.ParseSettings|0.717357910906298|0.14509211268505018|1.0|0.10408297484472877
        org.apache.commons.text.beta.translate.CharSequenceTranslator|0.9895833333333334|0.19769503546099287|1.0|0.19563571217494088

    - Low uniqueness, high: density, diversity

        >Note: a uniqueness lower than `0.3` is rare.

        class|normalized_density|diversity|uniqueness|ddu
        ---|---|---|---|---
        com.google.inject.internal.State|0.47167763871807855|0.675363283416528|0.2608695652173913|0.08310098055620775

    - Low: diversity, uniqueness, high: density

        class|normalized_density|diversity|uniqueness|ddu
        ---|---|---|---|---
        com.google.inject.internal.ProviderMethodsModule|0.717149705818261|0.2654611938199425|0.38461538461538464|0.07322131425159081

    - Low: density, uniqueness, high: diversity

        class|normalized_density|diversity|uniqueness|ddu
        ---|---|---|---|---
        com.google.inject.PrivateModule|0.24761904761904763|0.8554621848739495|0.3333333333333333|0.07060957716419901

    - Low: density, diversity, high: uniqueness

        class|normalized_density|diversity|uniqueness|ddu
        ---|---|---|---|---
        com.google.inject.matcher.Matchers|0.22886762360446578|0.2574865860556125|0.8|0.047144274448459846

- `goodness != 0`