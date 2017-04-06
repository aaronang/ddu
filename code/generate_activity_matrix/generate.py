import os

from src.activity_generator import ActivityGenerator
from src.spectra import Spectra
from src.util import to_str

filenames = [
    'com.google.inject.internal.ConstructorInjectorStore',
    'com.google.inject.spi.InterceptorBinding',
    'com.google.inject.internal.Scoping',
    'com.google.inject.spi.TypeConverterBinding',
    'com.google.inject.TypeLiteral',
    'org.apache.commons.csv.ExtendedBufferedReader',
    'org.jsoup.safety.Whitelist',
    'com.google.inject.AbstractModule',
    'com.google.inject.internal.BindingBuilder',
    'org.apache.commons.text.beta.StrBuilder',
    'org.apache.commons.text.beta.StringEscapeUtils',
    'com.google.inject.internal.PrivateElementProcessor',
    'org.apache.commons.text.beta.translate.CharSequenceTranslator',
    'org.jsoup.parser.ParseSettings',
    'com.google.inject.internal.State',
    'com.google.inject.internal.ProviderMethodsModule',
    'com.google.inject.PrivateModule',
    'com.google.inject.matcher.Matchers'
]

for filename in filenames:
    print(filename)
    spectra = Spectra('resources/spectra/%s' % filename)
    activity_generator = ActivityGenerator(spectra)

    output = 'out/matrices/%s' % filename
    if not os.path.exists(output):
        os.makedirs(output)

    faulties = []

    while len(faulties) < 1:
        activity_matrix, faulty_set = activity_generator.generate(2)
        faulty_set.sort()
        h = hash(frozenset(faulty_set))
        if h not in faulties:
            faulties.append(h)
            name = '_'.join(to_str(faulty_set))
            with open('out/matrices/%s/%s.txt' % (filename, name), 'w') as f:
                for column in activity_matrix:
                    f.write(' '.join(to_str(column)))
                    f.write('\n')
