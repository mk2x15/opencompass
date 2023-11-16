from mmengine.config import read_base

with read_base():
    from .datasets.siqa.siqa_gen import siqa_datasets
    # from .datasets.winograd.winograd_ppl import winograd_datasets
    from .datasets.xquad.xquad_gen import xquad_datasets
    from .datasets.wisesight_senti.wisesight_senti_gen import wisesenti_datasets
    from .datasets.limesoda.limesoda_gen import limesoda_datasets
    from .datasets.wikilingua_doc.wikilingua_doc_gen import wikilinguadoc_datasets
    from .datasets.massive.massive_gen import massive_datasets
    from .models.hf_llama.hf_llama_7b import models
    # from .models.opt.hf_opt_125m import opt125m
    from .models.opt.hf_opt_350m import opt350m

datasets = [*massive_datasets]
models = [opt350m]
