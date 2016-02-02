# InfraPhenoGrid

## A scientific workflow infrastructure for Plant Phenomics on the Grid

Plant phenotyping consists in the observation of physical and biochemical traits of plant genotypes in response to environmental conditions.
Challenges, in particular in context of climate change and food security, are numerous. High-throughput platforms have been introduced
to observe the  dynamic growth of a large number of plants in different environmental
conditions. Instead of considering a few genotypes at a time (as it is the case when phenomic traits are measured manually), such platforms make it possible to use completely new kinds of approaches.
However, the data sets produced by such widely instrumented platforms are huge, constantly augmenting and produced by increasingly complex experiments, reaching a point where distributed computation is mandatory to extract knowledge from data.

In this paper, we introduce [InfraPhenoGrid], the infrastructure we designed and deploy to efficiently manage data sets produced by the
[PhenoArch] plant phenomics platform in the context of the French [Phenome] Project. Our solution consists in deploying [OpenAlea] scientific workflows on a Grid using the [SciFloware] middleware to pilot workflow executions. Our approach is user-friendly
in the sense that despite the intrinsic complexity of the infrastructure,
running scientific workflows and understanding results obtained (using provenance information) is kept as simple as possible for end-users.

[InfraPhenoGrid]: https://github.com/openalea/InfraPhenoGrid
[PhenoArch]: https://www6.montpellier.inra.fr/lepse_eng/M3P/PHENOARCH-platform
[Phenome]: https://www.phenome-fppn.fr/phenome_eng/
[SciFloware]: http://www-sop.inria.fr/members/Didier.Parigot/pmwiki/Scifloware/
[OpenAlea]: http://openalea.gforge.inria.fr

## Installation

### OpenAlea installation
- [Ubuntu installation](http://openalea.gforge.inria.fr/dokuwiki/doku.php?id=download:linux)

### Detailed instructions
- pyqt
- pywin32
- ipython
- ipython-console

- deploy
- core
- graph_editor
- vpltk (change default QT_API_VERSION to 2 instead of 1 in qt/__init__.py)
- misc
- oalab
- visualea

- numpy
- scipy
- matplotlib
- opencv

- openalea-opencv
- infraphenogrid

## Data

<img src="./src/openalea/infraphenogrid/share/data/images/side_blob_test_1.png" width="30%"/>
<img src="./src/openalea/infraphenogrid/share/data/images/top_blob_test.png" width="43%"/>

Fetch data set:
https://gforge.inria.fr/frs/download.php/file/35148/data_set_0962_A310_ARCH2013-05-13.zip

Extract in any directory
Launch visualea
Open "openalea/infraphenogrid/demo/area_estimation/demo_area_estimation_meanshift"
Open 'import' node
select dir where images where extracted.
run workflow

## Workflow

### Description

In 'openalea/infraphenogrid/demo' two directories contain:
- some example of algorithms to evaluate the leaf area of binarized images
- some examples of algorithms to binarize pictures taken on the [PhenoArch] platform.

Two more workflow compare the result of each category of algorithms.

### Usage

- Open a workflow in 'visualea' (double click in the package explorer view)
- if the workflow contains a 'import_images' node you need to open it (double click on the node)
to point it to the directory where the data set has been unpacked.
- Run the workflow to display the results (Ctrl + R or right click on a specific node to run)

## Notebook

