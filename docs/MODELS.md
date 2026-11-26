# Open-weight video generation research

Target: Apple M4 with 24 GB unified memory. Benchmarks have **not yet been run**.

## Candidates
- Wan 2.1 T2V 1.3B with Apple's MLX implementation: initial local benchmark candidate.
- Wan 2.2 variants: compare memory and support only after confirming actual backend compatibility.
- CogVideoX 2B: research alternative; compatibility is not assumed.
- LTX-Video / LTX-2: evaluate model variants, memory use and licensing independently.

Sources:
- https://github.com/Wan-Video/Wan2.1
- https://github.com/ml-explore/mlx-examples
- https://github.com/THUDM/CogVideo
- https://github.com/Lightricks/LTX-Video

## Benchmark protocol
Record model revision, weight size, quantization, software versions, input prompt, seed, frames, fps, resolution, wall-clock time, peak unified memory, quality observations and license restrictions.

Avoid 14B unquantized models on 24 GB until a proven memory-fitting path exists. Model source code licenses and model weight/content licenses may differ.

## TinyToon requirements
Prioritize image-to-video and reference-image conditioning for recurring original characters, coherent facial features, child-friendly motion, and 9:16 export. Retain manually reviewed character sheets as canonical sources.
