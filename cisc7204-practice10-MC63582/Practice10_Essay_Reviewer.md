# Thread title (copy exactly)
My Essay as a Reviewer to the PCA Article

---

## Essay body (paste into the forum message)

**Review of:** E. Saccenti, “A gentle introduction to principal component analysis using tea-pots, dinosaurs, and pizza,” *Teaching Statistics* 46 (2024): 38–52. DOI: 10.1111/test.12363

**Problem / research question.** Modern data are high-dimensional, yet many students meet PCA only as opaque software output. Saccenti asks how to teach PCA so that learners grasp *why* rotation, variance, and linear combinations matter for visualization and dimensionality reduction—without requiring advanced linear algebra first—while still avoiding a pure “black box.”

**Key contributions.** The paper’s main contribution is pedagogical and visual rather than a new PCA algorithm. It reverses the usual order of presentation: start from *visualization* (2-D teapot; 3-D triceratops via interactive rotation), equate information with variance, introduce planar rotation with trigonometry as weighted linear combinations, then define principal components as directions of maximum variance that are mutually uncorrelated. Dimensionality reduction and multicollinearity removal follow as consequences. Concrete case studies (1000-D synthetic dinosaur data; pizza chemistry; psoriasis gene expression) show when score/loading plots succeed and when PCA fails. An appendix supplies the covariance-eigenvalue formulation for instructors who want rigor later. Course structure (two short lectures + R/Matlab practicals) and positive student feedback at Wageningen add evidence of classroom utility.

**Strengths and utility (visualization lens).** For a data-visualization course, this is a strong contribution: images carry the argument; rotation is treated as an exploratory visual operation before it becomes an optimization problem; scores and loadings are introduced as the natural visual products of PCA; and the “when PCA does not help” section teaches critical reading of plots (ball-shaped clouds, diffuse loadings). The pizza example shows unsupervised structure discovery in 2-D after standardization—exactly the kind of practice students need when reducing many measured attributes to interpretable views. Suggestions to improve: (1) add a short interactive checklist for choosing how many PCs (scree / cumulative variance) with a worked visual example; (2) contrast Pearson-linear PCA with one nonlinear embedding (e.g., a simple curved manifold cartoon) so students see what linear PCs miss; (3) provide side-by-side R and Matlab recipes for the same pizza analysis to lower tooling friction; (4) discuss loading-sign flip and axis reflection explicitly as visualization pitfalls.

**Limitations and weaknesses.** This is primarily a teaching paper, not a novel visualization research method. Classroom evaluation is promising but brief and single-institution. Examples lean toward life-science audiences. PCA’s linear/Pearson assumptions and scale sensitivity are acknowledged, yet nonlinear alternatives and formal component-selection methods remain pointers to the literature. Dense loadings in the gene example motivate sparse PCA only lightly. Contribution to “visualization research” is strongest as *design of instructional visualization* and *interpretation practice*, not as a new visual encoding.

**Methods and tools.** Conceptual pipeline: scatter plots → rotation matrices (sine/cosine) → variance explained → PCs as ordered uncorrelated linear combinations → scores/loadings. Computation via Matlab `pca` (and class use of R); teapot geometry and triceratops coordinates for demos; pizza data from data.world; psoriasis subset and codes on GitLab (`esaccenti/dinosaurpca`); MATLAB R2023a.

**Instructions for running PCA (as presented).** (1) Organize numeric observations × variables; mean-center (and usually standardize to unit variance when units/scales differ). (2) Call Matlab `[R,T,~,~,VarExplained] = pca(X);` (or equivalent `prcomp`/`princomp` in R) to obtain scores, loadings, and variance explained. (3) Inspect cumulative variance; plot PC1–PC2 (or PC1–PC3) scores, optionally color by known labels only for interpretation—not as input to PCA. (4) Read loadings to see which original variables drive each axis; remember loading signs are arbitrary in direction. (5) Interpret clusters only when variables are correlated; if variables are nearly uncorrelated, PCA mainly reorders axes and may not separate groups. Data/code: https://gitlab.com/esaccenti/dinosaurpca ; pizza: https://data.world/sdhilip/pizza-datasets .

Overall recommendation (as a constructive reviewer): accept as a valuable teaching contribution to visualization-oriented statistics education, with revisions that strengthen component-selection guidance and make failure modes of linear PCA more visually explicit.

---

### Declaration of AI Usage - mc63582 FAN ZIQIAN

- Did I use an AI LLM? Yes
- Exact LLM used: Cursor Composer
- Web Browser used: Cursor IDE Browser (Chrome-based) for UMMoodle and related article pages
