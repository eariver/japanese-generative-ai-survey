# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w36-primary-20260917-r1
- locator: https://www.worldlabs.ai/blog/atlas
- observed_at: 2026-09-17T00:00:00Z
- published_at: 2026-09-01
- retrieval: webfetch markdown of World Labs blog "Atlas: A World Model for Spatial Intelligence"; stored verbatim as returned.
- authority_class: PRIMARY_OFFICIAL

# Retrieved content (verbatim as returned)

September 1, 2026. Introducing Atlas, our new omni world model for spatial intelligence.

# Atlas: A World Model for Spatial Intelligence

World models generate, reconstruct, and simulate any possible world. They understand how worlds appear, behave, and evolve so that we can render imagined worlds for creative users, simulate the real world in high fidelity, and help robots plan actions. At World Labs, we build these general purpose world models in pursuit of spatial intelligence.

Today we are introducing Atlas, our next-generation world model. Atlas is an omni model that we pretrained from scratch to natively operate on text, images, video, and 3D. It is a multimodal autoregressive diffusion transformer: all inputs are combined into a shared spatial context. Atlas uses that context to generate what comes next, staying consistent in 3D with everything it has seen and imagining what lies beyond it. Atlas is built to scale: its performance improves with increased training compute, and we expect this trend to hold as we continue scaling.

Atlas can perform a broad range of tasks spanning world generation, reconstruction, and simulation:

-   **Camera-Controlled Generation**: Atlas generates images and videos from one or more images with pixel-perfect camera control, outputting up to 1 minute of video at 1440p.
-   **Spatial Reconstruction**: Atlas reconstructs real world scenes from one to dozens of input images. It generates both image frames from novel views and explicit 3D outputs, outperforming state-of-the-art models specialized for 3D reconstruction.
-   **Space-Time Simulation**: Atlas models space and time from input videos, reframing videos for dramatic visual effects and enabling Real-to-Sim workflows for robotics.
-   **Image Generation**: Atlas generates images and 360 panoramas from text; it can follow complex prompts, render text, and generate a wide variety of visual styles.

Atlas will power future versions of [Marble](https://marble.worldlabs.ai/) and other products from World Labs.

## Camera-Controlled Generation

Atlas takes one or more reference images and generates new views at any camera position and angle you specify. Generated views match the content and geometry of the input images, smoothly extrapolating beyond them to imagine parts of the scene not visible in the inputs.

### Pixel-Perfect Camera Control

Atlas uses precise camera geometry as a native input type, going beyond coarse text-based instructions for camera control. This lets you frame every shot and control every motion.

### Generating with Spatial Context

Similar to an LLM, Atlas first encodes its inputs into a context, then generates outputs conditioned on the context. However, Atlas is unique because each image is grounded at a 3D position in space; this forms a **spatial context**.

### Controllable Long Videos

Atlas lets you generate long videos with precise control by combining camera movement and spatial context management. In the example described, a 1 minute video at 1440p resolution is generated using a small number of reference images with a hand-designed camera path through the scene.

## Spatial Reconstruction

Atlas reconstructs real-world spaces from one or more input images. It does not require special capture equipment or hundreds of dense views to faithfully reconstruct objects and scenes.

Atlas can take a variable number of input views of a scene. When parts of the world are not visible in the input views, Atlas imagines a plausible way to fill in the gaps by drawing from its rich world knowledge. Passing more input images gives Atlas more context: the more it sees, the less it imagines. Atlas typically gives faithful reconstructions with as few as two or three images, outperforming state-of-the-art results by models specially trained only for 3D reconstruction. However, Atlas can also make use of over a hundred input images in its spatial context.

### Explicit 3D Outputs

Atlas natively operates on both 2D image frames and 3D depth maps, enabling it to output worlds as point clouds or 3D Gaussian splats. From a single input image, Atlas produces a full 3D world by jointly generating new views and estimating their geometry. From a video of a real space, it predicts the depth of every frame and combines them into a 3D reconstruction.

## Space-Time Simulation

Atlas serves as a world simulator. It understands both the spatial structure of the world and how the world evolves over time.

### Reframing Video

Atlas turns a handful of ordinary cameras into a "bullet time" multiview capture studio. With footage from as few as three cameras, Atlas can freeze time and reframe shots, letting you view events from impossible angles.

### Robotics Simulation

Atlas opens up new ways to scale Real-to-Sim for both navigation and manipulation. Atlas reconstructs spaces and aids in simulating robot navigation. From a few casual recordings, Atlas aids in building a simulation that also captures how objects move and interact. Once a task is simulated, you can vary objects, positions, motion, lighting, and background.

## Technical Details

### Model Architecture

Atlas is an omni model designed to handle many tasks and many kinds of input and output data in a single unified architecture, putting spatial control at the heart of the model.

Atlas is a multimodal autoregressive diffusion transformer. Its inputs are grounded in 3D space to form a spatial context, and it generates multimodal outputs conditioned on its context.

-   **Multimodal**: Atlas can natively process many different data types. At present it can operate on text, images, camera poses, and 3D depth maps; videos are represented as sequences of images.
-   **Autoregressive**: Atlas operates on sequences of elements, where each element is one of the multimodal data types above. Each output is generated one at a time, conditioned on earlier parts of the sequence.
-   **Diffusion**: Atlas is a rectified flow model that generates outputs by gradually denoising them.
-   **Transformer**: The transformer architecture consists primarily of large matrix multiply operations and is well-adapted to modern hardware.

### Benchmarks

Third-party human raters judge which model better follows the intended camera path. These results confirm that **Atlas outperforms recent video models at camera-controlled generation**, including comparisons against MiniMax H3 75%, Gemini Omni Flash 81%, Happy Horse 1.1 86%, FLUX 3 93%, Seedance 2.5 94% share of voters choosing Atlas.

Atlas outperforms the best specialized open-source reconstruction models on 3D reconstruction from sparse input views, including Pi3X (posed), pi-cubed, VGGT-Omega 1B, Depth Anything 3, MapAnything, across benchmarks DTU, ETH3D, KITTI, NRGBD, 7-Scenes, T&T, ScanNet.

### Model Scaling

We pretrained Atlas from scratch on a large diverse corpus of multimodal data. Over the course of development, we trained a series of models of increasing size and training compute, and found that each new level of compute unlocked new model capabilities.

## Build with Atlas

Atlas is entering early access with select partners.

*Please cite as: @article{worldlabs2026atlas, author = {World Labs Team}, title = {Atlas: A World Model for Spatial Intelligence}, journal = {World Labs Blog}, year = {2026}, note = {https://www.worldlabs.ai/blog/atlas}}*

[truncated for edition-local storage: interactive demos, images, and footer omitted; core article text preserved verbatim]
