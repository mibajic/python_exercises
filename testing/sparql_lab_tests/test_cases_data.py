test_cases_dict_correct_queries_checker = {
    1: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/some-data",
        'ASK { \n'
        '[] ?p [] . \n'
        '}'],

    2: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/one-triple",
        'SELECT * \n'
        'WHERE { \n'
        '?s ?p ?o . \n'
        '} LIMIT 1 '],

    3: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/some-named-graphs",
        'ASK \n'
        'WHERE { \n'
        'GRAPH ?g { \n'
        '[] ?p [] . \n'
        '} \n'
        '}'],

    4: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/classes",
        'SELECT DISTINCT ?class \n'
        'WHERE { \n'
        '[] a ?class . \n'
        '}'],

    5: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/count-triples",
        'SELECT (COUNT(*) as ?count) \n'
        'WHERE { \n'
        '?s ?p ?o . \n'
        '}'],

    6: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/properties",
        'SELECT DISTINCT ?p \n'
        'WHERE { \n'
        '[] ?p [] . \n'
        '} '],

    7: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/describe-orphan-pension",
        'DESCRIBE <https://data.cssz.cz/resource/pension-kind/PK_D>'],

    8: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/one-quad",
        'SELECT * \n'
        'WHERE { \n'
        'GRAPH ?g { \n'
        '?s ?p ?o . \n'
        '} \n'
        '} \n'
        'LIMIT 1'],

    9: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/named-graphs",
        'SELECT DISTINCT ?g \n'
        'WHERE { \n'
        'GRAPH ?g { \n'
        '?s ?p ?o . \n'
        '} \n'
        '}'],

    10: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/classes-histogram",
         'SELECT ?class (COUNT(?s) AS ?count) \n'
         'WHERE { \n'
         '?s a ?class . \n'
         '} \n'
         'GROUP BY ?class \n'
         'ORDER BY DESC(?count)'],

    11: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/properties-histogram",
         'SELECT ?p (COUNT(*) as ?count) \n'
         'WHERE { \n'
         '[] ?p [] . \n'
         '} \n'
         'GROUP BY ?p \n'
         'ORDER BY DESC( ?count)'],

    12: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/dataset-equals-named-graph",
         'PREFIX qb: <http://purl.org/linked-data/cube#> '
         'ASK \n'
         'WHERE { \n'
         'GRAPH ?d { \n'
         '?d a qb:DataSet . \n'
         '} \n'
         '}'],

    13: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/understanding-from",
         'SELECT (COUNT(*) AS ?count) \n'
         'FROM <https://data.cssz.cz/resource/dataset/rocenka/vocabulary> \n'
         'WHERE { \n'
         '?s ?p ?o . \n'
         '}'],

    14: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/describe-dimensions",
         'PREFIX qb: <http://purl.org/linked-data/cube#> \n'
         'DESCRIBE ?dimension \n'
         'WHERE { \n'
         '?dimension a qb:DimensionProperty . \n'
         '}'],

    15: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/graph-sizes",
         'SELECT ?g (COUNT(*) as ?count) \n'
         'WHERE { \n'
         'GRAPH ?g { \n'
         '[] ?p [] . \n'
         '} \n'
         '} \n'
         'GROUP BY ?g \n'
         'ORDER BY DESC(?count)'],

    16: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/understanding-graph",
         'SELECT (COUNT(*) AS ?COUNT) \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/rocenka/vocabulary> { \n'
         '[] ?p [] . \n'
         '} \n'
         '}'],

    17: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/understanding-from-named",
         'SELECT (COUNT(*) AS ?count) \n'
         'FROM NAMED <https://data.cssz.cz/resource/dataset/rocenka/vocabulary> \n'
         'WHERE { \n'
         'GRAPH ?g { \n'
         '[] ?p [] . \n'
         '} \n'
         '} '],

    18: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/count-distinct-classes",
         'SELECT (COUNT(DISTINCT ?class) AS ?count) \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '[] a ?class . \n'
         '} \n'
         '}'],

    19: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/classes-histogram-code-lists",
         'SELECT ?class (COUNT(?s) AS ?count) \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?s a ?class . \n'
         '} \n'
         '} \n'
         'GROUP BY ?class \n'
         'ORDER BY DESC(?count)'],

    20: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/disjoint-concept-and-concept-scheme",
         'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n'
         'ASK \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?s a skos:Concept, skos:ConceptScheme . \n'
         '} \n'
         '}'],

    21: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/properties-histogram-code-lists",
         'SELECT ?property (COUNT(*) AS ?count) \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '[] ?property [] . \n'
         '} \n'
         '} \n'
         'GROUP BY ?property \n'
         'ORDER BY DESC(?count)'],

    22: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/classes-histogram-data",
         'SELECT ?class (COUNT(?s) AS ?count) \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '?s a ?class . \n'
         '} \n'
         '} \n'
         'GROUP BY ?class \n'
         'ORDER BY DESC(?count)'],

    23: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/most-common-class-data",
         'SELECT ?class (COUNT(?s) AS ?count) \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '?s a ?class . \n'
         '} \n'
         '} \n'
         'GROUP BY ?class \n'
         'ORDER BY DESC(?count) \n'
         'LIMIT 1'],

    24: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/classes-histogram-metadata",
         'SELECT ?class (COUNT(?s) AS ?count) \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech/metadata> { \n'
         '?s a ?class . \n'
         '} \n'
         '} \n'
         'GROUP BY ?class \n'
         'ORDER BY DESC(?count)'],

    25: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/count-districts",
         'PREFIX ruian: <https://data.cssz.cz/ontology/ruian/> \n'
         'SELECT (COUNT(?okres) AS ?count) \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?okres a ruian:Okres . \n'
         '} \n'
         '}'],

    26: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/datasets",
         'PREFIX qb: <http://purl.org/linked-data/cube#> \n'
         'SELECT DISTINCT ?dataset \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '?dataset a qb:DataSet . \n'
         '} \n'
         '} '],

    27: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/properties-histogram-data",
         'SELECT ?property (COUNT(*) AS ?count) \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '[] ?property [] . \n'
         '} \n'
         '} \n'
         'GROUP BY ?property \n'
         'ORDER BY DESC(?count)'],

    28: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/reflexive-exact-match",
         'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n'
         'SELECT DISTINCT ?concept \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?concept skos:exactMatch ?concept . \n'
         '} \n'
         '}'],

    29: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/properties-histogram-metadata",
         'SELECT ?property (COUNT(*) AS ?count) \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech/metadata> { \n'
         '[] ?property [] . \n'
         '} \n'
         '} \n'
         'GROUP BY ?property \n'
         'ORDER BY DESC(?count)'],

    30: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/datatypes",
         'SELECT ?datatype (COUNT(*) AS ?count) \n'
         'WHERE { \n'
         '[] ?p ?literal . \n'
         'FILTER (isLiteral(?literal) && datatype(?literal) != "") \n'
         'BIND (datatype(?literal) AS ?datatype) \n } '
         'GROUP BY ?datatype \n'
         'ORDER BY DESC(?count)'],

    31: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/count-datasets",
         'PREFIX qb: <http://purl.org/linked-data/cube#> \n'
         'SELECT (COUNT(DISTINCT ?dataSet) AS ?count) \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '?dataSet a qb:DataSet . \n'
         '} \n'
         '}'],

    32: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/properties-qb-observation-data",
         'PREFIX qb: <http://purl.org/linked-data/cube#> \n'
         'SELECT DISTINCT ?property \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '[] a qb:Observation ; \n'
         '?property [] . \n'
         '} \n'
         '}'],

    33: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/component-property-subproperties",
         'PREFIX qb:   <http://purl.org/linked-data/cube#> \n'
         'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n'
         'SELECT ?property \n'
         'WHERE { \n'
         'GRAPH <http://purl.org/linked-data/cube> { \n'
         '?property rdfs:subPropertyOf qb:componentProperty . \n'
         '} \n'
         '}'],

    34: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/data-structure-definition",
         'PREFIX qb: <http://purl.org/linked-data/cube#> \n'
         'SELECT ?dsd \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '<https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> \n'
         'qb:structure ?dsd . \n'
         '} \n'
         '}'],

    35: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/czech-county-labels",
         'PREFIX ruian: <https://data.cssz.cz/ontology/ruian/> \n'
         'PREFIX skos:  <http://www.w3.org/2004/02/skos/core#> \n'
         'SELECT DISTINCT ?label \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '[] a ruian:Okres ; \n'
         'skos:prefLabel ?label . \n'
         '} \n'
         '}'],

    36: [
        "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/collection-disjoint-with-concept-and-concept"
        "-scheme",
        'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n'
        'ASK \n'
        'WHERE { \n'
        'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
        'VALUES ?disjointClass { \n'
        'skos:Concept \n'
        'skos:ConceptScheme \n'
        '} \n'
        '?collection a skos:Collection, ?disjointClass . \n'
        '} \n'
        '}'],

    37: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/label-without-language",
         'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n'
         'ASK \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         'VALUES ?labelProperty { \n'
         'skos:prefLabel \n'
         'skos:altLabel \n'
         'skos:hiddenLabel \n'
         '} \n'
         '[] ?labelProperty ?label . \n'
         'FILTER (lang(?label) = "") \n'
         '} \n'
         '}'],

    38: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/empty-labels",
         'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n'
         'ASK \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         'VALUES ?labelProperty { \n'
         'skos:prefLabel \n'
         'skos:altLabel \n'
         'skos:hiddenLabel \n'
         '} \n'
         '[] ?labelProperty ?label . \n'
         'FILTER (STRLEN(?label) = 0) \n'
         '} \n'
         '}  '],

    39: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/pairwise-disjoint-skos-match-properties",
         'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n'
         'ASK \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         'VALUES ?disjointProperty { \n'
         'skos:broadMatch \n'
         'skos:narrowMatch \n'
         'skos:relatedMatch \n'
         '} \n'
         '?a skos:exactMatch ?b ; \n'
         '?disjointProperty ?b . \n'
         '} \n'
         '}'],

    40: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/old-age-pension-kinds",
         'PREFIX pension-kind: <https://data.cssz.cz/resource/pension-kind/> \n'
         'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n'
         'SELECT ?pensionKind \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?pensionKind skos:exactMatch pension-kind:PK_old_age_total_without_SR . \n'
         '} \n'
         '}'],

    41: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/pension-kind-schemes",
         'PREFIX pen-onto: <http://data.cssz.cz/ontology/pension-kinds/> \n'
         'PREFIX skos:  <http://www.w3.org/2004/02/skos/core#> \n'
         'SELECT DISTINCT ?pensionKindScheme \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '[] a pen-onto:PensionKind ; \n'
         'skos:inScheme ?pensionKindScheme . \n'
         '} \n'
         '}'],

    42: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/dataset-measures",
         'PREFIX qb:   <http://purl.org/linked-data/cube#> \n'
         'SELECT DISTINCT ?measure \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '<https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> \n'
         'qb:structure/qb:component/(qb:measure|qb:componentProperty) ?measure . \n'
         '?measure a qb:MeasureProperty . \n'
         '} \n'
         '}'],

    43: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/dataset-attributes",
         'PREFIX qb:   <http://purl.org/linked-data/cube#> \n'
         'SELECT ?attribute \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '<https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> \n'
         'qb:structure ?dsd . \n'
         '?dsd qb:component [ \n'
         '?property ?attribute \n'
         '] . \n'
         '?attribute a qb:AttributeProperty . \n'
         '} \n'
         '}'],

    44: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/dataset-dimensions",
         'PREFIX qb:   <http://purl.org/linked-data/cube#> \n'
         'SELECT DISTINCT ?dimension \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '<https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> \n'
         'qb:structure/qb:component/(qb:dimension|qb:componentProperty) ?dimension . \n'
         '} \n'
         '} '],

    45: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/pension-kind-with-most-children",
         'PREFIX pen-onto: <http://data.cssz.cz/ontology/pension-kinds/> \n'
         'PREFIX skos:     <http://www.w3.org/2004/02/skos/core#> \n'
         'SELECT ?pensionKind \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?pensionKind skos:inScheme pen-onto:PensionKindScheme_2008 ;'
         'skos:narrower ?child . \n'
         '} \n'
         '} \n'
         'GROUP BY ?pensionKind \n'
         'ORDER BY DESC(COUNT(?child)) \n'
         'LIMIT 1'],

    46: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/count-distinct-classes-without-distinct",
         'SELECT (COUNT(?class) AS ?count) \n'
         'WHERE { \n'
         '{ \n'
         'SELECT ?class \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '[] a ?class . \n'
         '} \n'
         '} \n'
         'GROUP BY ?class \n'
         '} \n'
         '}'],

    47: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/"
         "overlapping-associative-and-hierarchical-relations",
         'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n'
         'ASK \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?a skos:related ?b ; \n'
         'skos:broaderTransitive+|skos:narrowerTransitive+ ?b . \n'
         '} \n'
         '}'],

    48: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/object-property-path",
         'SELECT ?class1 ?p ?class2 (COUNT(*) AS ?count) \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '[ a ?class1 ] ?p [ a ?class2 ] . \n'
         '} \n'
         '} \n'
         'GROUP BY ?class1 ?p ?class2 \n'
         'ORDER BY DESC(?count)'],

    49: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/valueless-associative-relations",
         'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n'
         'ASK \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '[] skos:narrower ?a, ?b . \n'
         '{ \n'
         '?a skos:related ?b . \n'
         '} UNION { \n'
         '?b skos:related ?a . \n'
         '} \n'
         '} \n'
         '}'],

    50: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/cyclic-hierchical-relations",
         'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n'
         'ASK \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '{ \n'
         '?concept skos:broaderTransitive+ ?concept . \n'
         '} UNION { \n'
         '?concept skos:narrowerTransitive+ ?concept . \n'
         '} \n'
         '} \n'
         '}'],

    51: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/omitted-top-concepts",
         'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n'
         'ASK \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?conceptScheme a skos:ConceptScheme . \n'
         'FILTER NOT EXISTS { \n'
         '?conceptScheme skos:hasTopConcept|^skos:topConceptOf [] . \n'
         '} \n'
         '} \n'
         '}'],

    52: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/ambiguous-notation-references",
         'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n'
         'ASK \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?a skos:inScheme ?scheme ; \n'
         'skos:notation ?notation . \n'
         '?b skos:inScheme ?scheme ; \n'
         'skos:notation ?notation . \n'
         'FILTER (!sameTerm(?a, ?b)) \n'
         '} \n'
         '}'],

    53: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/count-pension-kinds",
         'PREFIX pen-onto: <http://data.cssz.cz/ontology/pension-kinds/> \n'
         'PREFIX skos:     <http://www.w3.org/2004/02/skos/core#> \n'
         'SELECT (COUNT(DISTINCT ?concept) AS ?count) \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?concept skos:inScheme pen-onto:PensionKindScheme_2008 . \n'
         '} \n'
         '}'],

    54: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/count-distinct-classes-with-reduced",
         'SELECT (COUNT(?class) AS ?count) \n'
         'WHERE { \n'
         '{ \n'
         'SELECT REDUCED ?class \n'
         'WHERE { \n'
         '{ \n'
         'SELECT ?class \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '[] a ?class . \n'
         '} \n'
         '} \n'
         'ORDER BY ?class \n'
         '} \n'
         '} \n'
         '} \n'
         '}'],

    55: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/unprintable-characters-in-labels",
         'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n'
         'ASK \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         'VALUES ?labelProperty { \n'
         'skos:prefLabel \n'
         'skos:altLabel \n'
         'skos:hiddenLabel \n'
         '} \n'
         '[] ?labelProperty ?label . \n'
         r'FILTER REGEX(?label, "^.*\\p{Zl}|\\p{Zp}|\\p{C}.*$")' '\n'
         '} \n'
         '}'],

    56: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/path-between-pension-kinds",
         'PREFIX pension-kind: <https://data.cssz.cz/resource/pension-kind/> \n'
         'PREFIX skos:          <http://www.w3.org/2004/02/skos/core#> \n'
         'SELECT ?member \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         'pension-kind:PK_total_without_special_pensions_2008 skos:narrower* ?member . \n'
         '?member skos:narrower* pension-kind:PK_S_2008 . \n'
         '} \n'
         '}'],

    57: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/multiple-pref-labels-per-language",
         'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n'
         'ASK \n'
         'WHERE { \n'
         '{ \n'
         'SELECT ?concept ?language \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?concept skos:prefLabel ?prefLabel . \n'
         'BIND (lang(?prefLabel) AS ?language) \n'
         '} \n'
         '} \n'
         'GROUP BY ?concept ?language \n'
         'HAVING (COUNT(?prefLabel) > 1) \n'
         '} \n'
         '}'],

    58: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/highest-pension",
         'PREFIX cssz-measure: <https://data.cssz.cz/ontology/measure/> \n'
         'CONSTRUCT { \n'
         '?observation ?p ?o . \n'
         '} \n'
         'FROM <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> '
         'WHERE { \n'
         '{ \n'
         'SELECT ?observation \n'
         'WHERE { \n'
         '?observation cssz-measure:prumerna-vyse-duchodu-v-kc ?pension . \n'
         '} \n'
         'ORDER BY DESC(?pension) \n'
         'LIMIT 1 \n'
         '} \n'
         '?observation ?p ?o . \n'
         '}'],

    59: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/ref-area-classes",
         'PREFIX cssz-dimension: <https://data.cssz.cz/ontology/dimension/> \n'
         'SELECT DISTINCT ?class \n'
         'WHERE { \n'
         '{ \n'
         'SELECT DISTINCT ?refArea \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '[] cssz-dimension:refArea ?refArea . \n'
         '} \n'
         '} \n'
         '} \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?refArea a ?class . \n'
         '} \n'
         '}'],

    60: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/pairwise-disjoint-skos-label-properties",
         'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n'
         'ASK \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '{ \n'
         '?concept skos:prefLabel ?label ; \n'
         'skos:altLabel ?label . \n'
         '} UNION { \n'
         '?concept skos:altLabel ?label ; \n'
         'skos:hiddenLabel ?label . \n'
         '} UNION { \n'
         '?concept skos:prefLabel ?label ; \n'
         'skos:hiddenLabel ?label . \n'
         '} \n'
         '} \n'
         '}'],

    61: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/pension-kind-with-most-descendants",
         'PREFIX pen-onto: <http://data.cssz.cz/ontology/pension-kinds/> \n'
         'PREFIX skos:     <http://www.w3.org/2004/02/skos/core#> \n'
         'SELECT ?pensionKind \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?pensionKind skos:inScheme pen-onto:PensionKindScheme_2008 ; \n'
         'skos:narrower+ ?descendant . \n'
         '} \n '
         '} \n'
         'GROUP BY ?pensionKind \n'
         'ORDER BY DESC(COUNT(DISTINCT ?descendant)) \n'
         'LIMIT 1'],

    62: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/concepts-in-multiple-schemes",
         'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n'
         'CONSTRUCT { \n'
         '?concept skos:inScheme ?conceptScheme . \n'
         '} \n'
         'FROM <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> \n'
         'WHERE { \n'
         '{ \n'
         'SELECT ?concept \n'
         'WHERE { \n'
         '?concept a skos:Concept ; \n'
         'skos:inScheme ?conceptScheme . \n'
         '} \n'
         'GROUP BY ?concept \n'
         'HAVING (COUNT(?conceptScheme) > 1) \n'
         '} \n'
         '?concept skos:inScheme ?conceptScheme . \n'
         '} '],

    63: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/dsd-has-normal-form",
         'PREFIX qb: <http://purl.org/linked-data/cube#> \n'
         'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n'
         'ASK \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '[] a qb:DataStructureDefinition ; \n'
         'qb:component ?component . \n'
         'FILTER NOT EXISTS { \n'
         '?component qb:componentAttachment ?componentAttachment . \n'
         'FILTER (!sameTerm(?componentAttachment, qb:Observation)) \n'
         '} \n'
         '} \n'
         '}'],

    64: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/is-pension-kinds-2008-polyhierarchical",
         'PREFIX pen-onto: <http://data.cssz.cz/ontology/pension-kinds/> \n'
         'PREFIX skos:     <http://www.w3.org/2004/02/skos/core#> \n'
         'ASK \n'
         'WHERE { \n'
         '{ \n'
         'SELECT ?concept \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?concept skos:inScheme pen-onto:PensionKindScheme_2008 . \n'
         '?broader skos:narrower ?concept . \n'
         '} \n'
         '} \n'
         'GROUP BY ?concept \n'
         'HAVING (COUNT(DISTINCT ?broader) > 1) \n'
         '} \n'
         '}'],

    65: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/hierarchical-code-lists",
         'PREFIX skos:    <http://www.w3.org/2004/02/skos/core#> \n'
         'SELECT DISTINCT ?conceptScheme \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         'VALUES ?hierarchicalProperty { \n'
         'skos:broader \n'
         'skos:broaderTransitive \n'
         'skos:narrower \n'
         'skos:narrowerTransitive \n'
         '} \n'
         '?conceptScheme a skos:ConceptScheme . \n'
         '[ skos:inScheme ?conceptScheme ] ?hierarchicalProperty [ skos:inScheme ?conceptScheme ] . \n'
         '} \n'
         '}'],

    66: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/dataset-component-labels-czech",
         'PREFIX qb:   <http://purl.org/linked-data/cube#> \n'
         'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n'
         'SELECT DISTINCT ?componentLabel \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '<https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> \n'
         'qb:structure ?dsd . \n'
         '?dsd qb:component ?component . \n'
         '?component rdfs:label ?componentLabel . \n'
         'FILTER langMatches(lang(?componentLabel), "cs") \n'
         'OPTIONAL { \n'
         '?component qb:order ?order . \n'
         '} \n'
         '} \n'
         '} \n'
         'ORDER BY ?order'],

    67: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/unidirectionally-related-concepts",
         'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n'
         'ASK \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         'VALUES (?property ?inverseProperty) { \n'
         '(skos:broader skos:narrower) \n'
         '(skos:broaderTransitive skos:narrowerTransitive) \n'
         '(skos:topConceptOf skos:hasTopConcept) \n'
         '} \n'
         '{ \n'
         '?a ?property ?b . \n'
         'FILTER NOT EXISTS { \n'
         '?b ?inverseProperty ?a . \n'
         '} \n'
         '} UNION { \n'
         '?a ?inverseProperty ?b . \n'
         'FILTER NOT EXISTS { \n'
         '?b ?property ?a . \n'
         '} \n'
         '} \n'
         '} \n'
         '}'],

    68: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/top-concept-has-no-broader-concept",
         'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n'
         'ASK \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?topConcept skos:topConceptOf|^skos:hasTopConcept ?scheme . \n'
         '{ \n'
         'VALUES ?broaderProperty { \n'
         'skos:broader \n'
         'skos:broaderTransitive \n'
         '} \n'
         '?topConcept ?broaderProperty ?broader . \n'
         '} UNION { \n'
         'VALUES ?narrowerProperty { \n'
         'skos:narrower \n'
         'skos:narrowerTransitive \n'
         '} \n'
         '?broader ?narrowerProperty ?topConcept . \n'
         '} \n'
         '?broader skos:inScheme ?scheme . \n'
         '} \n'
         '}'],

    69: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/vocabularies",
         'SELECT ?vocabulary (COUNT(*) AS ?count) \n'
         'WHERE { \n'
         '{ \n'
         'SELECT DISTINCT ?term \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '[] a ?term . \n'
         '} \n'
         '} \n'
         '} UNION { \n'
         'SELECT DISTINCT ?term \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '[] ?term [] . \n'
         '} \n'
         '} \n'
         '} \n'
         r'BIND (IRI(REPLACE(STR(?term), "^(.+)(#|\\/).+$", "$1")) AS ?vocabulary)' '\n'
         '} \n'
         'GROUP BY ?vocabulary \n'
         'ORDER BY DESC(?count)'],

    70: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/component-properties-with-most-specific-classes",
         'PREFIX qb:   <http://purl.org/linked-data/cube#> \n'
         'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n'
         'SELECT DISTINCT ?componentProperty ?class \n'
         'FROM <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> \n'
         'FROM <http://purl.org/linked-data/cube> \n'
         'WHERE { \n'
         '?property rdfs:subPropertyOf* qb:componentProperty . \n'
         '<https://data.cssz.cz/resource/data-structure-definition/duchodci-v-cr-krajich-okresech> qb:component [ \n'
         '?property ?componentProperty \n'
         '] . \n'
         'OPTIONAL { \n'
         '?componentProperty a ?class . \n'
         'FILTER NOT EXISTS { \n'
         '[] rdfs:subClassOf ?class . \n'
         '} \n'
         '} \n'
         '}'],

    71: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/dataset-component-properties-with-classes",
         'PREFIX qb:   <http://purl.org/linked-data/cube#> \n'
         'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n'
         'SELECT DISTINCT ?componentProperty ?class \n'
         'WHERE { \n'
         'GRAPH <http://purl.org/linked-data/cube> { \n'
         '?property rdfs:subPropertyOf qb:componentProperty . \n'
         '} \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '<https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> qb:structure ?dsd . \n'
         '?dsd qb:component [ \n'
         '?property ?componentProperty \n'
         '] . \n'
         'OPTIONAL { \n'
         '?componentProperty a ?class . \n'
         '} \n'
         '} \n'
         '}'],

    72: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/orphan-concepts",
         'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n'
         'ASK \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?concept a skos:Concept . \n'
         'FILTER NOT EXISTS { \n'
         '{ \n'
         'VALUES ?semanticRelation { \n'
         'skos:broader \n'
         'skos:narrower \n'
         'skos:related \n'
         'skos:broaderTransitive \n'
         'skos:narrowerTransitive \n'
         '} \n'
         '{ \n'
         '?concept ?semanticRelation [] . \n'
         '} UNION { \n'
         '[] ?semanticRelation ?concept . \n'
         '} \n'
         '} UNION { \n'
         '?concept skos:topConceptOf|^skos:hasTopConcept [] . \n'
         '} \n'
         '} \n'
         '} \n'
         '}'],

    73: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/is-multimeasure-dataset",
         'PREFIX qb:   <http://purl.org/linked-data/cube#> \n'
         'ASK \n'
         'WHERE { \n'
         '{ \n'
         'SELECT ?dsd \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '<https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> \n'
         'qb:structure ?dsd . \n'
         '?dsd qb:component ?component . \n'
         '{ \n'
         '?component qb:measure ?measureProperty . \n'
         '} UNION { \n'
         '?component qb:componentProperty ?measureProperty . \n'
         '?measureProperty a qb:MeasureProperty . \n'
         '} \n'
         '} \n'
         '} \n'
         'GROUP BY ?dsd \n'
         'HAVING (COUNT(DISTINCT ?measureProperty) > 1) \n'
         '} \n'
         '}'],

    74: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/ambiguous-notation-references-construct",
         'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n'
         'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n'
         'PREFIX spin: <http://spinrdf.org/spin#> \n'
         'CONSTRUCT { \n'
         '[] a spin:ConstraintViolation ; \n'
         'spin:violationRoot ?a, ?b ; \n'
         'spin:violationPath skos:notation ; \n'
         'spin:violationValue ?notation ; \n'
         'rdfs:comment "Concepts within the same concept scheme should not have identical '
         'skos:notation literals."@en ; \n'
         'rdfs:seeAlso <https://github.com/cmader/qSKOS/wiki/'
         'Quality-Issues#ambiguous-notation-references> . \n'
         '} \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?a skos:inScheme ?scheme ; \n'
         'skos:notation ?notation . \n'
         '?b skos:inScheme ?scheme ; \n'
         'skos:notation ?notation . \n'
         'FILTER (!sameTerm(?a, ?b)) \n'
         '} \n'
         '}'],

    75: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/greatest-range-of-pensions-between-areas",
         'PREFIX cssz-dimension: <https://data.cssz.cz/ontology/dimension/> \n'
         'PREFIX cssz-measure:   <https://data.cssz.cz/ontology/measure/> \n'
         'PREFIX pension-kind:   <https://data.cssz.cz/resource/pension-kind/> \n'
         'PREFIX skos:           <http://www.w3.org/2004/02/skos/core#> \n'
         'SELECT (MAX(?pension) - MIN(?pension) AS ?pensionRange) \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?pensionKind skos:exactMatch pension-kind:PK_old_age_total_without_SR . \n'
         '} \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '[] cssz-dimension:pohlavi ?gender ; \n'
         'cssz-dimension:druh-duchodu ?pensionKind ; \n'
         'cssz-dimension:refPeriod ?refPeriod ; \n'
         'cssz-measure:prumerna-vyse-duchodu-v-kc ?pension . \n'
         '} \n'
         '} \n'
         'GROUP BY ?gender ?refPeriod \n'
         'ORDER BY ?pensionRange \n'
         'LIMIT 1'],

    76: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/orphan-count-over-time",
         'PREFIX cssz-dimension: <https://data.cssz.cz/ontology/dimension/> \n'
         'PREFIX cssz-measure:   <https://data.cssz.cz/ontology/measure/> \n'
         'PREFIX pension-kind:   <https://data.cssz.cz/resource/pension-kind/> \n'
         'PREFIX qb:             <http://purl.org/linked-data/cube#> \n'
         'PREFIX skos:           <http://www.w3.org/2004/02/skos/core#> \n'
         'PREFIX xsd:            <http://www.w3.org/2001/XMLSchema#> \n'
         'SELECT DISTINCT ?year ?orphanCount \n'
         'FROM <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> \n'
         'FROM <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> \n'
         'WHERE { \n'
         '[] a qb:Observation ; \n'
         'cssz-dimension:druh-duchodu/skos:exactMatch pension-kind:PK_D ; \n'
         'cssz-dimension:pohlavi <https://data.cssz.cz/ontology/sdmx/code/sex-T> ; \n'
         'cssz-dimension:refArea <https://data.cssz.cz/resource/ruian/staty/1> ; \n'
         'cssz-dimension:refPeriod/skos:notation ?refPeriod ; \n'
         'cssz-measure:pocet-duchodcu ?orphanCount . \n'
         'BIND (year(strdt(?refPeriod, xsd:date)) AS ?year) \n'
         '} \n'
         'ORDER BY ?year'],

    77: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/average-pension-per-region",
         'PREFIX cssz-dimension: <https://data.cssz.cz/ontology/dimension/> \n'
         'PREFIX cssz-measure:   <https://data.cssz.cz/ontology/measure/> \n'
         'PREFIX day:            <https://data.cssz.cz/resource/reference.data.gov.uk/'
         'id/gregorian-day/> \n'
         'PREFIX pension-kind:   <https://data.cssz.cz/resource/pension-kind/> \n'
         'PREFIX ruian:          <https://data.cssz.cz/ontology/ruian/> \n'
         'PREFIX sdmx-code:      <http://purl.org/linked-data/sdmx/2009/code#> \n'
         'PREFIX skos:           <http://www.w3.org/2004/02/skos/core#> \n'
         'SELECT (AVG(?pension) AS ?avgPensionPerRegion) \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?pensionKind skos:exactMatch pension-kind:PK_old_age_total_without_SR . \n'
         '?refArea a ruian:Vusc . \n'
         '} \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '[] cssz-dimension:refPeriod day:2015-12-31 ; \n'
         'cssz-dimension:pohlavi sdmx-code:sex-T ; \n'
         'cssz-dimension:refArea ?refArea ; \n'
         'cssz-dimension:druh-duchodu ?pensionKind ; \n'
         'cssz-measure:prumerna-vyse-duchodu-v-kc ?pension . \n'
         '} \n'
         '}'],

    78: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/are-there-regions-with-women-older-than-men",
         'PREFIX cssz-dimension: <https://data.cssz.cz/ontology/dimension/> \n'
         'PREFIX cssz-measure:   <https://data.cssz.cz/ontology/measure/> \n'
         'PREFIX pension-kind:   <https://data.cssz.cz/resource/pension-kind/> \n'
         'PREFIX qb:             <http://purl.org/linked-data/cube#> \n'
         'PREFIX sdmx-code:      <http://purl.org/linked-data/sdmx/2009/code#> \n'
         'PREFIX skos:           <http://www.w3.org/2004/02/skos/core#> \n'
         'ASK \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?pensionKind skos:exactMatch pension-kind:PK_old_age_total_without_SR . \n'
         '} \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '[] cssz-dimension:pohlavi sdmx-code:sex-F ; \n'
         'cssz-dimension:druh-duchodu ?pensionKind ; \n'
         'cssz-dimension:refArea ?refArea ; \n'
         'cssz-dimension:refPeriod ?refPeriod ; \n'
         'cssz-measure:prumerny-vek ?averageAgeWomen . \n'
         '[] cssz-dimension:pohlavi sdmx-code:sex-M ; \n'
         'cssz-dimension:druh-duchodu ?pensionKind ; \n'
         'cssz-dimension:refArea ?refArea ; \n'
         'cssz-dimension:refPeriod ?refPeriod ; \n'
         'cssz-measure:prumerny-vek ?averageAgeMen . \n'
         'FILTER (?averageAgeWomen > ?averageAgeMen) \n'
         '} \n'
         '}'],

    79: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/pension-gap-in-regions-over-time",
         'PREFIX cssz-dimension: <https://data.cssz.cz/ontology/dimension/> \n'
         'PREFIX cssz-measure:   <https://data.cssz.cz/ontology/measure/> \n'
         'PREFIX day:            <https://data.cssz.cz/resource/reference.data.gov.uk/'
         'id/gregorian-day/> \n'
         'PREFIX pension-kind:   <https://data.cssz.cz/resource/pension-kind/> \n'
         'PREFIX ruian:          <https://data.cssz.cz/ontology/ruian/> \n'
         'PREFIX sdmx-code:      <http://purl.org/linked-data/sdmx/2009/code#> \n'
         'PREFIX skos:           <http://www.w3.org/2004/02/skos/core#> \n'
         'PREFIX xsd:            <http://www.w3.org/2001/XMLSchema#> \n'
         'SELECT ?refPeriod (MAX(?pension) - MIN(?pension) AS ?range) \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?pensionKind skos:exactMatch pension-kind:PK_old_age_total_without_SR . \n'
         '?refArea a ruian:Vusc . \n'
         '} \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '[] cssz-dimension:refPeriod ?refPeriod ; \n'
         'cssz-dimension:pohlavi sdmx-code:sex-T ; \n'
         'cssz-dimension:refArea ?refArea ; \n'
         'cssz-dimension:druh-duchodu ?pensionKind ; \n'
         'cssz-measure:prumerna-vyse-duchodu-v-kc ?pension . \n'
         '} \n'
         '} \n'
         'GROUP BY ?refPeriod \n'
         'ORDER BY DESC(?refPeriod)'],

    80: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/dsd-components",
         'PREFIX qb:   <http://purl.org/linked-data/cube#> \n'
         'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n'
         'SELECT ?componentProperty ?label ?componentAttachment ?componentRequired \n'
         'WHERE { \n'
         'GRAPH <http://purl.org/linked-data/cube> { \n'
         '?property rdfs:subPropertyOf* qb:componentProperty . \n'
         '} \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '<https://data.cssz.cz/resource/data-structure-definition/duchodci-v-cr-krajich-okresech> \n'
         'qb:component ?component . \n'
         '?component ?property ?componentProperty ; \n'
         'rdfs:label ?label . \n'
         'FILTER langMatches(lang(?label), "cs") \n'
         'OPTIONAL { \n'
         '?component qb:order ?order . \n'
         '} \n'
         'OPTIONAL { \n'
         '?component qb:componentAttachment ?_componentAttachment . \n'
         '} \n'
         'BIND (COALESCE(?_componentAttachment, qb:Observation) AS ?componentAttachment) \n'
         'OPTIONAL { \n'
         '?component qb:componentRequired ?_componentRequired . \n'
         '} \n'
         '{ \n'
         'FILTER (sameTerm(?property, qb:attribute) || EXISTS { ?componentProperty a '
         'qb:AttributeProperty . }) \n'
         'BIND (false AS ?defaultComponentRequired) \n'
         '} UNION { \n'
         'BIND (true AS ?defaultComponentRequired) \n'
         '} \n'
         'BIND (COALESCE(?_componentRequired, ?defaultComponentRequired) AS ?componentRequired) \n'
         '} \n'
         '} \n'
         'ORDER BY ?order'],

    81: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/pensions-rounded-to-thousands",
         'PREFIX cssz-dimension: <https://data.cssz.cz/ontology/dimension/>'
         'PREFIX cssz-measure:   <https://data.cssz.cz/ontology/measure/>'
         'PREFIX pension-kind:   <https://data.cssz.cz/resource/pension-kind/>'
         'PREFIX qb:             <http://purl.org/linked-data/cube#>'
         'PREFIX sdmx-code:      <http://purl.org/linked-data/sdmx/2009/code#>'
         'PREFIX skos:           <http://www.w3.org/2004/02/skos/core#>'
         'PREFIX xsd:            <http://www.w3.org/2001/XMLSchema#>'
         'SELECT DISTINCT (ROUND(?pension / ?factor) * ?factor AS ?roundedPension) ?year'
         'WHERE {'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> {'
         '?pensionKind skos:exactMatch pension-kind:PK_old_age_total_without_SR .'
         '}'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> {'
         '[] a qb:Observation ;'
         'qb:dataSet <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> ;'
         '    cssz-dimension:pohlavi sdmx-code:sex-T ;'
         '    cssz-dimension:refArea <https://data.cssz.cz/resource/ruian/staty/1> ;'
         '    cssz-dimension:refPeriod ?refPeriod ;'
         '    cssz-dimension:druh-duchodu ?pensionKind ;'
         '    cssz-measure:prumerna-vyse-duchodu-v-kc ?pension .'
         '}'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> {'
         '?refPeriod skos:notation ?date .'
         'BIND(YEAR(STRDT(?date, xsd:date)) AS ?year)'
         '}'
         'BIND (1000 AS ?factor)'
         '}'
         'ORDER BY ?year'],

    82: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/"
         "total-pension-cost-for-2015-per-prague-district",
         'PREFIX cssz-dimension: <https://data.cssz.cz/ontology/dimension/> \n'
         'PREFIX cssz-measure:   <https://data.cssz.cz/ontology/measure/> \n'
         'PREFIX day:            <https://data.cssz.cz/resource/reference.data.gov.uk/'
         'id/gregorian-day/> \n'
         'PREFIX pension-kind:   <https://data.cssz.cz/resource/pension-kind/> \n'
         'PREFIX ruian:          <https://data.cssz.cz/ontology/ruian/> \n'
         'PREFIX sdmx-code:      <http://purl.org/linked-data/sdmx/2009/code#> \n'
         'PREFIX skos:           <http://www.w3.org/2004/02/skos/core#> \n'
         'SELECT ?pragueDistrictLabel (round(?pension * ?retireeCount * 12 / 1000000) '
         'AS ?pensionYearCost) \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?pensionKind skos:exactMatch pension-kind:PK_old_age_total_without_SR . \n'
         '?pragueDistrict a ruian:SpravniObvod ; \n'
         'skos:prefLabel ?pragueDistrictLabel . \n'
         '} \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '[] cssz-dimension:refPeriod day:2015-12-31 ; \n'
         'cssz-dimension:pohlavi sdmx-code:sex-T ; \n'
         'cssz-dimension:druh-duchodu ?pensionKind ; \n'
         'cssz-dimension:refArea ?pragueDistrict ; \n'
         'cssz-measure:prumerna-vyse-duchodu-v-kc ?pension . \n'
         '[] cssz-dimension:refPeriod day:2015-12-31 ; \n'
         'cssz-dimension:pohlavi sdmx-code:sex-T ; \n'
         'cssz-dimension:druh-duchodu ?pensionKind ; \n'
         'cssz-dimension:refArea ?pragueDistrict ; \n'
         'cssz-measure:pocet-duchodcu ?retireeCount . \n'
         '} \n'
         '} \n'
         'ORDER BY DESC(?pensionYearCost)'],

    83: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/poorest-prague-districts-over-time",
         'PREFIX cssz-dimension: <https://data.cssz.cz/ontology/dimension/> \n'
         'PREFIX cssz-measure:   <https://data.cssz.cz/ontology/measure/> \n'
         'PREFIX pension-kind:   <https://data.cssz.cz/resource/pension-kind/> \n'
         'PREFIX ruian:          <https://data.cssz.cz/ontology/ruian/> \n'
         'PREFIX sdmx-code:      <http://purl.org/linked-data/sdmx/2009/code#> \n'
         'PREFIX skos:           <http://www.w3.org/2004/02/skos/core#> \n'
         'PREFIX xsd:            <http://www.w3.org/2001/XMLSchema#> \n'
         'SELECT ?date ?pragueDistrict ?lowestPension \n'
         'FROM <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> \n'
         'FROM <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> \n'
         'WHERE { \n'
         '?pensionKind skos:exactMatch pension-kind:PK_old_age_total_without_SR . \n'
         '[] cssz-dimension:pohlavi sdmx-code:sex-T ; \n'
         'cssz-dimension:druh-duchodu ?pensionKind ; \n'
         'cssz-dimension:refPeriod ?refPeriod ; \n'
         'cssz-dimension:refArea ?refArea1 ; \n'
         'cssz-measure:prumerna-vyse-duchodu-v-kc ?lowestPension . \n'
         '?refArea1 a ruian:SpravniObvod . \n'
         'FILTER NOT EXISTS { \n'
         '[] cssz-dimension:pohlavi sdmx-code:sex-T ; \n'
         'cssz-dimension:druh-duchodu ?pensionKind ; \n'
         'cssz-dimension:refPeriod ?refPeriod ; \n'
         'cssz-dimension:refArea ?refArea2 ; \n'
         'cssz-measure:prumerna-vyse-duchodu-v-kc ?evenLowerPension . \n'
         '?refArea2 a ruian:SpravniObvod . \n'
         'FILTER (!sameTerm(?refArea1, ?refArea2) && ?evenLowerPension < ?lowestPension) \n'
         '} \n'
         '?refPeriod skos:notation ?_date . \n'
         'BIND (strdt(?_date, xsd:date) AS ?date) \n'
         '?refArea1 skos:prefLabel ?pragueDistrict . \n'
         '} \n'
         'ORDER BY ?date'],

    84: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/greatest-increase-in-pensions-over-5-years",
         'PREFIX cssz-dimension: <https://data.cssz.cz/ontology/dimension/> \n'
         'PREFIX cssz-measure: <https://data.cssz.cz/ontology/measure/> \n'
         'PREFIX day: <https://data.cssz.cz/resource/reference.data.gov.uk/id/gregorian-day/> \n'
         'PREFIX pension-kind: <https://data.cssz.cz/resource/pension-kind/> \n'
         'PREFIX sdmx-code: <http://purl.org/linked-data/sdmx/2009/code#> \n'
         'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> \n'
         'SELECT ?refAreaLabel ?pensionKindLabel ?gender ?increase \n'
         'FROM <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> \n'
         'FROM <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> \n'
         'WHERE { \n'
         '{ \n'
         'SELECT ?refArea ?gender ?increase ?pensionKind \n'
         'WHERE { \n'
         'VALUES ?gender { \n'
         'sdmx-code:sex-F \n'
         'sdmx-code:sex-M \n'
         '} \n'
         '[] cssz-dimension:refPeriod day:2014-12-31 ; \n'
         'cssz-dimension:pohlavi ?gender ; \n'
         'cssz-dimension:refArea ?refArea ; \n'
         'cssz-dimension:druh-duchodu/skos:exactMatch ?pensionKind ; \n'
         'cssz-measure:prumerna-vyse-duchodu-v-kc ?endPension . \n'
         '[] cssz-dimension:refPeriod day:2009-12-31 ; \n'
         'cssz-dimension:pohlavi ?gender ; \n'
         'cssz-dimension:refArea ?refArea ; \n'
         'cssz-dimension:druh-duchodu/skos:exactMatch ?pensionKind ; \n'
         'cssz-measure:prumerna-vyse-duchodu-v-kc ?startPension . \n'
         'FILTER (?endPension > ?startPension) \n'
         'BIND ((?endPension - ?startPension)/?startPension AS ?increase) \n'
         '} \n'
         'ORDER BY DESC(?increase) \n'
         'LIMIT 10 \n'
         '} \n'
         '?refArea skos:prefLabel ?refAreaLabel . \n'
         '?pensionKind skos:prefLabel ?pensionKindLabel . \n'
         '} \n'
         'ORDER BY DESC(?increase)'],

    85: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/average-age-per-disability-level-and-year",
         'PREFIX cssz-dimension: <https://data.cssz.cz/ontology/dimension/> \n'
         'PREFIX cssz-measure:   <https://data.cssz.cz/ontology/measure/> \n'
         'PREFIX pension-kind:   <https://data.cssz.cz/resource/pension-kind/> \n'
         'PREFIX sdmx-code:      <http://purl.org/linked-data/sdmx/2009/code#> \n'
         'PREFIX skos:           <http://www.w3.org/2004/02/skos/core#> \n'
         'SELECT ?refPeriod ?avgAgeLevel1 ?avgAgeLevel2 ?avgAgeLevel3 \n'
         'WHERE { \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { \n'
         '?disabilityPensionLevel1 skos:exactMatch pension-kind:PK_IP . \n'
         '?disabilityPensionLevel2 skos:exactMatch pension-kind:PK_ID . \n'
         '?disabilityPensionLevel3 skos:exactMatch pension-kind:PK_IT . \n'
         '} \n'
         'GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { \n'
         '[] cssz-dimension:refPeriod ?refPeriod ; \n'
         'cssz-dimension:pohlavi sdmx-code:sex-T ; \n'
         'cssz-dimension:druh-duchodu ?disabilityPensionLevel1 ; \n'
         'cssz-dimension:refArea <https://data.cssz.cz/resource/ruian/staty/1> ; \n'
         'cssz-measure:prumerny-vek ?avgAgeLevel1 . \n'
         '[] cssz-dimension:refPeriod ?refPeriod ; \n'
         'cssz-dimension:pohlavi sdmx-code:sex-T ; \n'
         'cssz-dimension:druh-duchodu ?disabilityPensionLevel2 ; \n'
         'cssz-dimension:refArea <https://data.cssz.cz/resource/ruian/staty/1> ; \n'
         'cssz-measure:prumerny-vek ?avgAgeLevel2 . \n'
         '[] cssz-dimension:refPeriod ?refPeriod ; \n'
         'cssz-dimension:pohlavi sdmx-code:sex-T ; \n'
         'cssz-dimension:druh-duchodu ?disabilityPensionLevel3 ; \n'
         'cssz-dimension:refArea <https://data.cssz.cz/resource/ruian/staty/1> ; \n'
         'cssz-measure:prumerny-vek ?avgAgeLevel3 . \n'
         '} \n'
         '} \n'
         'ORDER BY DESC(?refPeriod)']
}

