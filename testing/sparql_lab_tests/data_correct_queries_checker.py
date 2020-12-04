test_cases_dict = {1: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/some-data",
                       'PREFIX qb: <http://purl.org/linked-data/cube#> '
                       '\n DESCRIBE ?dimension '
                       '\n WHERE { '
                       '\n   ?dimension a qb:DimensionProperty . '
                       '\n } '],

                   2: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/one-triple",
                       'SELECT * '
                       '\n WHERE { '
                       '\n  ?s ?p ?o . '
                       '\n } LIMIT 1 '],

                   3: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/some-named-graphs",
                       'ASK '
                       '\n WHERE { '
                       '\n GRAPH ?g { '
                       '\n  [] ?p [] . '
                       '\n   } '
                       '\n }'],

                   4: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/classes",
                       'SELECT DISTINCT ?class '
                       '\n WHERE { '
                       '\n  [] a ?class . '
                       '\n }'],

                   5: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/count-triples",
                       'SELECT (COUNT(*) as ?count) '
                       '\n WHERE { '
                       '\n  ?s ?p ?o . '
                       '\n }'],

                   6: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/properties",
                       'SELECT DISTINCT ?p '
                       '\n WHERE { '
                       '\n  [] ?p [] . '
                       '\n } '],

                   7: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/describe-orphan-pension",
                       'DESCRIBE <https://data.cssz.cz/resource/pension-kind/PK_D>'],

                   8: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/one-quad",
                       'SELECT * '
                       '\n WHERE { '
                       '\n  GRAPH ?g { '
                       '\n    ?s ?p ?o . '
                       '\n   } '
                       '\n } '
                       '\n LIMIT 1'],

                   9: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/named-graphs",
                       'SELECT DISTINCT ?g '
                       '\n WHERE { '
                       '\n  GRAPH ?g { '
                       '\n   ?s ?p ?o . '
                       '\n   } '
                       '\n }'],

                   10: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/classes-histogram",
                        'SELECT ?class (COUNT(?s) AS ?count) '
                        '\n WHERE { '
                        '\n  ?s a ?class . '
                        '\n  } '
                        '\n GROUP BY ?class '
                        '\n ORDER BY DESC(?count)'],

                   11: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/properties-histogram",
                        'SELECT ?p (COUNT(*) as ?count) '
                        '\n WHERE { '
                        '\n [] ?p [] . '
                        '\n   } '
                        '\n GROUP BY ?p '
                        '\n ORDER BY DESC( ?count)'],

                   12: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/dataset-equals-named-graph",
                        'PREFIX qb: <http://purl.org/linked-data/cube#> '
                        '\n ASK '
                        '\n WHERE { '
                        '\n   GRAPH ?d { '
                        '\n    ?d a qb:DataSet . '
                        '\n   } '
                        '\n }'],

                   13: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/understanding-from",
                        'SELECT (COUNT(*) AS ?count) '
                        '\n FROM <https://data.cssz.cz/resource/dataset/rocenka/vocabulary> '
                        '\n WHERE { '
                        '\n   ?s ?p ?o . '
                        '\n }'],

                   14: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/describe-dimensions",
                        'PREFIX qb: <http://purl.org/linked-data/cube#> '
                        '\n DESCRIBE ?dimension '
                        '\n WHERE { '
                        '\n   ?dimension a qb:DimensionProperty . '
                        '\n }'],

                   15: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/graph-sizes",
                        'SELECT ?g (COUNT(*) as ?count) '
                        '\n WHERE { '
                        '\n  GRAPH ?g { '
                        '\n   [] ?p [] . '
                        '\n  } '
                        '\n } '
                        '\n GROUP BY ?g '
                        '\n ORDER BY DESC(?count)'],

                   16: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/understanding-graph",
                        'SELECT (COUNT(*) AS ?COUNT) '
                        '\n WHERE { '
                        '\n GRAPH <https://data.cssz.cz/resource/dataset/rocenka/vocabulary> { '
                        '\n [] ?p [] . '
                        '\n  } '
                        '\n }'],

                   17: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/understanding-from-named",
                        'SELECT (COUNT(*) AS ?count) '
                        '\n FROM NAMED <https://data.cssz.cz/resource/dataset/rocenka/vocabulary> '
                        '\n WHERE { '
                        '\n  GRAPH ?g { '
                        '\n   [] ?p [] . '
                        '\n  } '
                        '\n } '],

                   18: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/count-distinct-classes",
                        'SELECT (COUNT(DISTINCT ?class) AS ?count) '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { '
                        '\n   [] a ?class . '
                        '\n  } '
                        '\n }'],

                   19: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/classes-histogram-code-lists",
                        'SELECT ?class (COUNT(?s) AS ?count) '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { '
                        '\n   ?s a ?class . '
                        '\n  } '
                        '\n } '
                        '\n GROUP BY ?class '
                        '\n ORDER BY DESC(?count)'],

                   20: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/disjoint-concept-and-concept-scheme",
                        'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> '
                        '\n ASK '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { '
                        '\n   ?s a skos:Concept, skos:ConceptScheme . '
                        '\n  } '
                        '\n }'],

                   21: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/properties-histogram-code-lists",
                        'SELECT ?property (COUNT(*) AS ?count) '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { '
                        '\n   [] ?property [] . '
                        '\n  } '
                        '\n } '
                        '\n GROUP BY ?property '
                        '\n ORDER BY DESC(?count)'],

                   22: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/classes-histogram-data",
                        'SELECT ?class (COUNT(?s) AS ?count) '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { '
                        '\n   ?s a ?class . '
                        '\n  } '
                        '\n } '
                        '\n GROUP BY ?class '
                        '\n ORDER BY DESC(?count)'],

                   23: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/most-common-class-data",
                        'SELECT ?class (COUNT(?s) AS ?count) '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { '
                        '\n   ?s a ?class . '
                        '\n  } '
                        '\n } '
                        '\n GROUP BY ?class '
                        '\n ORDER BY DESC(?count) '
                        '\n LIMIT 1'],

                   24: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/classes-histogram-metadata",
                        'SELECT ?class (COUNT(?s) AS ?count) '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech/metadata> { '
                        '\n   ?s a ?class . '
                        '\n  } '
                        '\n } '
                        '\n GROUP BY ?class '
                        '\n ORDER BY DESC(?count)'],

                   25: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/count-districts",
                        'PREFIX ruian: <https://data.cssz.cz/ontology/ruian/> '
                        '\n SELECT (COUNT(?okres) AS ?count) '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { '
                        '\n   ?okres a ruian:Okres . '
                        '\n  } '
                        '\n }'],

                   26: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/datasets",
                        'PREFIX qb: <http://purl.org/linked-data/cube#> '
                        '\n SELECT DISTINCT ?dataset '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { '
                        '\n   ?dataset a qb:DataSet . '
                        '\n  } '
                        '\n } '],

                   27: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/properties-histogram-data",
                        'SELECT ?property (COUNT(*) AS ?count) '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { '
                        '\n [] ?property [] . '
                        '\n  } '
                        '\n } '
                        '\n GROUP BY ?property '
                        '\n ORDER BY DESC(?count)'],

                   28: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/reflexive-exact-match",
                        'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> '
                        '\n SELECT DISTINCT ?concept '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { '
                        '\n   ?concept skos:exactMatch ?concept . '
                        '\n  }'
                        '\n }'],

                   29: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/properties-histogram-metadata",
                        'SELECT ?property (COUNT(*) AS ?count) '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech/metadata> { '
                        '\n   [] ?property [] . '
                        '\n  } '
                        '\n } '
                        '\n GROUP BY ?property '
                        '\n ORDER BY DESC(?count)'],

                   30: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/datatypes",
                        'SELECT ?datatype (COUNT(*) AS ?count) '
                        '\n WHERE { '
                        '\n  [] ?p ?literal . '
                        '\n  FILTER (isLiteral(?literal) && datatype(?literal) != "") '
                        '\n  BIND (datatype(?literal) AS ?datatype) \n } '
                        '\n GROUP BY ?datatype '
                        '\n ORDER BY DESC(?count)'],

                   31: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/count-datasets",
                        'PREFIX qb: <http://purl.org/linked-data/cube#> '
                        '\n SELECT (COUNT(DISTINCT ?dataSet) AS ?count) '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> {'
                        '\n   ?dataSet a qb:DataSet . '
                        '\n  } '
                        '\n }'],

                   32: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/properties-qb-observation-data",
                        'PREFIX qb: <http://purl.org/linked-data/cube#> '
                        '\n SELECT DISTINCT ?property '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { '
                        '\n   [] a qb:Observation ; '
                        '\n        ?property [] . '
                        '\n  } '
                        '\n }'],

                   33: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/component-property-subproperties",
                        'PREFIX qb:   <http://purl.org/linked-data/cube#> '
                        '\n PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> '
                        '\n SELECT ?property '
                        '\n WHERE { '
                        '\n  GRAPH <http://purl.org/linked-data/cube> { '
                        '\n   ?property rdfs:subPropertyOf qb:componentProperty . '
                        '\n  } '
                        '\n }'],

                   34: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/data-structure-definition",
                        'PREFIX qb: <http://purl.org/linked-data/cube#> '
                        '\n SELECT ?dsd '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { '
                        '\n   <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> '
                        'qb:structure ?dsd . '
                        '\n  } '
                        '\n }'],

                   35: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/czech-county-labels",
                        'PREFIX ruian: <https://data.cssz.cz/ontology/ruian/> '
                        '\n PREFIX skos:  <http://www.w3.org/2004/02/skos/core#> '
                        '\n SELECT DISTINCT ?label '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { '
                        '\n   [] a ruian:Okres ; '
                        '\n        skos:prefLabel ?label . '
                        '\n  } '
                        '\n }'],

                   36: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/collection-disjoint-with-concept-and-concept"
                        "-scheme",
                        'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> '
                        '\n ASK '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { '
                        '\n   VALUES ?disjointClass { '
                        '\n       skos:Concept '
                        '\n       skos:ConceptScheme '
                        '\n    } '
                        '\n     ?collection a skos:Collection, ?disjointClass . '
                        '\n   } '
                        '\n }'],

                   37: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/label-without-language",
                        'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> '
                        '\n ASK '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { '
                        '\n    VALUES ?labelProperty { '
                        '\n      skos:prefLabel '
                        '\n      skos:altLabel '
                        '\n      skos:hiddenLabel '
                        '\n    } '
                        '\n    [] ?labelProperty ?label . '
                        '\n    FILTER (lang(?label) = "") '
                        '\n   } '
                        '\n }'],

                   38: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/evaluate/empty-labels",
                        'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> '
                        '\n ASK '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> {'
                        '\n    VALUES ?labelProperty { '
                        '\n      skos:prefLabel '
                        '\n      skos:altLabel '
                        '\n      skos:hiddenLabel '
                        '\n    } '
                        '\n    [] ?labelProperty ?label . '
                        '\n    FILTER (STRLEN(?label) = 0) '
                        '\n  } '
                        '\n }  '],

                   39: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/pairwise-disjoint-skos-match-properties",
                        'PREFIX skos: <http://www.w3.org/2004/02/skos/core#> '
                        '\n ASK '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> { '
                        '\n   VALUES ?disjointProperty { '
                        '\n     skos:broadMatch '
                        '\n     skos:narrowMatch '
                        '\n     skos:relatedMatch '
                        '\n    } '
                        '\n   ?a skos:exactMatch ?b ; '
                        '\n      ?disjointProperty ?b . '
                        '\n  } '
                        '\n }'],

                   40: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/old-age-pension-kinds",
                        'PREFIX pension-kind: <https://data.cssz.cz/resource/pension-kind/> '
                        '\n PREFIX skos: <http://www.w3.org/2004/02/skos/core#>'
                        '\n SELECT ?pensionKind '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> {'
                        '\n   ?pensionKind skos:exactMatch pension-kind:PK_old_age_total_without_SR . '
                        '\n  } '
                        '\n }'],

                   41: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/pension-kind-schemes",
                        'PREFIX pen-onto: <http://data.cssz.cz/ontology/pension-kinds/> '
                        '\n PREFIX skos:  <http://www.w3.org/2004/02/skos/core#> '
                        '\n SELECT DISTINCT ?pensionKindScheme '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/pomocne-ciselniky> {'
                        '\n   [] a pen-onto:PensionKind ; '
                        '\n       skos:inScheme ?pensionKindScheme . '
                        '\n   } '
                        '\n }'],

                   42: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/dataset-measures",
                        'PREFIX qb:   <http://purl.org/linked-data/cube#> '
                        '\n SELECT DISTINCT ?measure '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { '
                        '\n   <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> '
                        'qb:structure/qb:component/(qb:measure|qb:componentProperty) ?measure . '
                        '\n    ?measure a qb:MeasureProperty . '
                        '\n   } '
                        '\n }'],

                   43: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/dataset-attributes",
                        'PREFIX qb:   <http://purl.org/linked-data/cube#> '
                        '\n SELECT ?attribute '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { '
                        '\n   <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> '
                        'qb:structure ?dsd . '
                        '\n   ?dsd qb:component [ '
                        '\n    ?property ?attribute '
                        '\n     ] . '
                        '\n   ?attribute a qb:AttributeProperty . '
                        '\n   } '
                        '\n }'],

                   44: ["https://doc.lmcloud.vse.cz/sparqlab/exercise/show/dataset-dimensions",
                        'PREFIX qb:   <http://purl.org/linked-data/cube#> '
                        '\n SELECT DISTINCT ?dimension '
                        '\n WHERE { '
                        '\n  GRAPH <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> { '
                        '\n   <https://data.cssz.cz/resource/dataset/duchodci-v-cr-krajich-okresech> '
                        'qb:structure/qb:component/(qb:dimension|qb:componentProperty) ?dimension . '
                        '\n  } '
                        '\n } ']
                   }