test_cases_dict_wrong_queries_checker = {
    1: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/some-data",

    2: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/one-triple",

    3: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/some-named-graphs",

    4: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/classes",

    5: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/count-triples",

    6: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/properties",

    7: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/describe-orphan-pension",

    8: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/one-quad",

    9: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/named-graphs",

    10: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/classes-histogram",

    11: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/properties-histogram",

    12: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/dataset-equals-named-graph",

    13: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/understanding-from",

    14: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/describe-dimensions",

    15: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/graph-sizes",

    16: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/understanding-graph",

    17: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/understanding-from-named",

    18: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/count-distinct-classes",

    19: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/classes-histogram-code-lists",

    20: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/disjoint-concept-and-concept-scheme",

    21: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/properties-histogram-code-lists",

    22: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/classes-histogram-data",

    23: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/most-common-class-data",

    24: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/classes-histogram-metadata",

    25: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/count-districts",

    26: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/datasets",

    27: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/properties-histogram-data",

    28: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/reflexive-exact-match",

    29: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/properties-histogram-metadata",

    30: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/datatypes",

    31: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/count-datasets",

    32: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/properties-qb-observation-data",

    33: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/component-property-subproperties",

    34: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/data-structure-definition",

    35: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/czech-county-labels",

    36: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/collection-disjoint-with-concept-and-concept-scheme",

    37: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/label-without-language",

    38: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/empty-labels",

    39: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/pairwise-disjoint-skos-match-properties",

    40: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/old-age-pension-kinds",

    41: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/pension-kind-schemes",

    42: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/dataset-measures",

    43: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/dataset-attributes",

    44: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/dataset-dimensions",

    46: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/count-distinct-classes-without-distinct",

    47: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/overlapping-associative-and-hierarchical-relations",

    48: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/object-property-path",

    49: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/valueless-associative-relations",

    50: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/cyclic-hierchical-relations",

    51: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/omitted-top-concepts",

    52: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/ambiguous-notation-references",

    53: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/count-pension-kinds",

    54: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/count-distinct-classes-with-reduced",

    55: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/unprintable-characters-in-labels",

    56: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/path-between-pension-kinds",

    57: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/multiple-pref-labels-per-language",

    58: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/highest-pension",

    59: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/ref-area-classes",

    60: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/pairwise-disjoint-skos-label-properties",

    62: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/concepts-in-multiple-schemes",

    63: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/dsd-has-normal-form",

    64: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/is-pension-kinds-2008-polyhierarchical",

    65: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/hierarchical-code-lists",

    66: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/dataset-component-labels-czech",

    67: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/unidirectionally-related-concepts",

    68: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/top-concept-has-no-broader-concept",

    69: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/vocabularies",

    72: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/orphan-concepts",

    73: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/is-multimeasure-dataset",

    74: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/ambiguous-notation-references-construct",

    75: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/greatest-range-of-pensions-between-areas",

    76: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/orphan-count-over-time",

    77: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/average-pension-per-region",

    78: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/are-there-regions-with-women-older-than-men",

    79: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/pension-gap-in-regions-over-time",

    80: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/dsd-components",

    82: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/total-pension-cost-for-2015-per-prague-district",

    83: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/poorest-prague-districts-over-time",

    84: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/greatest-increase-in-pensions-over-5-years",

    85: "https://doc.lmcloud.vse.cz/sparqlab/exercise/show/average-age-per-disability-level-and-year"
}
