# Changelog

Auto-generated from commit subjects by [git-cliff](https://git-cliff.org/) on tag
push. Click any commit SHA below to see the full message body (why / how /
validation data) — those live in `git log`, not here. Don't hand-edit; the file
is regenerated on every tag.

**Versioning:** SemVer in `0.x` — treat any minor bump as potentially breaking
until `1.0`. Past CalVer tags (`v2026.05.09`, `v2026.05.10`) are preserved for
history; SemVer takes over from `v0.3.0` onward.

| CalVer tag | SemVer equivalent | Date |
|---|---|---|
| `v2026.05.09` | (≈ v0.1.0) | 2026-05-09 — first tagged release |
| `v2026.05.10` | (≈ v0.2.0) | 2026-05-10 — stack reorg + Gemma 4 INT8 PTH unblock |

---

## v0.12.0 — 2026-09-29


### ✨ Features

- feat(launch): label launched containers with their slug (club3090.slug) (#1498) ([#1498](https://github.com/noonghunna/club-3090/pull/1498) by @noonghunna)
- feat(settings): one-time notice while settings live in the checkout (#1466) (#1492) ([#1492](https://github.com/noonghunna/club-3090/pull/1492) by @noonghunna)
- feat(gateway): own routes and keys move to the settings dir (#1466, 4c) (#1489) ([#1489](https://github.com/noonghunna/club-3090/pull/1489) by @noonghunna)
- feat(caches): shared compile caches keyed by engine image; KV disk tier in the data dir (#1466 4a/4b) (#1491) ([#1491](https://github.com/noonghunna/club-3090/pull/1491) by @noonghunna)
- feat(c3): Launch settings form with drift marker (#1465, 3d) (#1490) ([#1490](https://github.com/noonghunna/club-3090/pull/1490) by @noonghunna)
- feat(gateway): gpu-mode gateway, rotate --apply, first-run key (#1467) (#1487) ([#1487](https://github.com/noonghunna/club-3090/pull/1487) by @noonghunna)
- feat(config): per-slug launch settings and resolver (#1465, 3b/3c) (#1486) ([#1486](https://github.com/noonghunna/club-3090/pull/1486) by @noonghunna)
- feat(config): settings.sh to see, change and migrate settings (#1466) (#1485) ([#1485](https://github.com/noonghunna/club-3090/pull/1485) by @noonghunna)
- feat(config): shell writers save settings via the one writer (#1466) (#1481) ([#1481](https://github.com/noonghunna/club-3090/pull/1481) by @noonghunna)
- feat(c3): read and write settings through the one loader (#1466) (#1482) ([#1482](https://github.com/noonghunna/club-3090/pull/1482) by @noonghunna)
- feat(gateway): per-install gateway key in secrets.env (#1467) (#1479) ([#1479](https://github.com/noonghunna/club-3090/pull/1479) by @noonghunna)
- feat(config): launch-knob catalogue + per-slug knobs in emit (#1465, 3a) (#1480) ([#1480](https://github.com/noonghunna/club-3090/pull/1480) by @noonghunna)
- feat(config): `unset --root` also clears the legacy repo .env (#1466) (#1478) ([#1478](https://github.com/noonghunna/club-3090/pull/1478) by @noonghunna)
- feat(config): gpu-mode + studio helpers read settings through the loader (#1466, 1b-2) (#1476) ([#1476](https://github.com/noonghunna/club-3090/pull/1476) by @noonghunna)
- feat(config): launchers and tools read settings through the one loader (#1466, 1b-1) (#1475) ([#1475](https://github.com/noonghunna/club-3090/pull/1475) by @noonghunna)
- feat(config): one settings loader (bash + Python) and one writer (#1466, 1a) (#1472) ([#1472](https://github.com/noonghunna/club-3090/pull/1472) by @noonghunna)
- feat(sglang): forward NCCL_P2P_DISABLE in every multi-GPU compose (#1468) ([#1468](https://github.com/noonghunna/club-3090/pull/1468) by @noonghunna)
- feat(vllm): pass the Qwen3.8 template as --chat-template too (#1463) ([#1463](https://github.com/noonghunna/club-3090/pull/1463) by @noonghunna)
- feat(gateway): send Claude Code's /v1/messages straight to SGLang (#1461) ([#1461](https://github.com/noonghunna/club-3090/pull/1461) by @noonghunna)
- feat(scripts): agentic KV offload probe (3 switched conversations) + report.sh --kv-agentic (#1435) ([#1435](https://github.com/noonghunna/club-3090/pull/1435) by @paulp83)
- feat: agent troubleshooting — prompt-cache share readout + LiteLLM request-logging switch (#1442) ([#1442](https://github.com/noonghunna/club-3090/pull/1442) by @noonghunna)
- feat(omp): point omp at whatever slug is serving, through the gateway (#1440) ([#1440](https://github.com/noonghunna/club-3090/pull/1440) by @noonghunna)
- feat(litellm): agent-ready gateway routes — effort passes, reasoning survives, real context window (#1438) ([#1438](https://github.com/noonghunna/club-3090/pull/1438) by @noonghunna)
- feat(gpu-mode): report support-service image drift; add `gpu-mode upgrade` (#1437) ([#1437](https://github.com/noonghunna/club-3090/pull/1437) by @noonghunna)
- feat(qwen38): probabilistic draft sampling; drop the inert #1052 hoist (#1428) ([#1428](https://github.com/noonghunna/club-3090/pull/1428) by @noonghunna)
- feat(setup): `setup.sh <slug>` fetches a slug's weights + companions (#1426) ([#1426](https://github.com/noonghunna/club-3090/pull/1426) by @noonghunna)
- feat(qwen38-single-iq4xs): LLAMA_ARG_MMPROJ_OFFLOAD knob for the #1380 recipe (#1424) ([#1424](https://github.com/noonghunna/club-3090/pull/1424) by @noonghunna)
- feat(kv-offload): probe that proves the tier serves hits; fix SGLang disk prefetch (#1421) ([#1421](https://github.com/noonghunna/club-3090/pull/1421) by @noonghunna)
- feat(qwen3.8/sglang): opt-in HiCache host-RAM + disk tier; dual-fast K=20 holds 2 x 262K (#1416) ([#1416](https://github.com/noonghunna/club-3090/pull/1416) by @noonghunna)
- feat(qwen3.8/vllm): opt-in KV offload to host RAM and disk on dual MTP tiers (#1408) ([#1408](https://github.com/noonghunna/club-3090/pull/1408) by @noonghunna)
- feat(qwen3.8/vllm): bf16 SSM state by default on the DFlash tiers (#1407) ([#1407](https://github.com/noonghunna/club-3090/pull/1407) by @noonghunna)
- feat(qwen3.8/vllm): bf16 SSM state by default; dual-fast reaches 2x 262K (#1406) ([#1406](https://github.com/noonghunna/club-3090/pull/1406) by @noonghunna)
- feat(engine): bump both PrismML engines to prism-b10735-842b188 (#1405) ([#1405](https://github.com/noonghunna/club-3090/pull/1405) by @noonghunna)
- feat(quality): record the sampling in effect and the rig (#1396) (#1398) ([#1398](https://github.com/noonghunna/club-3090/pull/1398) by @noonghunna)
- feat(engine): pin llama-cpp-local to llama.cpp v0.5.0 (b11146) — unbooted, validation pending (#1397) ([#1397](https://github.com/noonghunna/club-3090/pull/1397) by @noonghunna)
- feat(thinkingcap-qwen3.8-27b): onboard ThinkingCap-Qwen3.8-27B as 29 experimental replica slugs (#1395) ([#1395](https://github.com/noonghunna/club-3090/pull/1395) by @noonghunna)
- feat(engine): bump vllm-stable v0.29.0 -> v0.30.0 (maintenance; no patch drops) (#1392) ([#1392](https://github.com/noonghunna/club-3090/pull/1392) by @noonghunna)
- feat(mimo): promote llamacpp/mimo9b-single-vision to ⚠️ Production w/ caveats ([b3fb6b6](https://github.com/noonghunna/club-3090/commit/b3fb6b61509628d84f625317f4f91809240ac05f))
- feat(quality-test): opt-in --thinking-budget, verified per engine + pack class ([fbadccf](https://github.com/noonghunna/club-3090/commit/fbadccff2f791f17a1ebec155c7d604e5dc95381))
- feat(mimo-v2.6-9b): add MiMo-V2.6-Distill-Qwen-9B single-card vision slug ([c176b1c](https://github.com/noonghunna/club-3090/commit/c176b1c2948cf84ade2d89735dec6a079439d008))
- feat(exl3): size MOE_SPLIT as a VRAM fit instead of a hardcoded expert count (#1366) ([c5b480b](https://github.com/noonghunna/club-3090/commit/c5b480bd3963e4bc02669384a77c42781455768a))
- feat(launch): separate the image pin from hardware injection; drop the launcher prefix gate (#1365) ([83615a2](https://github.com/noonghunna/club-3090/commit/83615a2c7df3f435d8c62a706265c47fb9768db3))
- feat(launch): per-engine concurrency knob for #246 Phase 2 envelope injection ([ce18478](https://github.com/noonghunna/club-3090/commit/ce18478c8832fee3d16d73544583aa8507f3613a))
- feat(bonsai-ternary): raise the reasoning budget 8192 -> 16384 ([aecc254](https://github.com/noonghunna/club-3090/commit/aecc254e9d2f547dec789df15dc11da96b5104ab))
- feat(qwen3.8-27b): MTP-enabled ternary Bonsai slug on a source-built prism engine ([d95962f](https://github.com/noonghunna/club-3090/commit/d95962fcefc5e7c8534d63e9b720a3c4c5180660))
- feat(sglang): W4A8 on by default for the autoround-int4 slugs ([c18c8a4](https://github.com/noonghunna/club-3090/commit/c18c8a48ea645c226a4bf2c5de63a93221bd50ae))
- feat(qwen3.8-27b): expose all six --reasoning-* knobs across the llama.cpp composes ([0f45f9c](https://github.com/noonghunna/club-3090/commit/0f45f9cc6e479b9973271ba0a49f89de17e4bf21))
- feat(bonsai-ternary): cap thinking at 8192 tokens via --reasoning-budget ([5a28546](https://github.com/noonghunna/club-3090/commit/5a285469e8b83c3a8a27232adad537ea6a6ec8f6))
- feat(litellm): serve the gateway from what is running, not from the catalog ([ef2ab27](https://github.com/noonghunna/club-3090/commit/ef2ab2784bc29147df21fa436cdba9608525622b))
- feat(owui): sync the model picker with what is serving, and prune what is not ([dcb4996](https://github.com/noonghunna/club-3090/commit/dcb499652d7980988c1528bfe20d78a2622f44b9))
- feat(engines): add exl3/TabbyAPI and llama.cpp-prism ternary engines ([8757433](https://github.com/noonghunna/club-3090/commit/87574338191b8e22dc7b9222b90ce946c76506cb))
- feat(qwen3.8-27b): fa2-fp8kv on multi4/multi8 + kv-calc TP clamp (#1337) ([#1337](https://github.com/noonghunna/club-3090/pull/1337) by @noonghunna)
- feat(p2p): DISABLE_CUSTOM_ALL_REDUCE — keep the peer transport, drop the kernel (#1332) (#1334) ([#1334](https://github.com/noonghunna/club-3090/pull/1334) by @noonghunna)
- feat(sgl/dual-max): pin K=10 and raise context to 163840 (#1331) ([#1331](https://github.com/noonghunna/club-3090/pull/1331) by @noonghunna)
- feat(sgl/dual-fast): 2-session default — mem-fraction 0.95, max-running-requests 2 (#1329) ([#1329](https://github.com/noonghunna/club-3090/pull/1329) by @noonghunna)
- feat(qwen3.8): dual-ultrafast gains fp8 KV + FlashAttn via the FA2 plugin ([c511489](https://github.com/noonghunna/club-3090/commit/c511489a30960b1c2780101018d112f3fba58bf8))
- feat(qwen38): integrate prebuilt FlashAttention FP8 KV into ultramax ([d7bd7a5](https://github.com/noonghunna/club-3090/commit/d7bd7a5da056b743dcb5d4030635cef6dd183492))
- feat(qwen38): add hypermax FA2 FP8 KV profile for dual SM86 ([d35b3fa](https://github.com/noonghunna/club-3090/commit/d35b3fa4d167bb5c906276974ed29c7ad7b9d084))
- feat(probe): concurrent mode — two deep sessions, then compact one ([4bb3832](https://github.com/noonghunna/club-3090/commit/4bb3832487c86314d529015a221cedfa8e4d411d))
- feat(probe): report drafter acceptance and preemptions per turn (#1259) ([315ca4c](https://github.com/noonghunna/club-3090/commit/315ca4ca356997e8977d865e7b2c152610f94a9d))
- feat(bench): add deep-context-probe — the first instrument that reaches the regime users run in ([30027c6](https://github.com/noonghunna/club-3090/commit/30027c63de4cd52eb12cd2e08669bea1988080ff))
- feat(report): capture the engine's RESOLVED config + diff it against the shipped recipe (#1265) (#1286) ([#1286](https://github.com/noonghunna/club-3090/pull/1286) by @noonghunna)
- feat(report): surface the GPU power cap up front as a % of each card's default (#1277) ([#1277](https://github.com/noonghunna/club-3090/pull/1277) by @noonghunna)
- feat(engine): pin llama-cpp-local by DIGEST (b10920); widen the image-drift gate to all engines (#1273) ([#1273](https://github.com/noonghunna/club-3090/pull/1273) by @noonghunna)
- feat(engine): bump vllm-stable v0.27.1 -> v0.29.0; SPLIT the dflash2 backport (vllm#51581 is still open) (#1272) ([#1272](https://github.com/noonghunna/club-3090/pull/1272) by @noonghunna)
- feat(qwen3.8/vllm): enable prompt_tokens_details in the usage block (#1260) ([#1260](https://github.com/noonghunna/club-3090/pull/1260) by @noonghunna)
- feat(qwen3.8): wire @A1RM4X's W4A8 patch to every sgl/ slug ([6aa406c](https://github.com/noonghunna/club-3090/commit/6aa406c1493a98eefa1252ef8dc61be310df1e46))
- feat(qwen3.8): SGLang metrics + concurrency headroom, and an honest sampler contract across all three engines (#1244) ([#1244](https://github.com/noonghunna/club-3090/pull/1244) by @noonghunna)
- feat(sglang): first SGLang tier for Qwen3.8-27B — 11 sgl/ slugs on stock v0.5.19 (#1237) ([#1237](https://github.com/noonghunna/club-3090/pull/1237) by @noonghunna)


### 🎯 New models + serving paths

- Add MAMBA_RADIX_CACHE_STRATEGY env seam to SGLang composes (#1264) (#1412) ([#1412](https://github.com/noonghunna/club-3090/pull/1412) by @paulp83)


### 🐛 Bug fixes

- fix(report): spread partial-core bandwidth runs over every socket and die (#1500) ([#1500](https://github.com/noonghunna/club-3090/pull/1500) by @noonghunna)
- fix(report): measure host memory bandwidth the same way on any rig (#1499) ([#1499](https://github.com/noonghunna/club-3090/pull/1499) by @noonghunna)
- fix(records): attribute measurement records to the right slug, pods included (#1477) (#1497) ([#1497](https://github.com/noonghunna/club-3090/pull/1497) by @noonghunna)
- fix(health): autodetect the running endpoint; name the engine via engine-kind (#1495) ([#1495](https://github.com/noonghunna/club-3090/pull/1495) by @noonghunna)
- fix(gpu-mode): settings file per compose call; pass exported studio paths (#1466) (#1483) ([#1483](https://github.com/noonghunna/club-3090/pull/1483) by @noonghunna)
- fix(shm-cleanup): use `command grep` (test-no-bare-grep red since #1410) (#1474) ([#1474](https://github.com/noonghunna/club-3090/pull/1474) by @noonghunna)
- fix(sglang): SPEC_N=0 on dual-fast boots again (mem fraction 0.90 w/o drafter) (#1471) ([#1471](https://github.com/noonghunna/club-3090/pull/1471) by @noonghunna)
- fix(p2p): score SGLang's V1 custom all-reduce as on (PCIe rigs) (#1470) ([#1470](https://github.com/noonghunna/club-3090/pull/1470) by @noonghunna)
- fix(sglang): remap UUID CUDA_VISIBLE_DEVICES to ordinals; flag failed custom-AR setup (#1462) (#1469) ([#1469](https://github.com/noonghunna/club-3090/pull/1469) by @noonghunna)
- fix(switch): refuse a launch before tearing down the running slug (#1464) ([#1464](https://github.com/noonghunna/club-3090/pull/1464) by @noonghunna)
- fix(qwen3.8 template): accept reasoning_effort minimal and max (#1458) ([#1458](https://github.com/noonghunna/club-3090/pull/1458) by @noonghunna)
- fix(patches): list every slug that mounts a vendored chat template (+ guard) (#1457) ([#1457](https://github.com/noonghunna/club-3090/pull/1457) by @noonghunna)
- fix(qwen3.8 template): render a later system message in place — Claude Code on vLLM (#1456) ([#1456](https://github.com/noonghunna/club-3090/pull/1456) by @noonghunna)
- fix(omp): match the override keys to the served name — ThinkingCap slugs serve `thinkingcap38-27b` (#1444) ([#1444](https://github.com/noonghunna/club-3090/pull/1444) by @paulp83)
- fix(qwen3.8): render tool schemas with sorted keys so reordered keys keep the prefix cache (#1441) ([#1441](https://github.com/noonghunna/club-3090/pull/1441) by @noonghunna)
- fix(sglang): honour a request's reasoning_effort on the Qwen3.8 and ThinkingCap slugs (#1439) ([#1439](https://github.com/noonghunna/club-3090/pull/1439) by @noonghunna)
- fix(verify-full): stop failing concise and adaptive thinkers at [7/10] (#1429) ([#1429](https://github.com/noonghunna/club-3090/pull/1429) by @noonghunna)
- fix(composes): drafter entrypoint defaults to the flag's own depth (#1425) ([#1425](https://github.com/noonghunna/club-3090/pull/1425) by @noonghunna)
- fix(registry): sync max_num_seqs / mem_util with the composes; guard against drift (#1417) ([#1417](https://github.com/noonghunna/club-3090/pull/1417) by @noonghunna)
- fix(bench): detect SGLang collective runtime state (#1415) ([#1415](https://github.com/noonghunna/club-3090/pull/1415) by @TreyThomasCodes)
- fix(registry): order the ThinkingCap slugs like their qwen3.8-27b twins (#1413) ([#1413](https://github.com/noonghunna/club-3090/pull/1413) by @noonghunna)
- fix(ternary): thinking-row min_p 0.05 per the Bonsai 2 card and PrismML demo (#1411) ([#1411](https://github.com/noonghunna/club-3090/pull/1411) by @noonghunna)
- fix(kv-offload): stop /dev/shm leaks — unlink the disk-mode region, pre-boot cleanup (#1410) ([#1410](https://github.com/noonghunna/club-3090/pull/1410) by @noonghunna)
- fix(qwen3.8/sglang): act_format int8 on the W4A8-default SGLang tiers (#1409) ([#1409](https://github.com/noonghunna/club-3090/pull/1409) by @noonghunna)
- fix(bench): exit 0 on a clean run, not 1 (#1404) ([#1404](https://github.com/noonghunna/club-3090/pull/1404) by @noonghunna)
- fix(agents-a1): use native BF16 dtype (#1403) ([#1403](https://github.com/noonghunna/club-3090/pull/1403) by @TreyThomasCodes)
- fix(studio): pin step-voice pip deps to the validated image (#1401) ([#1401](https://github.com/noonghunna/club-3090/pull/1401) by @noonghunna)
- fix(studio): fetch Saganaki22's nodes from forks at pinned commits (#1394) (#1400) ([#1400](https://github.com/noonghunna/club-3090/pull/1400) by @noonghunna)
- fix(report): parse SGLang v0.5.20's dict-shaped server_args dump (#1399) ([#1399](https://github.com/noonghunna/club-3090/pull/1399) by @noonghunna)
- fix(fa2): keep fp8-KV prefill chunks inside the kernel's 2048 limit with 2+ sequences (#1358) ([edb2284](https://github.com/noonghunna/club-3090/commit/edb228499c4d7a5229ff3947a52c4a951c5761c5))
- fix(mimo): vendor a chat template that stops the Qwen3-Coder tool-call trap ([cf5c454](https://github.com/noonghunna/club-3090/commit/cf5c4544f7b2776ea1e3b8bf3ed8858b39624236))
- fix: make exllamav3 (TabbyAPI) visible to c3, the verify scripts and token counts (#1360) ([0dab6d9](https://github.com/noonghunna/club-3090/commit/0dab6d9c00d500c2ce22bfe0090f0064284ee997))
- fix(tests): repair test-registry-lookup's stale awk anchor (regression from #1330) ([02d2d18](https://github.com/noonghunna/club-3090/commit/02d2d18fdcfe9c16124a3e2aacdb38c59a8b34d7))
- fix(mimo-v2.6-9b): disjoint verify globs + drop the opt-in spec passthrough ([03429bf](https://github.com/noonghunna/club-3090/commit/03429bfcdbeb980edf5ffb124047bb9fbf53309b))
- fix(registry): re-canonicalize registry.yaml after the mimo entry ([12321d0](https://github.com/noonghunna/club-3090/commit/12321d07f0a872da0240f42ad33d52157b356ab4))
- fix(preflight): recognise our own fork images — 30 slugs skipped the weights check (#1247) ([4b1d599](https://github.com/noonghunna/club-3090/commit/4b1d599e1df9693554b1d9a47d06c718a3d6eb81))
- fix(preflight): refuse to invent a MODEL when we know better (#1330) ([1004324](https://github.com/noonghunna/club-3090/commit/1004324f12b59e294c8a10b846f00a63f16019c6))
- fix(deepseek-flash): --load-mode none, not --no-mmap — three slugs could not boot (#1370) ([e942850](https://github.com/noonghunna/club-3090/commit/e9428509e2c411967322e782810611f889135812))
- fix(litellm): route provider via the canonical engine resolver, not a private startswith ([54a8168](https://github.com/noonghunna/club-3090/commit/54a81680ac0a38df0ff290165b9185913bafb11e))
- fix(launch): hardware detector discarded VRAM above the SM floor (#1364) ([4157102](https://github.com/noonghunna/club-3090/commit/415710239bcabd9c2eaa801ed8dce25ea149c99e))
- fix(qwen3.8): ultrafast dflash2 header + 262K shipped default ([71c6869](https://github.com/noonghunna/club-3090/commit/71c686910dd9ad9c0b60b21618a056ee9dce675e))
- fix(bonsai-ternary): reasoning budget 8192 -> 32768, chosen by arithmetic ([7056947](https://github.com/noonghunna/club-3090/commit/70569470d373e65b989cfdda1dddd9ce8b14a9d3))
- fix(report): don't report a borrowed calibration verdict for an unchecked model ([55f192a](https://github.com/noonghunna/club-3090/commit/55f192a82cff79d6dee9eb863a899b67f5b6d031))
- fix(tests): allowlist engine-restart-guard.sh as sourced, not executed ([9001032](https://github.com/noonghunna/club-3090/commit/900103219c399d748d727ec0f50ce4d15368e7e6))
- fix(harness): fail loudly when the engine restarts mid-run ([39343b4](https://github.com/noonghunna/club-3090/commit/39343b464b520fe7f5b7f1fe528cbb7787703c8b))
- fix(searxng): pin the image — `latest` had frozen at a 4-month-old build ([291b80f](https://github.com/noonghunna/club-3090/commit/291b80f39c43c90e7d8cde63fe13c36850172205))
- fix(prism-mtp): digest-pin the engine image; reasoning budget 8192 -> 32768 ([e40d4e0](https://github.com/noonghunna/club-3090/commit/e40d4e0525816c8d4f5ee00b49382c0a1ab4a588))
- fix(sglang): correct the W4A8 tables — decode cost is ~2x what was published ([5005000](https://github.com/noonghunna/club-3090/commit/50050005cfa8a32c4643293746b8accb0f50696f))
- fix(tests): repair the two soak gates — incomplete baseline tree ([1a245f2](https://github.com/noonghunna/club-3090/commit/1a245f2b4e0dcce0eafe9e1a43f9b914b83e46dc))
- fix(tests): diagnose-estate's docker stub emulated one caller's argv ([2dd31e9](https://github.com/noonghunna/club-3090/commit/2dd31e9cc2aef0e1508fb2437e89b15644a298f1))
- fix(harness): exl3 rows are layer-split, not TP=2; drop stale soak-test advice ([6e2316c](https://github.com/noonghunna/club-3090/commit/6e2316c3af27e5a830e1611966f58ba63a22c2f7))
- fix(weights): size_gb was GiB on 8 entries, and one glob claimed a neighbour ([a357048](https://github.com/noonghunna/club-3090/commit/a357048302130b8af702717307376dfca589e217))
- fix(preflight): use the start-anchored matcher on composite docker lines ([ca7f287](https://github.com/noonghunna/club-3090/commit/ca7f28756fdb3b3dce6705b4d588fa4407f31a2a))
- fix(harness): derive "is this container ours?" from the registry, not a hand-list ([5fb41c2](https://github.com/noonghunna/club-3090/commit/5fb41c243d680b3415a7da31303de83bcdfb05fa))
- fix(preflight): size host RAM in decimal GB, matching the -GB header key ([37f74ed](https://github.com/noonghunna/club-3090/commit/37f74ed562d14b1e9dcf8163a88d8f6f5471b7bb))
- fix(weights): stop a variant's verify_glob claiming another variant's artifact ([addfcc7](https://github.com/noonghunna/club-3090/commit/addfcc7e65f95d604b8b796699d5827fef423fd2))
- fix(tests): setup-primary gate must read BOTH registry layers ([39dc7a6](https://github.com/noonghunna/club-3090/commit/39dc7a65dbf2b4f35ec3204d792f9feefd0e52be))
- fix(tests): diagnose-profile exit codes are a contract, not a boolean ([46ca61e](https://github.com/noonghunna/club-3090/commit/46ca61e58cd6fff3954bb29093448b519d63b048))
- fix(tests): stop the resolver test booting a 27B model, and gate the class ([56a342a](https://github.com/noonghunna/club-3090/commit/56a342aab1663c7f894cc1915c54654bd2b2e64a))
- fix(weights): give each Bonsai ternary variant its own verify_glob ([d3eb734](https://github.com/noonghunna/club-3090/commit/d3eb734289e4241d2955332ed697c25d0113f094))
- fix(c3): render drafter-less speculation with the same vocabulary as drafters ([a866d4c](https://github.com/noonghunna/club-3090/commit/a866d4c538a5cf9d3d33b12d955427c24b530f39))
- fix(emit): read weights metadata from BOTH registry layers ([60b9a6f](https://github.com/noonghunna/club-3090/commit/60b9a6ff5b3ead1966100a5bd7f98baeb05c5916))
- fix(harness): per-engine acceptance parsing for vLLM-modern and exl3 ([90d4478](https://github.com/noonghunna/club-3090/commit/90d447885d650dc582e661e6ad83424c8e139846))
- fix(registry-lookup): reap leaked tmp files — 433,584 of them / 130 GB on this rig ([2d272b1](https://github.com/noonghunna/club-3090/commit/2d272b162563a961d7f6d0947a6d214475d5ccff))
- fix(p2p): emit machine-readable interconnect state; make the AR knob universal (#1332) (#1336) ([#1336](https://github.com/noonghunna/club-3090/pull/1336) by @noonghunna)
- fix(p2p): attribute a 2-GPU nccl_only verdict to the operator, not the world>2 gate (#1332) (#1333) ([#1333](https://github.com/noonghunna/club-3090/pull/1333) by @noonghunna)
- fix(tests): re-baseline the kv-calc vllm/dual golden after #1328 ([014499f](https://github.com/noonghunna/club-3090/commit/014499f2fcf97b9328c2f3403f1f991f1b297315))
- fix(kv-calc): count the built-in MTP head as a KV-bearing layer (#1328) ([#1328](https://github.com/noonghunna/club-3090/pull/1328) by @noonghunna)
- fix(sglang): unbreak all 13 composes — CACHE[@] was written with literal \" quotes ([220ba5c](https://github.com/noonghunna/club-3090/commit/220ba5c833c960f9b5b37b826e2594cde9ab8b4e))
- fix(sglang): correct the GDN slot arithmetic and add prefix-cache knobs (#1319) (#1323) ([#1323](https://github.com/noonghunna/club-3090/pull/1323) by @noonghunna)
- fix(report): capture SGLang pool + state-slot lines, which were silently empty (#1320) ([#1320](https://github.com/noonghunna/club-3090/pull/1320) by @noonghunna)
- fix(tests): isolate the pytest fixtures from the machine's REAL local layer (#1318) ([#1318](https://github.com/noonghunna/club-3090/pull/1318) by @noonghunna)
- fix(tests): repair the 34 dead pytest tests and wire them into the gate (#1316) (#1317) ([#1317](https://github.com/noonghunna/club-3090/pull/1317) by @noonghunna)
- fix(spec-sweep): match the container to the arm's engine, not a hardcoded vllm ([1c731db](https://github.com/noonghunna/club-3090/commit/1c731dba28209372e4f0c583c10ba2a7e217eb97))
- fix(tests): the bare-grep scanner must not fire on comments ([a2a0ecf](https://github.com/noonghunna/club-3090/commit/a2a0ecf0719d6aa5c7a8efff6daf904122ddcd22))
- fix(setup): retry weight downloads instead of dying on one stall ([05ee8ab](https://github.com/noonghunna/club-3090/commit/05ee8ab84f7f31396d242108000558f935eb2ed0))
- fix(setup): surface WITH_ASSISTANT_DRAFT and the SPEC_N=0 way out ([ed7bda1](https://github.com/noonghunna/club-3090/commit/ed7bda142021c8a7d83a627d6b697d1ef4401821))
- fix(setup): fetch awq for gemma-4-26b-a4b, not the archived autoround tier ([b533560](https://github.com/noonghunna/club-3090/commit/b533560941c0bf3637c1fa0c9384d875dd082e39))
- fix(compose): run cache-mounting vLLM composes with the host GID ([39fd8c2](https://github.com/noonghunna/club-3090/commit/39fd8c2a6952f0a5f19983e1527a0a30528cbca2))
- fix(profiles): attribute hypermax API validation probes ([c762f38](https://github.com/noonghunna/club-3090/commit/c762f38bca25c6e05c32fcd37ec61776be32ebb0))
- fix(preflight): stop capturing a trailing backslash from escaped JSON paths ([7821734](https://github.com/noonghunna/club-3090/commit/78217346a6cd99d7ea41213f732ab648ff82ea3c))
- fix(probe): a zero acceptance gauge is unpopulated, not a dead drafter ([e41bc83](https://github.com/noonghunna/club-3090/commit/e41bc83ce671f3c4e63039153c1b836bb6b2b575))
- fix(probe): freeze the depth history — the feedback loop, not truncation ([c4a5fc2](https://github.com/noonghunna/club-3090/commit/c4a5fc2de6ed6d3d55f0e7112ed4590f3a17af11))
- fix(probe): breadth must not claim eviction it cannot observe (#1299) ([13cfc2e](https://github.com/noonghunna/club-3090/commit/13cfc2ec205a83ea1735964ec586e5d6677c8573))
- fix(probe): stop the depth probe poisoning its own history ([44bb832](https://github.com/noonghunna/club-3090/commit/44bb8322b45b336d01a57f5631c807bfba252f74))
- fix(probe): measure decode when the engine sends usage only once ([a875917](https://github.com/noonghunna/club-3090/commit/a87591738bb0a90110292ba517291a83f1e976b6))
- fix(compose): honour ESTATE_PORT in the 14 composes that ignored it ([7ff2b4d](https://github.com/noonghunna/club-3090/commit/7ff2b4d4c619eeacbc2140ac864a1c80f1379a37))
- fix(sglang): make the healthcheck able to fail when the service is unreachable ([36c339c](https://github.com/noonghunna/club-3090/commit/36c339ca5cd6d138494c3a0ce0d819b53f854090))
- fix(sglang): pass --enable-cache-report so prefix-cache hits reach clients ([34f7a6e](https://github.com/noonghunna/club-3090/commit/34f7a6eeb676b9d70ae8295abfaa9265b8b1fcfc))
- fix(sglang): a doc comment after a line continuation silently dropped every flag after it (#1296) ([#1296](https://github.com/noonghunna/club-3090/pull/1296) by @noonghunna)
- fix(soak): stop the client-timing ceiling deleting engine-reported decode rates (#1291) ([#1291](https://github.com/noonghunna/club-3090/pull/1291) by @noonghunna)
- fix(tests): give the fixture an `nvidia-smi -L` arm, and assert the precondition it enables (#1289) ([#1289](https://github.com/noonghunna/club-3090/pull/1289) by @noonghunna)
- fix(scripts): use `command grep` for every executed grep, and gate it repo-wide (#1287) ([#1287](https://github.com/noonghunna/club-3090/pull/1287) by @noonghunna)
- fix(harness): resolve engine family in ONE place; SGLang no longer mis-routes to the llama.cpp path (#1285) ([#1285](https://github.com/noonghunna/club-3090/pull/1285) by @noonghunna)
- fix(soak): read the engine's decode counter, and stop rendering unmeasurable turns as 0.0 (#1284) ([#1284](https://github.com/noonghunna/club-3090/pull/1284) by @noonghunna)
- fix(rig-state): resolve the power cap from its unit, and stop p2p_gpu_count emitting two lines (#1279, #1281) (#1283) ([#1283](https://github.com/noonghunna/club-3090/pull/1283) by @noonghunna)
- fix(quality): refuse a bare TOTAL when a pack scores 0/N (cause-agnostic structural-zero guard) (#1278) ([#1278](https://github.com/noonghunna/club-3090/pull/1278) by @noonghunna)
- fix(glm): point the drafter-missing remediation at scripts/setup.sh, not an out-of-repo wrapper (#1276) ([#1276](https://github.com/noonghunna/club-3090/pull/1276) by @noonghunna)
- fix(cockpit): probe the verify_glob's own dir for ABSENT, so a deleted nested-glob variant stops reporting "partial" (#1275) ([#1275](https://github.com/noonghunna/club-3090/pull/1275) by @noonghunna)
- fix(harness): resolve sglang-* containers to ENGINE_KIND=sglang (5 sites) (#1263) ([#1263](https://github.com/noonghunna/club-3090/pull/1263) by @noonghunna)
- fix(qwen3.8/llama.cpp): resolve the INSTRUCT sampler row in the entrypoint, once (#1258) ([#1258](https://github.com/noonghunna/club-3090/pull/1258) by @noonghunna)
- fix(glm): vendor a minja-compatible chat template — tool calling works (#1255) ([#1255](https://github.com/noonghunna/club-3090/pull/1255) by @noonghunna)
- fix(glm): document that tool calling is dead on llama.cpp, and stop printing a Qwen hint for it (#1254) ([#1254](https://github.com/noonghunna/club-3090/pull/1254) by @noonghunna)
- fix(qwen3.8): sgl super* slugs cannot fetch their drafter; SpecDecoding tail blank on 2 of 3 engines (#1252) ([#1252](https://github.com/noonghunna/club-3090/pull/1252) by @noonghunna)
- fix(harness): make acceptance + endpoint detection engine-aware (#1249) ([#1249](https://github.com/noonghunna/club-3090/pull/1249) by @noonghunna)
- fix(launchers): a user-set env var must win over the #246 profile default (#1243) ([#1243](https://github.com/noonghunna/club-3090/pull/1243) by @noonghunna)
- fix(residency): charge a single-card drafter to that card only (#1233) (#1236) ([#1236](https://github.com/noonghunna/club-3090/pull/1236) by @noonghunna)
- fix(quality-test): survive pipx two-token shebangs under set -e (#1234) ([#1234](https://github.com/noonghunna/club-3090/pull/1234) by @mgabor3141)


### 📊 Benchmarks + cross-rig data

- results: SGLang Qwen3.8-27B W4A8 + DFlash2 TP=4 bench (2026-09-09) ([1ed9cec](https://github.com/noonghunna/club-3090/commit/1ed9cec5c96311dfac26ab54bed9ebd39f93eaa4))


### 📝 Documentation

- docs(agents): working on a rig + fix stale defaults, examples, Tier 0 list (#1494) ([#1494](https://github.com/noonghunna/club-3090/pull/1494) by @noonghunna)
- docs(settings): last stale .env / kv-offload pointers (#1466) ([0960b00](https://github.com/noonghunna/club-3090/commit/0960b00ca26d95d84f6bb0dc38e3cdd1ec636d95))
- docs(config): point settings docs at ~/.config/club-3090 (#1466) (#1484) ([#1484](https://github.com/noonghunna/club-3090/pull/1484) by @noonghunna)
- docs(p2p): SGLang custom all-reduce — measured, kept off; fix stale SGLang note ([90299ef](https://github.com/noonghunna/club-3090/commit/90299ef77a6d623a8efffd313cc5851fc6b66784))
- docs(p2p): reference rig reproduces the Proxmox patched-P2P route ([c0be776](https://github.com/noonghunna/club-3090/commit/c0be776a431b14f3b057889d3ededca22db23cb6))
- docs: add validated Proxmox VFIO P2P route (#1455) ([#1455](https://github.com/noonghunna/club-3090/pull/1455) by @ensingerphilipp)
- docs(agents): add a Cautions section for coding agents ([4c2ad22](https://github.com/noonghunna/club-3090/commit/4c2ad2260d068282fa65741bb65889cef43f30e1))
- docs(agents): Hermes — recommend model.reasoning_echo for the club model ([059d071](https://github.com/noonghunna/club-3090/commit/059d0713999ad50a001cf725ade004e5a308c0b3))
- docs(agents): Hermes — resume, subagent cap, tools, status bar, live checks ([6df2b86](https://github.com/noonghunna/club-3090/commit/6df2b86b06f82684605697da517513fa073f8eb8))
- docs(agents): Claude Code section — verified on the reference rig, model id, what doesn't carry over ([a942bb5](https://github.com/noonghunna/club-3090/commit/a942bb5ac3197d486385bdf8abb2f0ee20af867c))
- docs(quality): describe run metadata and engine sampling flags in words (fixes test-quality-passthrough) ([349ebaf](https://github.com/noonghunna/club-3090/commit/349ebaf2193516c440ba87b0002dead0bd62aea3))
- docs(upstream): correct the stale ReplaySSM and qwen3coder rows ([e6e64d3](https://github.com/noonghunna/club-3090/commit/e6e64d332043d3229c29d972238f75e0646029cd))
- docs(byo): add Qwen3.8-27B FP8 + MTP row to the swap-weights examples ([9eddf1b](https://github.com/noonghunna/club-3090/commit/9eddf1b01194cce4984dbfdf91a3f34af831a3c0))
- docs(glm): correct the fork-image base in #28786 row; fix leloch RFC ref ([e3c967e](https://github.com/noonghunna/club-3090/commit/e3c967e1356763bba0d69a8631d8b45f91c9a9f5))
- docs(glm): record #28786 upstream fix; GLM template now fork-only (#1430) ([#1430](https://github.com/noonghunna/club-3090/pull/1430) by @paulp83)
- docs(qwen38): close out community runs #1380 / #1381 ([0a5ee5a](https://github.com/noonghunna/club-3090/commit/0a5ee5ae703a4b863a5514afdf2daa5b3dcfb477))
- docs: link the ThinkingCap (#1418) and KV offload (#1419) announcements ([701071c](https://github.com/noonghunna/club-3090/commit/701071c2ce0442ec6e40b1c1010d7abb5af9362c))
- docs(img): ThinkingCap-Qwen3.8 vs base Qwen3.8 chart for the announcement ([da4b1e8](https://github.com/noonghunna/club-3090/commit/da4b1e8d81ac3a70e304003c5dbbbae30a90bfc8))
- docs(env): document expandable_segments:False as an opt-in vLLM KV-pool lever ([63e99bd](https://github.com/noonghunna/club-3090/commit/63e99bd8615e8697c900cdc014c3f0defbb52dab))
- docs(sglang): refresh SGLANG.md at-a-glance to the shipped defaults ([5168715](https://github.com/noonghunna/club-3090/commit/5168715ba85eb8bcd4daf3e1ea8dcff767c010cc))
- docs(thinkingcap/sglang): dual-fast replica booted + verify-full PASS (2026-09-25) ([f38159f](https://github.com/noonghunna/club-3090/commit/f38159fb02a52f66fd9d9433ffb936da6627a774))
- docs(upstream): sgl#33713 re-tested on v0.5.20 — HiCache still write-only ([d783bf6](https://github.com/noonghunna/club-3090/commit/d783bf6ba73f5a60e007b5a046a6695e6cdbb2a5))
- docs(readme): restructure the README around "pick your path" (disc #498) ([71cea4f](https://github.com/noonghunna/club-3090/commit/71cea4f20ae1bba7f155464c7c866757e1a1e320))
- docs: rebuild the card pages around a generated slug table; add RUN_EVALS.md ([562c805](https://github.com/noonghunna/club-3090/commit/562c8051d968f7fd98cd044fcac87eb565bee15f))
- docs(qwen38-single-iq4xs): q4 KV does not cap the slug below Production ([d97118b](https://github.com/noonghunna/club-3090/commit/d97118b84691d1dc139597e5faf43bb467b58242))
- docs(benchmarks): record community Qwen3.8 runs #1339, #1380, #1381 ([15c0e44](https://github.com/noonghunna/club-3090/commit/15c0e44d615cfadf04d6b22a5ef0aab7e7c196d3))
- docs: ik-llama needs its OWN engine profile — 'split llama-cpp-local' misnamed the cause ([5c7d481](https://github.com/noonghunna/club-3090/commit/5c7d481f0ae7420c60f86b5eac6794961d146aba))
- docs(engine-flags): #1370 closed — strike the --no-mmap pin-drift row, note the new guard ([daa9957](https://github.com/noonghunna/club-3090/commit/daa99572a3093ee52fd44e58361ff55475a9e487))
- docs(engine-flags): refresh §7 against 4dc310a6 — #1369 and #1373 changed four of its rows ([55d8d11](https://github.com/noonghunna/club-3090/commit/55d8d1146a6f878376648ae5414ab10480901a76))
- docs(agents): tree-wide guards are Tier 0 — they run on every change, whatever the diff touches ([27388d3](https://github.com/noonghunna/club-3090/commit/27388d3957508c02b499e20f7ba5c6d9e851208a))
- docs: index ENGINE_FLAGS.md in the docs README ([daa2b28](https://github.com/noonghunna/club-3090/commit/daa2b2821a5c601ba446d02e76aa6d76772ab0f1))
- docs: add the engine-flag inventory (ENGINE_FLAGS.md) + link it from ARCHITECTURE ([96028d4](https://github.com/noonghunna/club-3090/commit/96028d4f03ad4cd4d17b2caafc5c618cf5a441f1))
- docs(exl3): both cpumoe headers stated a CPU-resident share the default had outgrown ([8c41137](https://github.com/noonghunna/club-3090/commit/8c41137e2c23de89b96440aa69869cb0236ad66f))
- docs(agents): sharpen the test-sweep scoping rule with the three cases that bite ([5a8be46](https://github.com/noonghunna/club-3090/commit/5a8be4654f592ecce0be6575ae80916b2eb20d7b))
- docs(bonsai-ternary): record that the 8192 reasoning budget TRUNCATES ([1d408cf](https://github.com/noonghunna/club-3090/commit/1d408cfaf47640c700042ecd5ee3ec15d67fad92))
- docs(exl3): retract the stale "container is ~9% slower" status_note ([0916a11](https://github.com/noonghunna/club-3090/commit/0916a11d32c1d101e043e892545668e364ad9b6a))
- docs(qwen3.8-27b): caveat the multi4/multi8 composes — fa2-fp8kv runs outside its validated envelope ([e5a212d](https://github.com/noonghunna/club-3090/commit/e5a212d66683c93aab917fd7c49ce3d694b9ac34))
- docs(prism-mtp): record the measured 8-pack in the compose header ([362ed54](https://github.com/noonghunna/club-3090/commit/362ed5410c7ade4541b1eb06aeeb4dc0b88dd5ae))
- docs(upstream): sglang #37500 + #36507 shipped in v0.5.20 ([552dd9e](https://github.com/noonghunna/club-3090/commit/552dd9ec47f9f3536ac3cd36c66eae2aa434946a))
- docs(p2p): re-land the #1332 sections, with the three wrong claims corrected ([fa79165](https://github.com/noonghunna/club-3090/commit/fa79165737ca29d76f8cff2fea3dea56d0b8d052))
- docs(p2p): the hard-reset failure mode, a ladder tier, and the DKMS initramfs trap (#1332) (#1335) ([#1335](https://github.com/noonghunna/club-3090/pull/1335) by @noonghunna)
- docs(qwen3.8-27b): the fp8 header table was the int4 sibling's, not a measurement ([af169b1](https://github.com/noonghunna/club-3090/commit/af169b1f93f6a69729e3fa94907e63a212f01397))
- docs(qwen3.8-27b): retract the dual-fast decode regression — it was the gate harness ([539860f](https://github.com/noonghunna/club-3090/commit/539860ffa0cbb9ec55a45965275b41a0b8e8f0d1))
- docs(qwen3.8-27b): refresh dual-fast citations after the 2-session default ([51606fd](https://github.com/noonghunna/club-3090/commit/51606fd118be62fe46b1a8125ff3a5e5d27cb1c3))
- docs(sglang): rewrite SGLANG.md for the shipped state; archive the 2026-05 EAGLE-3 page ([813b18d](https://github.com/noonghunna/club-3090/commit/813b18dfee5977eda8dc2369149856929cf79a12))
- docs: record the measured fp8-vs-bf16 decode A/B for dual-ultrafast ([68e8f30](https://github.com/noonghunna/club-3090/commit/68e8f3024e89c0eb15278b4f4aaa3e81ebc21d1e))
- docs(upstream): close the v0.29.0 mamba-align trigger — it fires on DFlash2 and buys +0.1% ([8e3f153](https://github.com/noonghunna/club-3090/commit/8e3f1533deb5aadd6fadd708899484281dc7380a))
- docs(sglang): record the measured mamba-state-slot / concurrency arithmetic in the dual composes (#1292) ([#1292](https://github.com/noonghunna/club-3090/pull/1292) by @noonghunna)
- docs(upstream): the align/DFlash2 crash was already filed AND is fixed in v0.29.0 ([c3551f5](https://github.com/noonghunna/club-3090/commit/c3551f52357111ae59cf46fd0d2eeda848a0aafb))
- docs(sglang): the DFlash2 headers named a drafter that stopped being the default in #1237 (#1266) ([#1266](https://github.com/noonghunna/club-3090/pull/1266) by @noonghunna)
- docs(qwen3.8/vllm): correct the --prefix-match-unit comment — pmu is also inert under MTP (#1262) ([#1262](https://github.com/noonghunna/club-3090/pull/1262) by @noonghunna)
- docs(sglang): warn that return_token_ids / return_prompt_token_ids / return_meta_info are refused under streaming (#1257) ([#1257](https://github.com/noonghunna/club-3090/pull/1257) by @noonghunna)
- docs(upstream): track ggml-org/llama.cpp#28786 (minja numeric dotted access) (#1256) ([#1256](https://github.com/noonghunna/club-3090/pull/1256) by @noonghunna)
- docs(upstream): track sglang#39096 — preferred-sampling-params inert on the chat path ([54bce70](https://github.com/noonghunna/club-3090/commit/54bce708bcba3537839b454eed5ddeea999f1015))
- docs(img): add SGLang-vs-vLLM chart + sgl c3 catalog screenshot ([a46d716](https://github.com/noonghunna/club-3090/commit/a46d716de8095abb3dbffede999c3b5ca2a6968e))
- docs(glm-5.3-flash): flag that -ub 2048 can crash long prefill (#1238) (#1241) ([#1241](https://github.com/noonghunna/club-3090/pull/1241) by @noonghunna)
- docs(qwen3.8-27b): fix reasoning-effort and thinking-default drift (#1239) (#1240) ([#1240](https://github.com/noonghunna/club-3090/pull/1240) by @noonghunna)


### 🧹 Maintenance

- test(c3): derive the curated profile-template count from the registry (#1496) ([#1496](https://github.com/noonghunna/club-3090/pull/1496) by @noonghunna)
- test(c3): stop tests leaving temp dirs on sys.path (#1493) ([#1493](https://github.com/noonghunna/club-3090/pull/1493) by @noonghunna)
- chore(settings): point stale hints at settings.sh (#1466) (#1488) ([#1488](https://github.com/noonghunna/club-3090/pull/1488) by @noonghunna)
- chore(services): bump and pin LiteLLM, Qdrant, Open WebUI, SearXNG (#1436) ([#1436](https://github.com/noonghunna/club-3090/pull/1436) by @noonghunna)
- test(engine-detection): assert sglang is in report.sh's override arm, not its exact shape (#1423) ([#1423](https://github.com/noonghunna/club-3090/pull/1423) by @noonghunna)
- test(spec-toggle): ship the real fa2 envelope helper into the stubbed /etc (#1358) ([1ff5ef6](https://github.com/noonghunna/club-3090/commit/1ff5ef68f1ecffdea82907347ce05c8e058a4038))
- chore(club3090): migrate 28 composes --no-mmap -> --load-mode none (#1370 follow-up) ([47eb544](https://github.com/noonghunna/club-3090/commit/47eb5444eadc1716d9d84a7e2e774995e1fe74c8))
- refactor(launch): retire the #246 Phase 1 KV-dtype injector — it was inert on every card (#1371) ([d367b10](https://github.com/noonghunna/club-3090/commit/d367b1014165e3ce0aaf72366e90027212f7732c))
- test(launch): neutralize the double-invocation harness for test-tests-never-launch ([e0b63af](https://github.com/noonghunna/club-3090/commit/e0b63af4837e1a525fdb7f9cd40ba4771c695f0f))
- test(launch): #1363 matrix guard — every slug x every hardware profile ([8085383](https://github.com/noonghunna/club-3090/commit/808538372e4a9fd7245827596899d7b17e720eb1))
- refactor(launch): key the concurrency knob by EngineProfile.type, not engine id ([ffb655f](https://github.com/noonghunna/club-3090/commit/ffb655fad42043dffccc53f5ab19cea0263fd70c))
- chore(sglang): bump the stable pin v0.5.19 -> v0.5.20 ([a2a3dea](https://github.com/noonghunna/club-3090/commit/a2a3deaaef85c0114bb532213ccdaf5104ac476e))
- test(engine-kind): gate hand-listed container prefixes (arm 5) ([702c89e](https://github.com/noonghunna/club-3090/commit/702c89e8ffe59a029f3fd3bc4cff1822b71f11dc))
- chore(owui): bump Open WebUI v0.11.0 -> v0.11.3 ([3520076](https://github.com/noonghunna/club-3090/commit/35200765a080e07e36fa4ba28722947b0e00a379))
- test: move the remaining fixture ports above the product port space ([397dd82](https://github.com/noonghunna/club-3090/commit/397dd82ca37ade92d0f6f07c5a3aaeb26b5cba34))
- test(bench-capture): move fixture ports above the product port space ([d117763](https://github.com/noonghunna/club-3090/commit/d117763657da0de53341be3ab8f4fd08c7855de7))
- test(compose): gate env vars that are declared but read by nothing ([3086161](https://github.com/noonghunna/club-3090/commit/3086161a3dca53e2297f9886357d8c3ca494fd28))
- test(compose): gate malformed array quoting, and fix a blind spot that hid it ([69f017a](https://github.com/noonghunna/club-3090/commit/69f017aa3f4b084e8d7ec8b228c35b0651970275))
- test(fa2): import importlib.metadata before patching pathlib.Path ([3c27e8e](https://github.com/noonghunna/club-3090/commit/3c27e8eb4c22bc36e718e3ce3b60e69c1959ba61))
- test(qwen38): record native FA2 validation and memory limits ([099bbe4](https://github.com/noonghunna/club-3090/commit/099bbe43112cfe8b2e1c8adcb8b1c37c9f7d75a3))
- test(qwen38): finish hypermax context vision and quality validation ([eae04ac](https://github.com/noonghunna/club-3090/commit/eae04ace695533104a123eaf985460e0df6dddba))
- test(probe): cover the wall basis and pin the basis order ([eb36423](https://github.com/noonghunna/club-3090/commit/eb36423bad2c62e64df3268ec8f015e72ae919f1))


### 🧹 Other

- agents: Hermes Agent setup (scripts/hermes-setup.sh + docs), tested through the gateway (#1459) ([#1459](https://github.com/noonghunna/club-3090/pull/1459) by @noonghunna)
- agents: pi setup (scripts/pi-setup.sh + docs), tested through the gateway (#1451) ([#1451](https://github.com/noonghunna/club-3090/pull/1451) by @noonghunna)
- omp: don't limit omp to club models; meter section; Claude Code status on vLLM (#1449) ([#1449](https://github.com/noonghunna/club-3090/pull/1449) by @noonghunna)
- agents: statusline cache meter, gateway/models.yml snippets, fallback set-up + enabledModels (#1448) ([#1448](https://github.com/noonghunna/club-3090/pull/1448) by @noonghunna)
- omp: pin the Qwen3.8 reply cap; document what the gateway sets; link the doug.sh articles (#1445) ([#1445](https://github.com/noonghunna/club-3090/pull/1445) by @noonghunna)
- litellm: move rig-specific routes out of the tracked catalog into a gitignored config.local.yaml (#1446) ([#1446](https://github.com/noonghunna/club-3090/pull/1446) by @noonghunna)
- perf(sglang): --sleep-on-idle on every SGLang compose (idle CPU ~2 cores -> <0.5) (#1443) ([#1443](https://github.com/noonghunna/club-3090/pull/1443) by @noonghunna)
- Fix ExLlamaV3 benchmark telemetry (#1420) ([#1420](https://github.com/noonghunna/club-3090/pull/1420) by @TreyThomasCodes)
- Fix test-bench-capture triad branch for numpy-less rigs (#1422) ([#1422](https://github.com/noonghunna/club-3090/pull/1422) by @paulp83)
- perf(registry-emit): parse composes with libyaml's CSafeLoader when available (#1382) ([6290828](https://github.com/noonghunna/club-3090/commit/6290828e3d31bbfec774c45a4580ee6f1d679c6e))
- perf(setup): picker reads the catalog, GPUs and registry once (#1382) ([fcf7090](https://github.com/noonghunna/club-3090/commit/fcf7090fe2a7daf899f6004a556672c9a16ffecd))
- perf(compose-meta): read header fields without forking per line (#1382) ([121e80c](https://github.com/noonghunna/club-3090/commit/121e80cc8bfd8f9ecf39fb37a6b337830c5d7e34))
- litellm: emit hosted_vllm provider for local vLLM routes ([d63bb8d](https://github.com/noonghunna/club-3090/commit/d63bb8d9e27f3b449c05e5e8e081bf90af020faa))
- Revert "docs(p2p): the hard-reset failure mode, a ladder tier, and the DKMS initramfs trap (#1332) (#1335)" ([5596a92](https://github.com/noonghunna/club-3090/commit/5596a92daafb850fbfbccb2c26a1a815fed65a85))
- Track sglang#32468 — draft embed/lm_head freed after KV pool sizing ([1e4f6e2](https://github.com/noonghunna/club-3090/commit/1e4f6e245ab3b09316effcd3313fd94c4c8a6faa))
- Retract our #33713 root cause; #33450 does not apply to GDN ([c69618f](https://github.com/noonghunna/club-3090/commit/c69618fb4cfe9a4fcd0795a09c6447b7eb9dc0b0))
- Track five SGLang upstream rows from the concurrency investigation ([080c86d](https://github.com/noonghunna/club-3090/commit/080c86d9959e59c4077acab99ed210f5b9c97004))
- qwen3.8-27b: measure W4A8 on vLLM ultrafast, ship it ON, and correct the SGLang W4A8 comments (#1315) ([#1315](https://github.com/noonghunna/club-3090/pull/1315) by @noonghunna)
- Merge #1313: match the spec-sweep container to the arm's engine (@paulp83) ([#1313](https://github.com/noonghunna/club-3090/pull/1313) by @noonghunna)
- Merge #1314: the bare-grep scanner must not fire on comments ([#1314](https://github.com/noonghunna/club-3090/pull/1314) by @noonghunna)
- Merge #1312: fix the gemma setup-then-switch journey (#1303, #1304, #1305) ([#1312](https://github.com/noonghunna/club-3090/pull/1312) by @noonghunna)
- Merge #1311: dual-ultrafast gains fp8 KV + FlashAttn via the FA2 plugin ([#1311](https://github.com/noonghunna/club-3090/pull/1311) by @noonghunna)
- Merge #1310: run cache-mounting vLLM composes with the host GID ([#1310](https://github.com/noonghunna/club-3090/pull/1310) by @noonghunna)
- Merge #1274: FlashAttention FP8 KV on consumer SM — lands the ultramax tier (@AntonProkopyev) ([#1274](https://github.com/noonghunna/club-3090/pull/1274) by @noonghunna)
- Merge #1307: preflight — stop capturing a trailing backslash from escaped JSON drafter paths ([#1307](https://github.com/noonghunna/club-3090/pull/1307) by @noonghunna)
- Merge #1302: probe concurrent mode — two deep sessions, then compact one ([#1302](https://github.com/noonghunna/club-3090/pull/1302) by @noonghunna)
- Merge #1298: deep-context-probe — an instrument that reaches 140K, and four fixes to itself ([#1298](https://github.com/noonghunna/club-3090/pull/1298) by @noonghunna)
- Merge #1301: emit prefix-cache hits, fix the SGLang healthcheck, honour ESTATE_PORT ([#1301](https://github.com/noonghunna/club-3090/pull/1301) by @noonghunna)
- Merge #1248: vendor @A1RM4X's SGLang W4A8 patch and wire it to every sgl/ slug ([#1248](https://github.com/noonghunna/club-3090/pull/1248) by @noonghunna)
- sglang: AutoRound W4A8 v0.5.19 patch + installer + patches.yml entry (shape-guard fix) ([71e8ae9](https://github.com/noonghunna/club-3090/commit/71e8ae9232cd7bf76af0bb293406d8d03d5d0563))



[Pin: `git checkout v0.12.0`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.11.0...v0.12.0)
## v0.11.0 — 2026-09-10


### ⚠️ Cliffs, gotchas, regressions

- Merge #1150: allow --spec-file in the quality-test doc drift guard (regression from #1143) ([#1150](https://github.com/noonghunna/club-3090/pull/1150) by @noonghunna)


### ✨ Features

- feat(glm-5.3-flash): add static-offload tier for low-host-RAM rigs (#1235) ([#1235](https://github.com/noonghunna/club-3090/pull/1235) by @noonghunna)
- feat(glm-5.3-flash): add DevQuasar Q2_K + Q3_K_M K-quant slugs (#1231) ([#1231](https://github.com/noonghunna/club-3090/pull/1231) by @noonghunna)
- feat(engines): register sglang-stable + define the sglang patch contract (#1228) ([#1228](https://github.com/noonghunna/club-3090/pull/1228) by @noonghunna)
- feat(scripts): add compaction-probe — does TPS drop AFTER a compaction? ([1f8181b](https://github.com/noonghunna/club-3090/commit/1f8181bc2ec7eb9056c3ea3eafb8d0091e0d07be))
- feat(c3): manage the local layer from the cockpit — list, rename, edit, remove (#1153) (#1210) ([#1210](https://github.com/noonghunna/club-3090/pull/1210) by @noonghunna)
- feat(catalog): rename + update for local entries — the shadowing remedy we owed (#1209) ([#1209](https://github.com/noonghunna/club-3090/pull/1209) by @noonghunna)
- feat(switch): `--local` filter and a provenance marker on local rows (#1207) ([#1207](https://github.com/noonghunna/club-3090/pull/1207) by @noonghunna)
- feat(catalog): scripts/catalog.sh + a local ENGINE layer, so a user's own build can register (#1202 P4) (#1206) ([#1206](https://github.com/noonghunna/club-3090/pull/1206) by @noonghunna)
- feat(profiles): hard-cut the `local/` namespace — local slugs take `<engine>/<name>` (#1205) ([#1205](https://github.com/noonghunna/club-3090/pull/1205) by @noonghunna)
- feat(profiles): make catalog provenance a first-class `origin` field; core wins (#1204) ([#1204](https://github.com/noonghunna/club-3090/pull/1204) by @noonghunna)
- feat(c3): used/total anchor line + full-width warnings in the VRAM split ([f39f2a5](https://github.com/noonghunna/club-3090/commit/f39f2a52ae8c16769e37aa5bd127229ca0344707))
- feat(qwen3.8-27b): port the MAMBA_BLOCK_SIZE knob to the other seven vLLM composes ([4ce708f](https://github.com/noonghunna/club-3090/commit/4ce708f34b3558906c46461927501f7e70b4f993))
- feat(qwen3.8-27b): dual-fast MAMBA_BLOCK_SIZE knob — recovers ~20% effective KV pool on hybrid-GDN (2x242K concurrent, 0 preemptions) ([9805097](https://github.com/noonghunna/club-3090/commit/98050979e3820dab99eb445aeacd53beda454f57))
- feat(vram-breakdown): join CUDA ordinals to GPUs by PCI bus id (#1118 §4 option A) + RESULT-1118 ([8368bd7](https://github.com/noonghunna/club-3090/commit/8368bd75f417ed2ed16c76dac360c33396c43850))
- feat(c3): estate-bar VRAM breakdown with per-GPU drill-down (#1118) ([ee8126d](https://github.com/noonghunna/club-3090/commit/ee8126d2e9100a83cf286174f1faf4bea1167fe3))
- feat(vram-breakdown): --json mode + negative-unaccounted clamp (#1118) ([53e7090](https://github.com/noonghunna/club-3090/commit/53e70901cdfe54daffb87c9e593c3f2c40ff8d53))
- feat(glm-5.3-flash): wire KV_TYPE on the dual moecache compose (default f16) ([138cfc9](https://github.com/noonghunna/club-3090/commit/138cfc9c11243e06ef568cb69fe1a94c0dd730ff))
- feat(profiles): demote.py — remove a local model, with an end-to-end lifecycle test ([68e5fe4](https://github.com/noonghunna/club-3090/commit/68e5fe434d33784eca16bb920b595a637c75ada0))
- feat(c3): view the compose behind a slug — [c] opens it, read-only ([d2e0d56](https://github.com/noonghunna/club-3090/commit/d2e0d56375863c349f2b4746086572dca64b718d))
- feat(c3): Doctor's checks are a keyboard list — ↑/↓ pick, ⏎ runs ([1d6c753](https://github.com/noonghunna/club-3090/commit/1d6c75338fbc5d8694e777dc61a2852bd5fe49cc))
- feat(c3): Route-K — ① accepts a compose you already wrote (#1153) ([8ee1c08](https://github.com/noonghunna/club-3090/commit/8ee1c080811bfe77cfb02cba672f738ade619c24))
- feat(promote): state the written layer, pose the default, and un-break the test fixture (#1142) ([f248b2d](https://github.com/noonghunna/club-3090/commit/f248b2d5321bc697d6dbcb75e1bc3b08f2723651))
- feat(byom): keep local models out of the curated port band; warn what destroys the layer ([514040f](https://github.com/noonghunna/club-3090/commit/514040f12c335a1b29d89d0195db3e36bd199f0b))
- feat(qwen3.8-27b): wire ASYNC_SCHED=off on dual-max — vllm#50021 mitigation (1), drafter kept ([cc6a494](https://github.com/noonghunna/club-3090/commit/cc6a4940b122875882f1ad1cd6ce2a740f2a8dfc))
- feat(qwen3.8-27b): bare passthroughs for VLLM_CACHE_ROOT and VLLM_LOG_STATS_INTERVAL ([a9061d9](https://github.com/noonghunna/club-3090/commit/a9061d96adaf8c48b963f5163d94b6126cdebfe3))
- feat(qwen3.8-27b): ship thinking by default across all 22 composes ([19e3e82](https://github.com/noonghunna/club-3090/commit/19e3e8230d3c7e682e2be92ea71f8c856b5d0a26))
- feat(bench): break the VRAM figure down by component in CAPTURE: VRAM ([2d78472](https://github.com/noonghunna/club-3090/commit/2d784720f44fa93e25268e747ef0d513dd7686ff))
- feat(deepseek-vision): catalog the model; make -t portable across 19 composes ([6f4958a](https://github.com/noonghunna/club-3090/commit/6f4958a8fb42878972fbdefc4ecf9710b74ca0ef))
- feat(engine): pin GLM + Qwen Flash to moe-cache v1.6-rc0 ([9383525](https://github.com/noonghunna/club-3090/commit/9383525410dba40403f858aa23f617c58a86ce43))
- feat(bench): add the decode-at-depth leg the suite was missing ([73064e4](https://github.com/noonghunna/club-3090/commit/73064e434920f89a95bef0429d7cdbdc438b4a6b))
- feat(preflight,report): detect THP shmem misconfiguration on offload slugs ([402d326](https://github.com/noonghunna/club-3090/commit/402d326c7c19834e41c7d7e7541b43a98ca06673))
- feat(concurrency-probe): warn when served slots < requested N ([005f92f](https://github.com/noonghunna/club-3090/commit/005f92f03652ac602cfe7359e8d136e32385b027))
- feat(scripts): add hugepages.sh — THP check/apply for CPU-offload MoE ([0091e54](https://github.com/noonghunna/club-3090/commit/0091e5420d1d541b106b97cd9049785589735d83))
- feat(glm-5.3-flash): add the UD-IQ3_XXS quant (dual/multi4/multi8) ([dfd4917](https://github.com/noonghunna/club-3090/commit/dfd49173f9f5614cc134215bc5f097a6996ff90d))
- feat(inkling): migrate to the v1.5 engine; set the vendor sampler ([0d1ed5d](https://github.com/noonghunna/club-3090/commit/0d1ed5d5b15c1c0ffcb93f1d1cd3588823404017))
- feat(deepseek): migrate the moecache slugs to the v1.5 engine ([8bcdb7b](https://github.com/noonghunna/club-3090/commit/8bcdb7b7341a5185d51ce6e103d61dd9869f2056))
- feat(qwen3.8-flash-next): ship ngram-mod speculation ON by default ([c39fad8](https://github.com/noonghunna/club-3090/commit/c39fad8790769bad882ea0ff3d998459903de74e))
- feat(qwen3.8-flash-next): catalog the model (dual/multi4/multi8) ([0472a19](https://github.com/noonghunna/club-3090/commit/0472a19d5e2d8cce1f202f092afb48861a7af7a2))
- feat(verify-full): add capability-probed vision check [10/10] ([7765403](https://github.com/noonghunna/club-3090/commit/776540368454ffc2c8ac2c59bcc3e8c87131427f))
- feat(catalog): add GLM-5.3-Flash — 3 slugs on moe-cache engine v1.5 ([3144113](https://github.com/noonghunna/club-3090/commit/314411365a160c1721de6e15de755e9ba6333e21))
- feat(concurrency-probe): make the sampler configurable, default unchanged ([a22be4b](https://github.com/noonghunna/club-3090/commit/a22be4b8c001b17aa63cd35371177278de491201))
- feat(qwen3.8-27b): mamba-align prefix caching on MTP composes — cuts between-turn TTFT (#1093) ([#1093](https://github.com/noonghunna/club-3090/pull/1093) by @noonghunna)
- feat(kv-calc): llama.cpp VRAM projection — kills kvcalc_key SKIP for priced llama slugs ([4d409c8](https://github.com/noonghunna/club-3090/commit/4d409c87694dd09bb98d8bd92e18a8213e9c33cd))
- feat(deriver): ModelSpec M5 — GDN/SWA/MLA family extractors (GGUF verified) ([5edc339](https://github.com/noonghunna/club-3090/commit/5edc339af0df3ebcf140f1b495af8be3cea1d98e))
- feat(promote): ModelSpec M4 — typed spec is the canonical write-path input ([84144e0](https://github.com/noonghunna/club-3090/commit/84144e0739d69167ac15c1bb6e6c822583c66542))
- feat(deriver): ModelSpec M5-MoE — expert facts from config.json AND GGUF headers ([852d0bd](https://github.com/noonghunna/club-3090/commit/852d0bdacaab02b066dd6bda17db9d4e29ec710e))
- feat(qwen3.8-27b): seqs=8 fast-tier default + crash-fixes on all vLLM composes (#1091) ([#1091](https://github.com/noonghunna/club-3090/pull/1091) by @noonghunna)
- feat(concurrency-probe): opt-in WARMUP gate for the live --sweep path (#1088) ([#1088](https://github.com/noonghunna/club-3090/pull/1088) by @noonghunna)
- feat(qwen3.8-27b/dual-fast): vendor FlashInfer decode-buffer unpin (#1051) — unlocks MTP concurrency (#1089) ([#1089](https://github.com/noonghunna/club-3090/pull/1089) by @noonghunna)
- feat(deriver): ModelSpec M1–M3 — typed, provenance-labeled specs through Bring→Promote ([4a29ab5](https://github.com/noonghunna/club-3090/commit/4a29ab57d42a1d587de1042fa5dfd9535f94a063))
- feat(catalog): one-sentence description on every model profile ([cea3c00](https://github.com/noonghunna/club-3090/commit/cea3c00510d0f76e089648e2f599dabf33cf1bff))
- feat(c3): log-follow underline tracks only the newest batch ([9f7e451](https://github.com/noonghunna/club-3090/commit/9f7e451e6c02ef8b9c61f39d2e114e00fdc8297f))
- feat(c3): underline tint + colored following/paused follow state ([5af538c](https://github.com/noonghunna/club-3090/commit/5af538c978865f1d4ed0e7a89fe6e6fe674cab1e))
- feat(c3): [f] log-follow tick — 2s poll with anchor dedupe ([7749588](https://github.com/noonghunna/club-3090/commit/77495887b0ce81e796aa014dc2c409b04fa8cf9b))
- feat(c3): arm/pause/disarm the [f] log-follow with live title ([e1dc078](https://github.com/noonghunna/club-3090/commit/e1dc078f05031592d70e858801f7ecd30468d130))
- feat(c3): wire [f] log-follow binding, context gate, palette + hint ([78f878e](https://github.com/noonghunna/club-3090/commit/78f878e7994d4f462c9b6f9064f2b20c68342e9f))
- feat(tui-core): LivePane tail-reader scroll-follow + set_title ([a23c01e](https://github.com/noonghunna/club-3090/commit/a23c01e9573915888151bd860918070ad84fbd50))
- feat(c3): catalog column sort + first-run guided path ([a3ed372](https://github.com/noonghunna/club-3090/commit/a3ed3723efc617c8c115d3c818bf99f9c226af7d))
- feat(quality): #983+#981 — both-modes flag, version-stamped Quality lines, card wiring ([e758ca3](https://github.com/noonghunna/club-3090/commit/e758ca39a253a1d174772cb6b5fd04b493d0b582))
- feat(c3): your-rig TPS/8pk columns + estate KV-pool line + quit guard ([04d358d](https://github.com/noonghunna/club-3090/commit/04d358db2c24ec2dbd3ee0f5ff3e0586b91c8b46))
- feat(quality): #987+#1023 — pass-through + promoted flags + drift guard ([8afb751](https://github.com/noonghunna/club-3090/commit/8afb7511a7aa88f7b1d3b488f88811dd786db59a))
- feat(export): export_pr adapted to registry.yaml storage + sys.path guard port ([2246259](https://github.com/noonghunna/club-3090/commit/22462598c8fb5d47f03e3c6877bd23ecfe44b317))
- feat(registry): registry-as-data — catalog moves to registry.yaml, compose_registry.py becomes loader+API shim ([c423258](https://github.com/noonghunna/club-3090/commit/c423258a5c2685606ea120730b26e81c3e082fd5))
- feat(c3): boot-log KV back-solve [K] + ADDING_MODELS contract-reference rewrite ([fd539c0](https://github.com/noonghunna/club-3090/commit/fd539c0bbf8e467975dc92d19c872cd4649d465c))
- feat(sampler): llama.cpp rows in registry + guard argv mode; thinking-pin persistence ([6612554](https://github.com/noonghunna/club-3090/commit/661255493b33c163d439705ec05634bca7ff298b))
- feat(c3): PR-export bundle + optimizer brain + sys.path contamination fix ([1542c6a](https://github.com/noonghunna/club-3090/commit/1542c6aecca366495a845272c73e80c473fbb0b9))
- feat(deriver): #984-adjacent P3 — GGUF header KV extraction ([7d5ce31](https://github.com/noonghunna/club-3090/commit/7d5ce3103cdca365337d4c849f6e5e9b7d6acf25))
- feat(gateway): registry-derived routes for gemma/deepseek/35b/gemma-12b/deckard ([6613fa6](https://github.com/noonghunna/club-3090/commit/6613fa6203f274e995e65e977c678466af49882f))
- feat(c3): #1014 Layer 3 — tri-state thinking toggle + reset-to-card-defaults ([27c89e7](https://github.com/noonghunna/club-3090/commit/27c89e77fda3e7c4690bc22448fc5938d6594d45))
- feat(c3): HF search browser on the Bring lane — search the Hub before Inspect ([6ea7734](https://github.com/noonghunna/club-3090/commit/6ea773400f333bb9c5a151744f5a71a1112a3dd0))
- feat(registry): shared lookup helper + fix two live hand-copy drift bugs ([4192695](https://github.com/noonghunna/club-3090/commit/4192695ab59c349b8498531b40ecb09b33c3ab6b))
- feat(sampler): #984/#1014 L1+L2 — sampler follows ENABLE_THINKING; profiles in registry ([ea24343](https://github.com/noonghunna/club-3090/commit/ea24343dfd98f89777ac6c5d73bcd6cd0642f7b1))
- feat(preflight): #1042 — catch missing weight shards before the engine does ([fdc7fbd](https://github.com/noonghunna/club-3090/commit/fdc7fbdc44e554d2df5ddc85333e5bd96865c757))
- feat(gateway): #1078 LiteLLM local config generated from the registry ([16d3b56](https://github.com/noonghunna/club-3090/commit/16d3b56a238f9ba4e81be91dcd11c514f6ab9130))
- feat(registry): served_name as a first-class emitted fact ([0dd6ed8](https://github.com/noonghunna/club-3090/commit/0dd6ed8e1b1d7fab503219ed246b11d1b6ba3a71))
- feat(registry): strict profile-key validation — unknown YAML keys fail loudly ([d65126c](https://github.com/noonghunna/club-3090/commit/d65126c2b3b4fa580ceba948424bbbb6dc8b9928))
- feat(c3): smooth animated horizontal scroll on wide tables (shift+←/→) ([24afc71](https://github.com/noonghunna/club-3090/commit/24afc71aa67141e5e496c25497f4d7477f09386a))
- feat(c3): model-info popup, default markers, real promote flow, degraded-catalog surfacing ([bad5913](https://github.com/noonghunna/club-3090/commit/bad59135176c73e74f978ff974f4e3e90c3bc9e8))
- feat(registry): profiles-local community layer + promote executor ([5d800e9](https://github.com/noonghunna/club-3090/commit/5d800e99de26dae78da159d0da964dbba33432e2))
- feat(setup): registry-derived front door + scoped add-model preflight ([cb6d261](https://github.com/noonghunna/club-3090/commit/cb6d26115f88a655b9a95f53eebf69061debc3a9))
- feat(tests): gate litellm gateway ports resolve to registry (#1062) ([df2bdcd](https://github.com/noonghunna/club-3090/commit/df2bdcdb7370edd352f7e64f89ffccda954754f1))
- feat(qwen3.8): DFlash2 speed×fidelity tiers + iq4xs slug + port hygiene (#1072) ([#1072](https://github.com/noonghunna/club-3090/pull/1072) by @noonghunna)
- feat(qwen3.8-27b): swap single-card llama.cpp slug to UD-IQ4_XS ([dbbf733](https://github.com/noonghunna/club-3090/commit/dbbf7339378864e34e6590b7ff8140bb29e8b540))
- feat(concurrency-probe): live N×ctx --sweep matrix, card, compose rec (#1057) ([#1057](https://github.com/noonghunna/club-3090/pull/1057) by @noonghunna)
- feat(qwen3.8-27b): default reasoning_effort to medium on the llama.cpp slugs (#1021) ([#1021](https://github.com/noonghunna/club-3090/pull/1021) by @noonghunna)
- feat(qwen3.8-27b): default reasoning_effort to medium when thinking is on (#1020) ([#1020](https://github.com/noonghunna/club-3090/pull/1020) by @noonghunna)
- feat(baselines): record vllm/qwen38-27b-dual-fast on the v0.27.1 pin (#1016) ([#1016](https://github.com/noonghunna/club-3090/pull/1016) by @noonghunna)
- feat(qwen3.8-27b): ship the fast tier W4A8 by default (#1008) ([#1008](https://github.com/noonghunna/club-3090/pull/1008) by @noonghunna)
- feat(qwen3.8-27b): add the NVFP4 tier — single + dual (#1007) ([#1007](https://github.com/noonghunna/club-3090/pull/1007) by @noonghunna)
- feat(qwen3.8-27b): add the AutoRound INT4 "fast" tier — dual/multi4/multi8 (#1003) ([#1003](https://github.com/noonghunna/club-3090/pull/1003) by @noonghunna)
- feat(concurrency-probe): emit tail latency and engine-side admitted concurrency (#1002) ([#1002](https://github.com/noonghunna/club-3090/pull/1002) by @noonghunna)
- feat(qwen3.8-27b): add the model catalog — 5 slugs, 2 engines, 3 booted (#990) ([#990](https://github.com/noonghunna/club-3090/pull/990) by @noonghunna)
- feat(catalog): llamacpp-club3090 engine + DeepSeek moe-cache slugs ([3fb98b4](https://github.com/noonghunna/club-3090/commit/3fb98b46ffff15178137d33e5c3de0e51f0d993d))
- feat(launch-compat): per-card expert-cache reserve floor ([75e3cd2](https://github.com/noonghunna/club-3090/commit/75e3cd23b1332ae8ed000da6bf4e63d70a9e152d))
- feat(residency): additive auto-sizer calibrated from #931 — replaces the x0.55 guard (#937) ([#937](https://github.com/noonghunna/club-3090/pull/937) by @noonghunna)
- feat: auto-detect club-3090 endpoint for Claude Code (#898) ([#898](https://github.com/noonghunna/club-3090/pull/898) by @paulp83)
- feat(p2p-validate): report peer vs host-staged bandwidth, subordinate to the verdict (#926) ([#926](https://github.com/noonghunna/club-3090/pull/926) by @noonghunna)
- feat(c3): surface offload slugs properly + wire setup.sh + fix two #905 regressions (#908) ([#908](https://github.com/noonghunna/club-3090/pull/908) by @noonghunna)
- feat(deepseek-flash): CPU-offload slugs + marker-scoped offload guards (#905) ([#905](https://github.com/noonghunna/club-3090/pull/905) by @noonghunna)
- feat(scripts): p2p-validate — collective-level P2P check (#902) ([#902](https://github.com/noonghunna/club-3090/pull/902) by @noonghunna)
- feat(bench): --quick preset for A/B sweeps (#832) ([c657e67](https://github.com/noonghunna/club-3090/commit/c657e67d6683a16ffe9136dc156ee8c153bca580))
- feat(owui): bump v0.9.6 -> v0.11.0 + DeepSeek lane + key-count fix (#807) ([e4abbb1](https://github.com/noonghunna/club-3090/commit/e4abbb129e93d440d5073641c335d81b0fdd6df9))
- feat(dual-nvfp4): fold #849 — first native-FP4 validation + envelope correction ([fa502b4](https://github.com/noonghunna/club-3090/commit/fa502b44bf8a1f2e11242cace72297f0f67ac0be))
- feat(gemma): production-gate Google QAT TP4 ([f698189](https://github.com/noonghunna/club-3090/commit/f698189796a4bb83ec8f94dd030b9d15c6db7b6f))
- feat(gemma): add official QAT TP4 profile ([b8b714f](https://github.com/noonghunna/club-3090/commit/b8b714f2e461eb2a820c9da4dd6650b5d4551dab))
- feat(kv-calc): model the GDN chunked-prefill scratch (batch-scaled, not ctx-scaled) ([c145b90](https://github.com/noonghunna/club-3090/commit/c145b908a706ed4afa5ec7a6c1e3e663547d096b))
- feat(card): render PCIe on non-offload snapshot cards (#841 remainder) ([827df27](https://github.com/noonghunna/club-3090/commit/827df277242bda098e991bde9adafcefa955f4d7))
- feat(capture): generalize the lib to serve both callers; retire the deferral note ([0ee1b36](https://github.com/noonghunna/club-3090/commit/0ee1b36d5bd2d33df6bf40bd8686997422840a12))
- feat(bench): CARD= toggle + live-run calibration fixes ([57def5a](https://github.com/noonghunna/club-3090/commit/57def5aa9fdad79848122329225d787107c206c2))
- feat(bench): add scripts/lib/card.sh — render a BENCH_CARD from a run ([e47aafd](https://github.com/noonghunna/club-3090/commit/e47aafdffb99a741e25fd9948cd6a769039f6057))
- feat(bench): wire the capture layer into bench.sh (11-item capture backlog) ([b9d9e6c](https://github.com/noonghunna/club-3090/commit/b9d9e6c2bcd3ac3d761de33e7f18d403aa8df17b))
- feat(bench): add scripts/lib/capture.sh — shared measurement-capture primitives ([aec124a](https://github.com/noonghunna/club-3090/commit/aec124a6258a485b8c6f308219ed8ffc2b4c1b51))
- feat(pull): actionable GGUF hint on the unsupported-format abort (#794) ([#794](https://github.com/noonghunna/club-3090/pull/794) by @noonghunna)
- feat(c3): persistent download logs + download preflight (2026-07-27 triage) (#793) ([#793](https://github.com/noonghunna/club-3090/pull/793) by @noonghunna)
- feat(thinkingcap-27b): add ThinkingCap-Qwen3.6-27B W4A8 dual compose + catalog ([9515a4c](https://github.com/noonghunna/club-3090/commit/9515a4c1dbfb7cc8ba47c8bde776f6d8304c7263))
- feat(quality): cloud/proxy endpoint support + qwen3.8-max cloud reference route (#746) ([#746](https://github.com/noonghunna/club-3090/pull/746) by @noonghunna)
- feat(nemotron-3-puzzle-75b): add 2-card vllm/nemotron-75b-dual-w4a16 (W4A16, 262K, N=4) (#721) ([#721](https://github.com/noonghunna/club-3090/pull/721) by @MIkamal88)
- Vendor Google's canonical Gemma 4 chat template (2026-07-09 fix) — repoint all 11 gemma vLLM composes (#737) ([#737](https://github.com/noonghunna/club-3090/pull/737) by @noonghunna)


### 🎯 New models + serving paths

- Add Qwen AgentWorld 35B production profile (#868) ([#868](https://github.com/noonghunna/club-3090/pull/868) by @Whamp)
- compose: fix orphaned pre-reframe fragment contradicting the stock-pin KV block (#765 round-2 review catch) ([25e54b7](https://github.com/noonghunna/club-3090/commit/25e54b746cf1b46976610c3a44682bb94a6cfb96))


### 🐛 Bug fixes

- fix(qwen3.8-27b): drop the retracted #1096 decode-cliff claim from 20 composes (#1232) ([#1232](https://github.com/noonghunna/club-3090/pull/1232) by @noonghunna)
- fix(concurrency-probe): a -1 MB VRAM delta must not FAIL the fit verdict (#1224) ([#1224](https://github.com/noonghunna/club-3090/pull/1224) by @noonghunna)
- fix(detect): classify engines from the REGISTRY, not container-name prefixes (#1223) ([#1223](https://github.com/noonghunna/club-3090/pull/1223) by @noonghunna)
- fix(concurrency-probe): SWEEP_DRY must not boot the slug (#1222) ([#1222](https://github.com/noonghunna/club-3090/pull/1222) by @noonghunna)
- fix(cockpit): render one GPU card per card, and default to multi4/multi8 (#1221) ([#1221](https://github.com/noonghunna/club-3090/pull/1221) by @noonghunna)
- fix(compaction-probe): continue the session, add correctness canaries ([5fef088](https://github.com/noonghunna/club-3090/commit/5fef088bfde13a4a1f1ba9894a79c01a391df7ff))
- fix(bench-agentic): measure decode correctly on reasoning models (#1218) ([#1218](https://github.com/noonghunna/club-3090/pull/1218) by @noonghunna)
- fix(catalog): derive what a real third-party recipe actually states (#1216) ([#1216](https://github.com/noonghunna/club-3090/pull/1216) by @noonghunna)
- fix(compose): ship the measured n=2 drafter depth on GLM dual (#1215) ([#1215](https://github.com/noonghunna/club-3090/pull/1215) by @noonghunna)
- fix(cockpit): re-read the catalog after a registry write (#1214) ([#1214](https://github.com/noonghunna/club-3090/pull/1214) by @noonghunna)
- fix(catalog): unbreak --weights <gguf>, surface the local-layer view, keep the (#1213) ([#1213](https://github.com/noonghunna/club-3090/pull/1213) by @noonghunna)
- fix(c3): read the FULL boot log, both streams, for the VRAM split ([a807bd7](https://github.com/noonghunna/club-3090/commit/a807bd787ffd6aec5939a152dd8b5d10c4bd43e9))
- fix(preflight): judge thinking levels by reasoning length, not "did it answer" (#1199) ([#1199](https://github.com/noonghunna/club-3090/pull/1199) by @noonghunna)
- fix(preflight): give the thinking probe enough budget to see a thinking-only model (#1197) ([#1197](https://github.com/noonghunna/club-3090/pull/1197) by @noonghunna)
- fix(verify): detect thinking-only models instead of assuming a dial means OFF (#1196) ([#1196](https://github.com/noonghunna/club-3090/pull/1196) by @noonghunna)
- fix(verify): stop reporting a crash when the model returns no content (#1194) ([#1194](https://github.com/noonghunna/club-3090/pull/1194) by @noonghunna)
- fix(tests): repair the generate-compose fixtures #1188 broke ([206ce02](https://github.com/noonghunna/club-3090/commit/206ce029a1898e50d86c46334e45810e5cb15537))
- fix(preflight): the gpu-fit failure gives Linux-only advice that is a dead end on WSL (#1134) ([51b531d](https://github.com/noonghunna/club-3090/commit/51b531df319f742d14477918bf2dd85fb4a83985))
- fix(patches): two dormant entries stop claiming load-bearing status (#1012) ([dd665b0](https://github.com/noonghunna/club-3090/commit/dd665b0b7403f193e8200af84330fe7311ee2eb4))
- fix(tests): test-bench-capture must start the bench right after the first stats sample (#1137) ([01ef968](https://github.com/noonghunna/club-3090/commit/01ef968e7af943f617f4c48c3845a4a8fdf7e3ff))
- fix(tests): args-array-scope gate must export PYTHONUTF8 (#779) ([bebf5e9](https://github.com/noonghunna/club-3090/commit/bebf5e91d9444b28a35759231f10084d2e9a6d81))
- fix(qwen3.8-27b): map reasoning_effort high -> xhigh, not medium ([a2ca899](https://github.com/noonghunna/club-3090/commit/a2ca899a11d048608a25402d73167427f5ca319a))
- fix(qwen3.8): map reasoning_effort `high` -> `medium` on all 20 vLLM slugs ([f8dda49](https://github.com/noonghunna/club-3090/commit/f8dda4989415110c11abd051179016cc14022e65))
- fix(litellm): regenerate config for the #1175 status change, and stop the test hard-coding a status ([a668c6a](https://github.com/noonghunna/club-3090/commit/a668c6a388e0e9bc939608c5f4a819a052949a1e))
- fix(hf-fetch): missing hf binary escalates to rung 3; CLI announces failure (#1132) ([69bc378](https://github.com/noonghunna/club-3090/commit/69bc378fc6ee3eecc4c6f7f301752ffdfcda4a2c))
- fix(setup): skip non-numeric WEIGHT_SIZE_GB in the disk gate instead of crashing (#1131) ([0a3f189](https://github.com/noonghunna/club-3090/commit/0a3f1891fa8401d517d652e3700be929ea1a45c1))
- fix(vram-breakdown): count drafter weights and GLM recurrent state (#1171) ([49afe82](https://github.com/noonghunna/club-3090/commit/49afe82663d36bb888b7d923b28540353028d67b))
- fix(cockpit): deferred tab focus must not reach past a modal ([f49dc87](https://github.com/noonghunna/club-3090/commit/f49dc87f6bd1f26a938b14be96dd98952e90ff87))
- fix(cockpit): deferred tab-activation focus must not steal the tab bar ([b46fb44](https://github.com/noonghunna/club-3090/commit/b46fb4421a32540b51865df60ea7877701fb52bf))
- fix(cockpit): Help title says 'club3090 cockpit', matching the app header ([855c534](https://github.com/noonghunna/club-3090/commit/855c53498bcc7c374332d646f6ff83a91b4209b9))
- fix(cockpit): drop the confirm body line duplicating the modal footer ([51e0d75](https://github.com/noonghunna/club-3090/commit/51e0d75459b8530ef2d18197f3972af5e7c01d78))
- fix(cockpit): hide dead KV/Apply controls on the unavailable Optimize card ([b9be0d5](https://github.com/noonghunna/club-3090/commit/b9be0d5bf253bc93d20a25335801bfd46140709b))
- fix(cockpit): state confirm-gating once in the Orchestration hint ([9bf3e36](https://github.com/noonghunna/club-3090/commit/9bf3e36dafbd3c4c95483d341c37bda7b114266a))
- fix(c3): read the resize EVENT's width in the footer width gate ([66859e2](https://github.com/noonghunna/club-3090/commit/66859e2991cf9e02c869cc9ec7ab77e86687f37d))
- fix(c3): fill the lane focus black holes + teach the six hidden Catalog keys ([de400ee](https://github.com/noonghunna/club-3090/commit/de400eeae15f3b52a4cd541c41fd814da36f3391))
- fix(c3): make 80x24 and 100x30 usable (review #16-#22) ([8c8522b](https://github.com/noonghunna/club-3090/commit/8c8522b0e2c48750583ec449ed37fc5c8a14df68))
- fix(c3): Explain falls back to the catalog row instead of showing dashes ([3e2a7f2](https://github.com/noonghunna/club-3090/commit/3e2a7f2941130eecb13d7adf2826f57cb911fa43))
- fix(c3): make Settings saveable at 80x24 ([d8ce320](https://github.com/noonghunna/club-3090/commit/d8ce3200a8864458f231fcbf563326d45f8a7fb9))
- fix(c3): land focus on Fit-check after Inspect, and keep the verdict on screen ([f43a31c](https://github.com/noonghunna/club-3090/commit/f43a31c5fb0fa8d0451199342ab20a80040b8625))
- fix(c3): advertise ⏎ in one consistent place instead of half the panes ([215910f](https://github.com/noonghunna/club-3090/commit/215910fc5c89fb7d5b17942bbfa21085ced71d28))
- fix(c3): repaint ⑤ Promote's footer when the stage gate opens ([af6b9fa](https://github.com/noonghunna/club-3090/commit/af6b9faf32ff75bf00b407050d34b9a3134b3199))
- fix(c3): escape key hints so Textual markup stops deleting them ([ef86b0f](https://github.com/noonghunna/club-3090/commit/ef86b0f67d3503722f6e3e4ba5be7b313c4fc483))
- fix(moecache): close the engine-knob gaps; leave the shell-knob drift alone ([1dbc629](https://github.com/noonghunna/club-3090/commit/1dbc62995a7b21fd9f9ee0907ebaacb98d780e93))
- fix(moecache): declare LLAMA_GRAPH_REUSE_DISABLE on all 16 composes, not 1 ([d6f0122](https://github.com/noonghunna/club-3090/commit/d6f01220d256a1b4f531db2c541f3024ceac00eb))
- fix(c3,bench): stop claiming things the code and the record don't support ([5b81b5f](https://github.com/noonghunna/club-3090/commit/5b81b5fd28815bef06fe5823b8aa6968c9ca391d))
- fix(c3): Bring & Validate UX pass — visible focus, honest copy, working stages ([2a2b1d3](https://github.com/noonghunna/club-3090/commit/2a2b1d369f4276b5b31f41b5740b061c73d5d0bd))
- fix(c3): ⑤ Promote never passed the compose, so every LOCAL write was refused (#1156) ([e03f768](https://github.com/noonghunna/club-3090/commit/e03f768c5349e16871874ca5f03bf5e3ba5bfe02))
- fix(bench): make the RAM-derivation refusal loud, and split its two failure causes (#1137) ([8cdb64b](https://github.com/noonghunna/club-3090/commit/8cdb64bd6466e5c3b12357ab7bc019cdf60e0a7c))
- fix(tests): allow --spec-file in the quality-test doc drift guard (regression from #1143) ([80aa25e](https://github.com/noonghunna/club-3090/commit/80aa25e9dcc10abf08a71a8837acda98a95b92b4))
- fix(promote): honour repo-root .env so the core gate stops being a silent no-op (#1142) ([56afa2a](https://github.com/noonghunna/club-3090/commit/56afa2aff302f5fea05157752af0326650a51100))
- fix(deepseek-vision): correct the vision rationale in the model profile too ([677115d](https://github.com/noonghunna/club-3090/commit/677115d59c30daf27dde5a9b912be19a5b4dfff6))
- fix(deepseek-vision): the model HAS vision — the GGUF conversion lost it ([c33a2f9](https://github.com/noonghunna/club-3090/commit/c33a2f9ab3d0a39aa58462ddb5c2d26e38c9f981))
- fix(deepseek-vision): replace the swap-confounded numbers with a controlled re-run ([8844f0f](https://github.com/noonghunna/club-3090/commit/8844f0f51e38c07c0aeeb3a19aebeb44402a966d))
- fix(capture): the moe-cache pool census double-counted on drafter runs ([56d8f4a](https://github.com/noonghunna/club-3090/commit/56d8f4ae6371b36e18ab75a2b13b5076d5cd2d97))
- fix(deepseek-vision): align both composes with the GLM/Qwen Flash siblings ([e955c64](https://github.com/noonghunna/club-3090/commit/e955c643b29048f1563a2ebfb2f2a1bb558496e6))
- fix(bench): give the depth leg a decode floor so terse models measure ([c77f345](https://github.com/noonghunna/club-3090/commit/c77f34539ff8033157b5db2f1e7917016d09fc31))
- fix(glm): ubatch 2048 on dual, reasoning-effort header, status drift ([7ede960](https://github.com/noonghunna/club-3090/commit/7ede960b13104c7e129ab7cdc9324fed6ab55cb2))
- fix(compose): declare VLLM_ENFORCE_EAGER and MMPROJ; empty the debt register ([5ce47c6](https://github.com/noonghunna/club-3090/commit/5ce47c68bfb009b7f04533d8d9e0c4a1c5d41494))
- fix(glm): forward THREADS to the container; guard the whole class ([8dc460f](https://github.com/noonghunna/club-3090/commit/8dc460ffdd7da0af3999c01c410a58e1992a9ada))
- fix(compose): make -np operator-settable via NPARALLEL (17 composes) ([90b9768](https://github.com/noonghunna/club-3090/commit/90b97689718d821c045aa6c5b0aa3c4fe7509aa6))
- fix(preflight): probe whether the top-level effort field defeats the kwarg ([c8e3ef2](https://github.com/noonghunna/club-3090/commit/c8e3ef254d2814eae142f18cd30b7246b900cfeb))
- fix(catalog): offload column shows static/dynamic; correct 4 drifted entries ([4ad9517](https://github.com/noonghunna/club-3090/commit/4ad95179672740af98f55caf2b2d9fb873ac58d6))
- fix(engines): declare q8_0 KV support on llamacpp-club3090-v1.5 ([49f1f26](https://github.com/noonghunna/club-3090/commit/49f1f264b0b655908526491aac26f202fff3c710))
- fix(tests): sampler-profiles gate mishandled non-vLLM llama.cpp engines ([150f758](https://github.com/noonghunna/club-3090/commit/150f7586ffa03c5259f55fe3467f39b8b053d26b))
- fix(c3): reap timed-out subprocesses so the loop closes cleanly ([def39b4](https://github.com/noonghunna/club-3090/commit/def39b4bb32d93fbe62f19c25a57a7b8dd76a3b7))
- fix(inkling): pin GGML_EXPERT_PREFETCH=0 explicitly on all three slugs ([d06fd75](https://github.com/noonghunna/club-3090/commit/d06fd75b00ab330891400c94428ae350037980e6))
- fix(cockpit): reap subprocesses on timeout so the loop can close cleanly ([5c0d6d3](https://github.com/noonghunna/club-3090/commit/5c0d6d3504d8fa641e45ca77eadf986adce58601))
- fix(preflight): probe reasoning-effort as a ladder, not one hardcoded level ([247b21e](https://github.com/noonghunna/club-3090/commit/247b21eaaa1d4818f0dcea01c64dc4cc60249506))
- fix(grammar-eval): replace a hardcoded maintainer-rig tokenizer default ([5a89766](https://github.com/noonghunna/club-3090/commit/5a89766a4c5532251f3820727bec15a8af1d0291))
- fix(moe-cache): make telemetry reachable on all five cache composes, opt-in by default ([199d296](https://github.com/noonghunna/club-3090/commit/199d296f14663c485dfe8f3a0eafd415b1921e5d))
- fix(moe-cache): make cache telemetry reachable, and stop reporting its absence as zero ([1d92942](https://github.com/noonghunna/club-3090/commit/1d92942f1b575b54e43cf4f5009508b6f7322c04))
- fix(switch): catch crash-loops and prove generation before ready (#1103) ([#1103](https://github.com/noonghunna/club-3090/pull/1103) by @noonghunna)
- fix(deepseek-v4-flash): reap zombies with init:true, resolve -t in the entrypoint ([9e1644d](https://github.com/noonghunna/club-3090/commit/9e1644d2ed27be7949fb501da08ea1be8c9e6188))
- fix(gpu-mode): status-probe labels match registry truth (:8013/:8030/:8032) ([bcabbb2](https://github.com/noonghunna/club-3090/commit/bcabbb2da7bc235c66f116074476d5ef2806bf5b))
- fix(verify-stress): #1017 — salted haystacks + cache-hit guard + --save-json ([4961286](https://github.com/noonghunna/club-3090/commit/496128606d3017c29d50ec88e4b832ab5acd37b5))
- fix(studio): setup-ai-studio connections match the openwebui→gateway collapse ([2f31984](https://github.com/noonghunna/club-3090/commit/2f31984ab61b48bc77eb82f2b0009a330a3b4772))
- fix(scripts): default engine URLs derive from the registry; openwebui routes via gateway ([4264065](https://github.com/noonghunna/club-3090/commit/4264065b5700d07a65c39751b699c713baa5d84d))
- fix(c3): catalog ←/→ now page horizontally; horizontal wheel handlers added ([154ea03](https://github.com/noonghunna/club-3090/commit/154ea03d4d8a74464377fb14334751e2743c0f9e))
- fix(c3): #1010 — int8 toggle no-op/backwards on ship-int8 slugs ([de0064b](https://github.com/noonghunna/club-3090/commit/de0064b20aa308e38e18331ef3436d50e4f3ba1a))
- fix(tests): #1009 — classifier/dedup tests tolerate schema-2 capture leftovers ([6d4ac93](https://github.com/noonghunna/club-3090/commit/6d4ac93d56c06c3500a156dec7649adfd2158a5b))
- fix(tests): export PYTHONUTF8 in test-setup-picker.sh (#779 guard) ([8e7a429](https://github.com/noonghunna/club-3090/commit/8e7a42981986d0878c570d34eb6165e24751f88e))
- fix(c3): mouse UX — click-on-highlighted-row no longer fires the serve confirm; copyable scaffold/compose modals; Help mouse section ([223ebfe](https://github.com/noonghunna/club-3090/commit/223ebfe3526b56f9a7965a54358e4f37978f81c7))
- fix(c3): [|] columns-picker key was silently dead — wrong Textual key name ([8d5b993](https://github.com/noonghunna/club-3090/commit/8d5b99370ed6f9acd66b747914b19dade3583bcd))
- fix(tests): update stale spec-sweep port 8020 -> 8115 (#1077 follow-up) ([df4338d](https://github.com/noonghunna/club-3090/commit/df4338d724f69292d072f92e8a6612c31cf3f9e0))
- fix(deepseek-moecache): fail loud when the DSpark drafter GGUF is missing (#1054) ([9a50ea6](https://github.com/noonghunna/club-3090/commit/9a50ea68f596a81a6ffc8e75338f3299b37db203))
- fix(verify-full): respect ENGINE_KIND, detect llama.cpp fingerprint, guard docker none (#1067) ([ba77fed](https://github.com/noonghunna/club-3090/commit/ba77fed42b5bc02c1f8a2654a08c2da668ca5111))
- fix(report): respect inherited CONTAINER + special-case CONTAINER=none (#1066) ([3785e19](https://github.com/noonghunna/club-3090/commit/3785e19a2afba409c73cf8bdf3f0a37ccfd996e1))
- fix(tests): add missing PYTHONUTF8 guard to test-concurrency-probe.sh (#779) ([df52709](https://github.com/noonghunna/club-3090/commit/df527091204a9e0743e83f187905d91685595c42))
- fix(litellm): register local qwen3.8-27b routes on :8091 (#1062) ([86aa73f](https://github.com/noonghunna/club-3090/commit/86aa73f5deba312967da0ebf98dba4441b00c186))
- fix: resolve 8020/8032 cross-model port collisions (#1077) ([#1077](https://github.com/noonghunna/club-3090/pull/1077) by @noonghunna)
- fix(qwen3.8): swap FAST-tier weights Avuja → Frozenlock (#1052 acceptance collapse) (#1070) ([#1070](https://github.com/noonghunna/club-3090/pull/1070) by @noonghunna)
- fix(qwen3.8): patch GDN+MTP async wild-write crash on dual-fast (#1052) (#1061) ([#1061](https://github.com/noonghunna/club-3090/pull/1061) by @noonghunna)
- fix: make qwen3.8-27b reachable from setup.sh, truncate preflight notes, correct a stale weights claim (#1043) ([#1043](https://github.com/noonghunna/club-3090/pull/1043) by @noonghunna)
- fix(switch): truncate status_note in terminal warnings (reported via #1036) (#1041) ([#1041](https://github.com/noonghunna/club-3090/pull/1041) by @noonghunna)
- fix: remove leaked absolute paths (username in a public repo) (#1038) ([#1038](https://github.com/noonghunna/club-3090/pull/1038) by @noonghunna)
- fix(qwen3.8-27b): default reasoning_effort low, was medium (#1029) ([#1029](https://github.com/noonghunna/club-3090/pull/1029) by @noonghunna)
- fix(verify-stress): split the summary into boundary vs recall verdicts (#1018) ([#1018](https://github.com/noonghunna/club-3090/pull/1018) by @noonghunna)
- fix(qwen3.8-27b): vision works — correct the headers, trim duplicated prose (#1015) ([#1015](https://github.com/noonghunna/club-3090/pull/1015) by @noonghunna)
- fix(qwen3.8-27b): mark the fast tier act8_capable so c3 offers the int8 knob (#1006) ([#1006](https://github.com/noonghunna/club-3090/pull/1006) by @noonghunna)
- fix(qwen3.8-27b): bf16 KV on the multi4/multi8 max slugs (#1001) ([#1001](https://github.com/noonghunna/club-3090/pull/1001) by @noonghunna)
- fix(c3): only require reconcile for GPU-holding services in service_start (#941) ([#941](https://github.com/noonghunna/club-3090/pull/941) by @paulp83)
- fix(verify-stress): make probe-6 reasoning timeout configurable (#934) ([#934](https://github.com/noonghunna/club-3090/pull/934) by @noonghunna)
- fix(deepseek-flash): derive multi4's residency constants for 4 cards, not 2 (#927) ([#927](https://github.com/noonghunna/club-3090/pull/927) by @noonghunna)
- fix(p2p): classify user-disabled custom-AR; document the wrong-data failure mode (#924) ([#924](https://github.com/noonghunna/club-3090/pull/924) by @noonghunna)
- fix(deepseek-flash): map host port to container 8080, restoring endpoint autodetect (#923) ([#923](https://github.com/noonghunna/club-3090/pull/923) by @noonghunna)
- fix(report): capture memory CHANNELS and MEASURED bandwidth, not slots and rated MT/s (#919) ([#919](https://github.com/noonghunna/club-3090/pull/919) by @noonghunna)
- fix(preflight): catch weights reachable only through a symlink out of MODEL_DIR (#918) ([#918](https://github.com/noonghunna/club-3090/pull/918) by @noonghunna)
- fix(report): capture what we ask users for — CPU topology, DIMM config, P2P status (#916) ([#916](https://github.com/noonghunna/club-3090/pull/916) by @noonghunna)
- fix(preflight): see list-form compose args, so the deps guard stops false-greening (#915) ([#915](https://github.com/noonghunna/club-3090/pull/915) by @noonghunna)
- fix(setup): size the disk gate from the actual fetch; stop crashing on exit (#914) ([#914](https://github.com/noonghunna/club-3090/pull/914) by @noonghunna)
- fix(deepseek-flash): gate readiness on the DSpark drafter (#912) ([#912](https://github.com/noonghunna/club-3090/pull/912) by @noonghunna)
- fix(deepseek-flash): scope the weight fetch to the quant we serve (#911) ([#911](https://github.com/noonghunna/club-3090/pull/911) by @noonghunna)
- fix(deepseek-flash): declare verify_glob on the GGUF weights entries (#910) ([#910](https://github.com/noonghunna/club-3090/pull/910) by @noonghunna)
- fix(p2p): scope the +10-22% gain to vLLM; record llama.cpp's measured zero (#889) ([#889](https://github.com/noonghunna/club-3090/pull/889) by @noonghunna)
- fix(p2p): llama.cpp DOES have a runtime P2P toggle -- GGML_CUDA_P2P (#888) ([#888](https://github.com/noonghunna/club-3090/pull/888) by @noonghunna)
- fix(p2p): stop telling llama.cpp users to set NCCL_P2P_DISABLE (#887) ([#887](https://github.com/noonghunna/club-3090/pull/887) by @noonghunna)
- fix(bench): gate the log-scraped PP tok/s on plausibility instead of printing it unconditionally (#817) ([bc4af65](https://github.com/noonghunna/club-3090/commit/bc4af653cd664bbe68536a25ab46b8080ee42694))
- fix(bench): never divide by an epsilon decode window; classify canvas-granularity models (#809) ([ce5aba0](https://github.com/noonghunna/club-3090/commit/ce5aba095c5859698330029c39a38986d7d44e25))
- fix(report): propagate inner check verdicts to the exit code (#813) ([eede9dc](https://github.com/noonghunna/club-3090/commit/eede9dcac44a0fd9965ae957378a744085894e82))
- fix(report): stop running stages into a dead engine (#830) ([c2e0379](https://github.com/noonghunna/club-3090/commit/c2e037925d74327e00efa66d8644bb77b418b38f))
- fix(soak): derive wall TPS for canvas-granularity turns instead of 0.0 (#809) ([795b903](https://github.com/noonghunna/club-3090/commit/795b9036fb0180defa86081fd08c1c206fa00383))
- fix(soak): anchor the warm VRAM baseline on the first CLEAN session (#829) ([0ef049e](https://github.com/noonghunna/club-3090/commit/0ef049ee4a892bcdb3c1c9714afd97b6107c2044))
- fix(qwen-27b-dual-nvfp4): derate the authored-blind 262K envelope (#838) ([f46eb54](https://github.com/noonghunna/club-3090/commit/f46eb549f31c75650e143a99dfea20adfe3e6b60))
- fix(composes): keep the Status<->Caveats contract when recording the #50021 risk ([cfd1878](https://github.com/noonghunna/club-3090/commit/cfd1878913d18e33cfc3417c7499ef07a89fdc18))
- fix(offload-matrix): reconcile the rebase over #835 + port branch-era guards ([23e1d76](https://github.com/noonghunna/club-3090/commit/23e1d76e8eefbb862e1f0eae8cd513b77d9edb6b))
- fix(probe): validate SWEEP/SLUG args before environment probing ([378eb4d](https://github.com/noonghunna/club-3090/commit/378eb4d4b6df3cb0aa5c36406618f94fb330c535))
- fix(spark-dashboard): enable multi-GPU support and fix Docker GID detection ([dde343e](https://github.com/noonghunna/club-3090/commit/dde343e4d353d0ccf4a907c7fce8b223e0a890bf))
- fix(bench): correct the cache-health pass condition; live run disproved the spec ([5598569](https://github.com/noonghunna/club-3090/commit/5598569d454b97f24e8e175e21a1786608c5c6a1))
- fix(tess): lower MTP default n=5 -> n=3, precautionary (#758) ([7c31b17](https://github.com/noonghunna/club-3090/commit/7c31b176b262a3ed3fdd0b9a57c8e40c79ab80c7))
- fix(thinkingcap): lower MTP default n=5 -> n=3 (engine crash, #758) ([70a1418](https://github.com/noonghunna/club-3090/commit/70a1418d36350f94443a084ebf191bd328bb383b))
- hotfix: default prefix caching OFF on both nvfp4 MTP slugs — unpatched vllm#43559 pair (#810) (#811) ([#811](https://github.com/noonghunna/club-3090/pull/811) by @noonghunna)
- fix(c3): GGUF-only repos redirect to the quant picker instead of dead-ending (#792) ([#792](https://github.com/noonghunna/club-3090/pull/792) by @noonghunna)
- fix(thinkingcap): #736 prefix-caching parity — pr48375 + prefix-ON default (#790) (#791) ([#791](https://github.com/noonghunna/club-3090/pull/791) by @noonghunna)
- fix(p2p): nccl_only verdict state — never claim custom-AR-ON that vLLM vetoes at world>2 (#786) (#789) ([#789](https://github.com/noonghunna/club-3090/pull/789) by @noonghunna)
- fix(preflight): gate qwen-35b-a3b-dual-nvfp4 on homogeneous arch (#783) (#784) ([#784](https://github.com/noonghunna/club-3090/pull/784) by @noonghunna)
- fix(beellama): correct a false claim in the qwen-dflash-dual caveats ([d0136dd](https://github.com/noonghunna/club-3090/commit/d0136ddef98b87cc0294c973210178d7fd01fa9c))
- fix(patch-attribution): decode `docker compose config` as utf-8 (#779) (#781) ([#781](https://github.com/noonghunna/club-3090/pull/781) by @noonghunna)
- fix(preflight): refuse mixed-architecture TP for arch-gated composes (#762) (#775) ([#775](https://github.com/noonghunna/club-3090/pull/775) by @noonghunna)
- fix(qwen3.6-27b): DFlash is native on mainline; fix nonexistent drafter default (#759) (#774) ([#774](https://github.com/noonghunna/club-3090/pull/774) by @noonghunna)
- fix(qwen3.6-27b): FlashInfer sampler OFF on the 2x3090 MTP composes (#772) ([#772](https://github.com/noonghunna/club-3090/pull/772) by @noonghunna)
- fix(thinkingcap-27b): correct the hermesagent attribution (variance, not tightening) ([0f8a9ba](https://github.com/noonghunna/club-3090/commit/0f8a9ba58fd59e1f3404de8cd628e013bb5a5d99))
- fix(thinkingcap-27b): re-run 8-pack on benchlocal-cli v0.9.8 (114/126) ([0d781cf](https://github.com/noonghunna/club-3090/commit/0d781cf0220350781cf900e04681ea87b5494fc2))
- fix(thinkingcap-27b): add the missing baselines.yml row (c3 catalog columns) ([7c1f72a](https://github.com/noonghunna/club-3090/commit/7c1f72a988e91d48a64e796177c817c3c1b5dfdd))
- fix(nemotron-3-puzzle-75b): bump dual-w4a16 image v0.24.0->v0.25.1 (image-drift) ([#748](https://github.com/noonghunna/club-3090/pull/748) by @noonghunna)


### 📊 Benchmarks + cross-rig data

- bench: bank five @paulp83 2x5090 rows (#851 #858 #859 #833 #766) ([caa6ad1](https://github.com/noonghunna/club-3090/commit/caa6ad18af4da3cfdc3b27d0162d8837b86ba124))
- bench(diffusiongemma): first Blackwell row — paulp83 2x5090 (#822) ([33caf31](https://github.com/noonghunna/club-3090/commit/33caf31a8f55e5e811995b7bc2b586f111ab3e9c))
- bench: record paulp83 power A/B on mixed-arch 5090+3090Ti row (#761 — cap non-binding, clean null) ([4f77f35](https://github.com/noonghunna/club-3090/commit/4f77f35247c52c8ced8adf62ac65bd6ea6cc73ba))
- bench: add @henrykrinkle01 cross-rig 8-pack, thinking ON vs OFF (#770) ([03e1396](https://github.com/noonghunna/club-3090/commit/03e13966b1e9c1531fc9fac8067895e72a008b3b))
- bench: add vllm-stable v0.25.1 pin-bump validation row (dual.yml) ([999881e](https://github.com/noonghunna/club-3090/commit/999881eb6c9b4ff2157562e3ac3c7cee6b3d4152))
- bench: add heterogeneous uneven-TP=3 section (@efschu 2×3080+5090, #707) ([d580a87](https://github.com/noonghunna/club-3090/commit/d580a875bd8741b8b48a33d56615e3eb17ea4c94))


### 📝 Documentation

- docs(upstream): correct #52816 status, record the v0.28.0 retention regression ([6b8fdc7](https://github.com/noonghunna/club-3090/commit/6b8fdc7d7574afd496a08a7cd6b8e9cc7f59e6a7))
- docs+test(catalog): document the local workflow; pin that a local entry is never a default (#1208) ([#1208](https://github.com/noonghunna/club-3090/pull/1208) by @noonghunna)
- docs: RESULT-1118 follow-up — full-log both-streams read (tail+stderr root cause) ([143023e](https://github.com/noonghunna/club-3090/commit/143023e833fe729aa96eb5fb36130a0c99237440))
- docs(benchmarks): dual-fast + MAMBA_BLOCK_SIZE=8192 sub-row (ref 2x3090, rebench-full 2026-09-04) (#1198) ([#1198](https://github.com/noonghunna/club-3090/pull/1198) by @metaoutfitter)
- docs(qwen3.8-27b): vision headers from MEASUREMENT — all three dual tiers see ([ad23182](https://github.com/noonghunna/club-3090/commit/ad231821fc72a3569c1c67be90a2535295a9f6f6))
- docs(qwen3.8-27b): correct the stale "Vision: ✅ WORKING" header on all 8 vLLM composes ([16c6ace](https://github.com/noonghunna/club-3090/commit/16c6aced75c0962645fbec1dcdc17a903c81e498))
- docs(qwen3.8-27b): MAMBA_BLOCK_SIZE has no per-turn tail-block cost — 2K..200K sweep at 1616/4096/8192 ([b5271c1](https://github.com/noonghunna/club-3090/commit/b5271c1c9467dd778ea89bf6a68fd588bc417e93))
- docs(qwen3.8-27b): record rebench-full gate results for the MAMBA_BLOCK_SIZE=8192 config ([5023004](https://github.com/noonghunna/club-3090/commit/502300487524a735ac1c119df07b728a2cc518ef))
- docs(cockpit): LanePromotePane docstring — the write is real, not mock-only ([f4ac7e4](https://github.com/noonghunna/club-3090/commit/f4ac7e40f9080e43dc0ea3324d7da1970b9e8c42))
- docs(moe-cache): the reserve is NOT the lever — more slots measured 12.5% slower ([cb4d03b](https://github.com/noonghunna/club-3090/commit/cb4d03b4506fabfbef1020dfa91fc44ffb64ddb0))
- docs(moe-cache): two v1.6 engine findings, both measured on the rig ([9562eab](https://github.com/noonghunna/club-3090/commit/9562eab5ddb7d67e40a73a56b9212735434897ef))
- docs(qwen3.8-27b): correct the multi4/multi8-max wild-write caveat (#1147) ([57dbe74](https://github.com/noonghunna/club-3090/commit/57dbe747cc8cd55e411b9aa088ee69997fed4b94))
- docs(qwen3.8-27b): correct the dual-max wild-write caveat — two faults, one patched ([2b72904](https://github.com/noonghunna/club-3090/commit/2b72904eedc533144edc4a89fd30614f35b74093))
- docs: registry.yaml is the source of truth, not compose_registry.py ([38ba322](https://github.com/noonghunna/club-3090/commit/38ba322c511ced886e57e48d9a418f05e437900b))
- docs: route BYOM to the local model layer, not the curated catalog (#1142) ([4e80019](https://github.com/noonghunna/club-3090/commit/4e8001953571ec693603a0729dbb328a8bb91741))
- docs(drafter): flag the DFlash2 figures as stale on v1.6 ([2aa4a34](https://github.com/noonghunna/club-3090/commit/2aa4a34c8595b0d0e211197103f5b004aa860313))
- docs(glm): close the CUDA0 drafter-placement question (maintainer decision) ([1ae9d0f](https://github.com/noonghunna/club-3090/commit/1ae9d0f003a607dac52d862a47a2131739007deb))
- docs: correct stale engine provenance after testing DeepSeek on v1.5 ([4c257be](https://github.com/noonghunna/club-3090/commit/4c257be3ffb27ec205485d0c2ba728cffd587896))
- docs(benchmarks): the qwen3.8-flash-next canonical row is stale on TWO axes ([30f2a04](https://github.com/noonghunna/club-3090/commit/30f2a0413cb073eba796d2d1daac9bd33573b393))
- docs(glm-5.3-flash): trim compose history, fix stale MMPROJ_DEVICE claim ([ebeaa76](https://github.com/noonghunna/club-3090/commit/ebeaa76e95b5c9e9bb1c0eabe49fd8b6b9739fbe))
- docs(glm): retract the withdrawn prefetch figure from the multi-card headers ([5e43c50](https://github.com/noonghunna/club-3090/commit/5e43c50d1186924e3a32cd4dcf640aa2354a5cd9))
- docs(upstream): record b10648 as the v1.4.0 rebase target ([3673bb6](https://github.com/noonghunna/club-3090/commit/3673bb6fa8f0f95c9f47b5f80a6c3b1325607df0))
- docs(moe-cache): correct the prefetch claim — it is inert on the pinned image ([c235947](https://github.com/noonghunna/club-3090/commit/c235947e8c865d179867a44da902c5e083122f71))
- docs(upstream): pin #1096↔ReplaySSM and #1052↔hoist as distinct re-test triggers ([dbd97fb](https://github.com/noonghunna/club-3090/commit/dbd97fb202e9f3a3c06b528dd9958c68b48f1900))
- docs(qwen3.8-27b): correct spec-dec collapse caveats across DFlash2+MTP composes (#1096) ([b7c6958](https://github.com/noonghunna/club-3090/commit/b7c6958d544e9e8b11e9a29dda86efada8536bac))
- docs(upstream): add #40756 row — FlashInfer decode-pin vendored (accepts #1051) ([191e3ad](https://github.com/noonghunna/club-3090/commit/191e3ad6cfac61182195f4ac0c45ad72c489fd5b))
- docs(c3): document the [f] log-follow keybinding ([7f226fa](https://github.com/noonghunna/club-3090/commit/7f226fab89c82360818595d96d762e4d1cb7b882))
- docs(specs): design c3 container log-follow ([f]) for the Containers drill ([99ab322](https://github.com/noonghunna/club-3090/commit/99ab322b3954d8b608722ce87614acfe5c6c8811))
- docs(upstream): NVIDIA engaged on nccl#2335 — internal case #6637419 logged ([863a157](https://github.com/noonghunna/club-3090/commit/863a157cf11e40f1cb47ad9080eaabe7e24b9187))
- docs(img): add DFlash2 throughput card for the announcement (#1076) ([b2a539b](https://github.com/noonghunna/club-3090/commit/b2a539b84bdca0b2493c7a79c0f03581e69b2afc))
- docs(img): add c3 catalog screenshot for the DFlash2 announcement (#1076) ([4c99937](https://github.com/noonghunna/club-3090/commit/4c99937ff169e3cf4dce8c4248575353a4caa306))
- docs(upstream): correct declined ASYNC_SCHED-knob phrasing in #50021 row (#1052/#1059) ([4e6c336](https://github.com/noonghunna/club-3090/commit/4e6c336330c5ded0bce45a218ec72b96596f529b))
- docs(pcie-p2p): fold @fkrutko's two-rig confirmation into the §7a wrong-data row (#922) ([e858103](https://github.com/noonghunna/club-3090/commit/e8581033cd07a77c023fa880808a7edaabeec311))
- docs(upstream): #50021 async-scheduling mitigation + first field crash (#1059) ([9f61283](https://github.com/noonghunna/club-3090/commit/9f612834a19297d4eaeec5f688833a8a6ec5ab3b))
- docs(upstream): close #52873 — acceptance-collapse is checkpoint-specific ([b85efd8](https://github.com/noonghunna/club-3090/commit/b85efd8d46e3d89a4a85a2c30ca4081a3714e6e8))
- docs: purge Genesis from user-facing docs, close the Qwen3.8 gaps, fix the broken FAQ ladder (#1034) ([#1034](https://github.com/noonghunna/club-3090/pull/1034) by @noonghunna)
- docs: restructure the landing + three audience pages (−59%, zero new pages) (#1033) ([#1033](https://github.com/noonghunna/club-3090/pull/1033) by @noonghunna)
- docs: fix commands that cannot run + the TP head counts (#1031) ([#1031](https://github.com/noonghunna/club-3090/pull/1031) by @noonghunna)
- docs(qwen3.8-27b): correct pin references left stale by the v0.27.1 bump (#1022) ([#1022](https://github.com/noonghunna/club-3090/pull/1022) by @noonghunna)
- docs(club3090-env): add Claude Code settings.json configuration instructions (#947) ([#947](https://github.com/noonghunna/club-3090/pull/947) by @paulp83)
- docs(p2p): name verify-full as the correctness tier §7a already implied (#922) ([970a9f1](https://github.com/noonghunna/club-3090/commit/970a9f1b7cca84b36668622ddac394ffaf19deff))
- docs(AGENTS): warn both directions on reasoning-mode/leg matching ([24d4552](https://github.com/noonghunna/club-3090/commit/24d4552fef71a1844af0440c6ee7f36fb651fcef))
- docs: restructure SINGLE_CARD + IK_LLAMA after the single-card retirements (#967) (#970) ([#970](https://github.com/noonghunna/club-3090/pull/970) by @noonghunna)
- docs: quality tables carry pass@1 AND pass@3, per pack ([4673465](https://github.com/noonghunna/club-3090/commit/4673465f05fa88f7a2ac20a2320f497f1baca8b1))
- Document the llamacpp-club3090 engine for public release ([962301b](https://github.com/noonghunna/club-3090/commit/962301b92cd8589ed5e2624c5eeb5a70a1d84d80))
- docs(deepseek-q8): record why -ub stays 4096 on the stock slug ([7d5c94f](https://github.com/noonghunna/club-3090/commit/7d5c94fd6c6403667ba668daaa4efd322b0da480))
- docs(p2p): clique-granted aperture is a MIRROR on VFIO — correct the 'copies work' tier ([d0476a3](https://github.com/noonghunna/club-3090/commit/d0476a3ef43f63cd1f78d21bcc82b84b84b5ad1b))
- docs(upstream): NVIDIA/nccl#2335 filed — VFIO P2P visibility-contract question ([f616b44](https://github.com/noonghunna/club-3090/commit/f616b44ba27605027e531faf4d839d1d019fcdb3))
- docs(faq): fix contradictory wording in NVFP4 requirements line ([84d4738](https://github.com/noonghunna/club-3090/commit/84d4738aab182b9262292a6b1f9bfa6ddb1f95e5))
- docs(faq): refresh 5090 section with current Blackwell state (#942) ([#942](https://github.com/noonghunna/club-3090/pull/942) by @paulp83)
- docs(deepseek): first canonical bench published for both dual slugs ([d14feca](https://github.com/noonghunna/club-3090/commit/d14feca45984464f808e223b2245f8b0d646a0e0))
- docs(upstream): moe-cache v2 non-gated validation done on mainline fork; ggml-org agent-contribution policy row ([1ee3e49](https://github.com/noonghunna/club-3090/commit/1ee3e49ff0e27051b9686ab4344d5d2ce35be98e))
- docs(upstream): track leloch's moe-cache RFC — v2 rebased, validation landed, prefill is the open cost ([789c41d](https://github.com/noonghunna/club-3090/commit/789c41d88cb37f779675c1f4067971ade00d87fe))
- docs(p2p): decode gain is the KERNEL and we auto-enable it; add the engine split (#928) ([#928](https://github.com/noonghunna/club-3090/pull/928) by @noonghunna)
- docs(p2p): stop overselling the patched-P2P gain; lead with prefill and the risk (#925) ([#925](https://github.com/noonghunna/club-3090/pull/925) by @noonghunna)
- docs(upstream): track the ik-llama pin bump for the hybrid-GDN np>1 fix ([f1bfa1f](https://github.com/noonghunna/club-3090/commit/f1bfa1f615ab909180c2ceee12776c1771996311))
- docs(ik-llama): NP=1 is REQUIRED on the hybrid-GDN slug, not merely defaulted (#920) ([#920](https://github.com/noonghunna/club-3090/pull/920) by @noonghunna)
- docs(dual-card): drop stray blank line from the cherry-picked sampling note ([3314b1b](https://github.com/noonghunna/club-3090/commit/3314b1bfa0234e0c6730073c3219e973826b7813))
- docs(dual-card): temperature is best controlled per-task by the agent/harness, not the server default (#662) ([aa3589c](https://github.com/noonghunna/club-3090/commit/aa3589c0af635c70a4421c82b79bce1684a07697))
- docs(dual-card): document Qwen3.6-27B sampling defaults (coding temp 0.6) + TEMP=1.0 reasoning override, min-p 0 caveat (#662) ([00fcd4d](https://github.com/noonghunna/club-3090/commit/00fcd4db85039d28a49c7781d61ef9db448d2b27))
- docs(agents): two c3 test traps that both produce false green/red ([777c34f](https://github.com/noonghunna/club-3090/commit/777c34f5ff5ad9f5b14fde2ae832f8c8ffc4768e))
- docs(adding-models): cover the acquisition path, not just serving ([05a9c41](https://github.com/noonghunna/club-3090/commit/05a9c410d755f27c3b4fe7e51fb8c964ae1fa4d8))
- docs: #24489 was never our bug -- one root cause, not two (#897) ([#897](https://github.com/noonghunna/club-3090/pull/897) by @noonghunna)
- docs(p2p): physical layer -- CPU vs chipset lanes, real PLX switches, risers (#895) ([#895](https://github.com/noonghunna/club-3090/pull/895) by @noonghunna)
- docs(p2p): per-engine enablement, bare-metal vs VM paths, and their pitfalls (#894) ([#894](https://github.com/noonghunna/club-3090/pull/894) by @noonghunna)
- docs(p2p): layer-stack + TP/PP/EP diagrams, and the clique's real verdict (#893) ([#893](https://github.com/noonghunna/club-3090/pull/893) by @noonghunna)
- docs(p2p): NCCL correction + symptom-first gotcha reference for the whole arc (#892) ([#892](https://github.com/noonghunna/club-3090/pull/892) by @noonghunna)
- docs(p2p): a passing transfer test is NOT sufficient -- measured (#891) ([#891](https://github.com/noonghunna/club-3090/pull/891) by @noonghunna)
- docs(p2p): the WORKING Proxmox recipe -- x-nv-gpudirect-clique, verified (#890) ([#890](https://github.com/noonghunna/club-3090/pull/890) by @noonghunna)
- docs(p2p): the exact chipset gate behind CNS, and two no-compile escapes (#886) ([#886](https://github.com/noonghunna/club-3090/pull/886) by @noonghunna)
- docs(p2p): NVreg override measured and REFUTED on a virtualised rig (#885) ([#885](https://github.com/noonghunna/club-3090/pull/885) by @noonghunna)
- docs(p2p): add virtualised-rig path; correct a false VBIOS-cap claim (#884) ([#884](https://github.com/noonghunna/club-3090/pull/884) by @noonghunna)
- docs: bank the #873 P2P A/B, caveat its absolutes, credit @vladie (#883) ([#883](https://github.com/noonghunna/club-3090/pull/883) by @noonghunna)
- docs(p2p): add the Blackwell P2P A/B row, retire the "does not exist" claim (#882) ([#882](https://github.com/noonghunna/club-3090/pull/882) by @noonghunna)
- docs(p2p): scope the Blackwell registry override, add per-card P2P paths ([00e994a](https://github.com/noonghunna/club-3090/commit/00e994a37a6763fe44e4f4c6caad6c9bde05b4d3))
- docs: the serving tests auto-detect MODEL — correct the stale gotcha ([86aa893](https://github.com/noonghunna/club-3090/commit/86aa8931dec4d5d915e1b75a1ad07f0e1c0a9eb2))
- docs(nvfp4): prefix-caching-OFF is policy, not pending wiring (#810) ([74e63db](https://github.com/noonghunna/club-3090/commit/74e63db8dca5c8163f5847c5a5bc5c67d6dd833a))
- docs: Results Card v2 — henrykrinkle01's quality table + enriched Serving (#806) ([ecb093b](https://github.com/noonghunna/club-3090/commit/ecb093babb2500c2bcf3b241ee41fc6eb5be6f7b))
- docs(upstream): vllm#50021 row — sean's patched-build sustained confirmation ([34c1c59](https://github.com/noonghunna/club-3090/commit/34c1c5951924be9c7ec849f5cf59a8d7abe45809))
- docs(composes): caveat the vllm#50021 MTP x hybrid-GDN exposure on all 9 MTP-on slugs ([5d19929](https://github.com/noonghunna/club-3090/commit/5d19929324f3a6d301de4ddc99eda349833a1b04))
- docs(upstream): track vllm#50021 (MTP x hybrid-GDN wild write) + vllm#44209 envelope ([7f9f6d1](https://github.com/noonghunna/club-3090/commit/7f9f6d1ae117b38503eec54973cec2504d0032fd))
- docs(offload-matrix): equal n-max does not make drafters comparable ([759101d](https://github.com/noonghunna/club-3090/commit/759101dec3014a06fa5287bd9a5351803ff3079b))
- docs(p2p): explain WHY layer 3's gate is NVLink-only; record the bypass decision ([ef2467c](https://github.com/noonghunna/club-3090/commit/ef2467c1563161cc3a2887bfc4530f0155b7891a))
- docs(bench): grow both card templates for offload/PCIe/RAM telemetry ([89cfa56](https://github.com/noonghunna/club-3090/commit/89cfa5659ee74f67b67d520bfb81718f2b3271b0))
- docs(bench): record which card fields auto-fill + the new capture knobs ([0e19967](https://github.com/noonghunna/club-3090/commit/0e1996746b62ad4cb79cbb8238ad1ae4745ed5bf))
- docs: add BENCH_CARD.md — per-run bench.sh card templates (Snapshot + A/B) ([fc96f4c](https://github.com/noonghunna/club-3090/commit/fc96f4c932adabe793ad3a320ce4f26a0ce1385a))
- docs(p2p): patched-module auto-enable can silently hang vLLM at pynccl init ([fd28f7b](https://github.com/noonghunna/club-3090/commit/fd28f7b288ac0754119185c3550a3c3ab1296802))
- docs(offload-matrix): correct the between-boot variance figure ([921f58c](https://github.com/noonghunna/club-3090/commit/921f58caa11fbce8791f112208d6e33228709db5))
- docs(multi-card): the matched-recipe TP pair lands in the scoped section (#773) ([4bd960e](https://github.com/noonghunna/club-3090/commit/4bd960e2bb3be3b77c58726d3bfe2bad776eaee6))
- docs: 5090 NVFP4-KV thread round 2 — V-scale root cause + the owed 35B 8-pack (disc #765) ([9c125ec](https://github.com/noonghunna/club-3090/commit/9c125ec193c0e00216144191c68b485921ca882f))
- docs(p2p): three-layer overview up top + retire the stale ~+15% NVLink figure ([a872025](https://github.com/noonghunna/club-3090/commit/a872025c87eaadcc57db270735c11ddb8adb8b1b))
- docs(dtype): re-land the #773 backend-tiers row — its A/B gate has fired ([8ffa898](https://github.com/noonghunna/club-3090/commit/8ffa898667f8275c5adf3b53442f1f863f7aa957))
- docs(dtype): #594 backend-selection — cross-rig confirmation + TQ depth tiers (#773) ([f7ccce3](https://github.com/noonghunna/club-3090/commit/f7ccce3d0f7985e91d38d3a7717d23bcc463f7bb))
- docs(engines): vllm-stable notes read two pins out of date ([a61d7a6](https://github.com/noonghunna/club-3090/commit/a61d7a67fa35758abf93347506b306edf446a3f6))
- docs(bench): the P2P-engagement gap is historical, not a tooling gap ([0e2a364](https://github.com/noonghunna/club-3090/commit/0e2a36496aad344ce0ca9892d9cd4367c9248adf))
- docs: correct four claims the community disproved (disc #765, #773) ([8a19292](https://github.com/noonghunna/club-3090/commit/8a19292e7f72558b1bc3753b6c8284b2c05123b2))
- docs(agents): lead the encoding rule with the UTF-8-mode guarantee ([f9897a8](https://github.com/noonghunna/club-3090/commit/f9897a8a2596f5f7edb276ea15ca278feeab0ad1))
- Document vllm-gemma-stable x UUID-pinning incompatibility (#750) ([a929d96](https://github.com/noonghunna/club-3090/commit/a929d9631e8067699e77ae0074a170bb5992b4a3))
- docs: cloud/proxy endpoint testing + cloud references table (qwen3.8-max-preview) (#754) ([#754](https://github.com/noonghunna/club-3090/pull/754) by @noonghunna)
- docs(thinkingcap-27b): record the v0.9.7 harness provenance on the baseline row ([c3dab09](https://github.com/noonghunna/club-3090/commit/c3dab096ef6c19978ea2c26b4254b527ccbbe700))
- docs(nemotron-3-puzzle-75b): record maintainer validation for dual-w4a16 ([f2f8da1](https://github.com/noonghunna/club-3090/commit/f2f8da1d13c51493f9b3988333c6ed4c07181066))
- docs: canonical 262K fast-vs-max numbers — tiers are decode-tied, retire cross-session spread (#662) ([fbb858c](https://github.com/noonghunna/club-3090/commit/fbb858cec1fb042b698e436fd2454d50e42faba2))
- docs(quality-test): cli-40 variance is mode-dependent — think-off near-deterministic, think-on churny (#662) ([0a19a20](https://github.com/noonghunna/club-3090/commit/0a19a2030b455c3548daf14ca726f2e6c46ef902))
- docs(dual-card): revise fast/max decode numbers with same-session ABBA A/B (#662) ([9cbc2f1](https://github.com/noonghunna/club-3090/commit/9cbc2f1eb3b8b002e41c88c595cb6dc0f8d4b87e))
- docs(quality-test): note loopback-bound engines refuse sandbox connections (hermes 0/20 signature) (#741) ([0bf81b6](https://github.com/noonghunna/club-3090/commit/0bf81b6da726cfd4e9e23141268ffb5a2d6e28af))
- docs: DUAL_CARD.md — mark archived Carnice/dual-turbo rows, gate beellama dflash-dual on v0.4.0 bump (#740) ([35b2c0b](https://github.com/noonghunna/club-3090/commit/35b2c0b426ff833536b72974fb9639ff57abe354))
- docs(pcie-p2p): VBIOS gates ReBAR/BAR1 on Ampere consumer cards (#734) ([31268fc](https://github.com/noonghunna/club-3090/commit/31268fcdff92b48eb0ea72e4121c0fc4c6fbb179))
- docs(upstream): record the write-side proposal posted on vllm#43559 ([ae0c188](https://github.com/noonghunna/club-3090/commit/ae0c1882ab95193c70236a2c13843869bce09d5e))
- docs(tess): same-rig prefill A/B — fill PP cells + baselines prefill_tps ([1021474](https://github.com/noonghunna/club-3090/commit/1021474a18060eaf16242f9d5499e2c96040936f))
- docs(upstream): dedicated tracking rows for the filed W4A8 bugs (vllm#48904, #48905) ([3a4e63a](https://github.com/noonghunna/club-3090/commit/3a4e63a08c81a4a7697070151e439f3bcab7e027))
- docs: record upstream W4A8 bug filings (vllm#48904 INC input_dtype, vllm#48905 unsigned scale read) ([c2ce99c](https://github.com/noonghunna/club-3090/commit/c2ce99c9bb524815c4f634ac68ebd3ae00e2e182))
- docs(nemotron): add util→KV-pool headroom note to the compose (#717) ([#717](https://github.com/noonghunna/club-3090/pull/717) by @noonghunna)
- docs(upstream): beellama DFlash-on-Ada FILED — Anbeeld#91 (broken on v0.3.1 stable too; not a preview regression) ([c120fca](https://github.com/noonghunna/club-3090/commit/c120fca3a74ea296e8364fcf45bb8047eac2355e))


### 🔧 Pin bumps + upstream

- Bump vllm-stable pin v0.24.0 → v0.25.1 (arm waived; single-card live-validated) (#682) ([#682](https://github.com/noonghunna/club-3090/pull/682) by @noonghunna)


### 🧹 Maintenance

- refactor(profiles): lift derive_compose_facts out of the cockpit into shared profiles (#1203) ([#1203](https://github.com/noonghunna/club-3090/pull/1203) by @noonghunna)
- chore(patches): delete the pr35936 required-fallback patch — verified unnecessary (#1189) ([3ba8816](https://github.com/noonghunna/club-3090/commit/3ba88160314b5ae40384bf9303adb6c33ed4de85))
- chore(registry): moe-cache slugs incubating -> experimental, engine label v1.5 -> v1.6 ([c207b93](https://github.com/noonghunna/club-3090/commit/c207b93af19f4949a1e543fe916803edfb86e624))
- test(c3): tidy the new UX-review test file ([3a2b714](https://github.com/noonghunna/club-3090/commit/3a2b7143a6e55ec48b66fda661fcc30344a3a732))
- chore(scripts): make the 30 shebang scripts that are executed +x, and guard it ([265e3a0](https://github.com/noonghunna/club-3090/commit/265e3a0207a10a01f0aa5720d2adf1ee674f1906))
- test: guard against a caveat promising an upstream fix we already patch (#1147) ([77ca4fe](https://github.com/noonghunna/club-3090/commit/77ca4fe77bdf94e7655510e087badfb0a73a4ba2))
- test(profiles): engine count 16 -> 17 for the v1.6 profile ([ff2ea24](https://github.com/noonghunna/club-3090/commit/ff2ea24971cbcb5c190fe25ec98ec490dc8a2901))
- test(preflight): map the GLM IQ3_XXS slugs to their composes ([4aa2ed8](https://github.com/noonghunna/club-3090/commit/4aa2ed82f2ffa67dec29b032a818dabf2279aed7))
- test(catalog): drift-guard the registry `offload` facet ([8fb5194](https://github.com/noonghunna/club-3090/commit/8fb5194dff8754967e9eb5bcbd68efac1b198a4a))
- test(list-topology-filter): neutralize per-model default pins ([125c54d](https://github.com/noonghunna/club-3090/commit/125c54d8a20d58cda044fc3ae3e1aa2f690add67))
- chore(genesis): #1040 — remove dead Genesis code from the tooling ([541a945](https://github.com/noonghunna/club-3090/commit/541a9458e7ff8161534fdf9860e9e83f0e8160b7))
- test(route-g): exclude boot-residue cache dirs from the throwaway copy ([c7a93ac](https://github.com/noonghunna/club-3090/commit/c7a93ac83ac515ead93fef0052cbefde5e4e3bda))
- test(route-g): end-to-end all-legs walk — bring GGUF → fit → scaffold → promote local ([6cd6732](https://github.com/noonghunna/club-3090/commit/6cd6732581b2442274c033b81bd6b3e105c13e5b))
- test(spec-toggle): stub draft-flag paths so the #1054 fail-loud check stays inspectable ([68a8944](https://github.com/noonghunna/club-3090/commit/68a8944113cfa57ae72727726a9cdc05c27cd79e))
- test: add test-docs-slugs-resolve — assert documented commands can actually run (#1035) ([#1035](https://github.com/noonghunna/club-3090/pull/1035) by @noonghunna)
- test(compose): forbid maintainer-rig paths as env defaults ([2c0a93a](https://github.com/noonghunna/club-3090/commit/2c0a93a13cc8bc45407873614465aba9fa2d6cab))
- test: add the PYTHONUTF8 export the locale gate requires to 4 capture-era suites ([5e898db](https://github.com/noonghunna/club-3090/commit/5e898db4a25d17afa5fa1afc964b74bcff8c0500))
- test: guard the adoption — device-count detection, lib consumption, both remainders ([b0517ff](https://github.com/noonghunna/club-3090/commit/b0517ff603d4b7a98088bdc4a99272da8a2194e1))
- refactor(offload-matrix): adopt scripts/lib/capture.sh, delete the private copies ([7e234df](https://github.com/noonghunna/club-3090/commit/7e234df7b13ad0b89faa453f1db058b847b16e25))
- test(bench): card suite (19 checks) + capture guards for the corrected spec ([fb66cac](https://github.com/noonghunna/club-3090/commit/fb66cacd84d78b9dc4f777e5cdd2294097dd6e94))
- test(bench): mocked guards for the capture layer, extending the #835 pattern ([50bb67b](https://github.com/noonghunna/club-3090/commit/50bb67b28807df79e9d39418fd9f4f71ab0660e8))
- test(offload-matrix): 3-tier suite + fix CACHE_DISABLED per-device hole (#824) ([95d7a61](https://github.com/noonghunna/club-3090/commit/95d7a61295d41be3ff10ed8d7fb4047e359c3d65))


### 🧹 Other

- Merge #1193: delete the pr35936 required-fallback patch — verified unnecessary (#1189) ([#1193](https://github.com/noonghunna/club-3090/pull/1193) by @noonghunna)
- Merge #1192: repair the generate-compose fixtures #1188 broke ([#1192](https://github.com/noonghunna/club-3090/pull/1192) by @noonghunna)
- Merge #1190: gpu-fit failure gives Linux-only advice that is a dead end on WSL (#1134) ([#1190](https://github.com/noonghunna/club-3090/pull/1190) by @noonghunna)
- Merge #1188: two dormant patch entries stop claiming load-bearing status (#1012) ([#1188](https://github.com/noonghunna/club-3090/pull/1188) by @noonghunna)
- Merge #1187: test-bench-capture must start the bench right after the first stats sample (#1137) ([#1187](https://github.com/noonghunna/club-3090/pull/1187) by @noonghunna)
- Merge #1186: qwen3.8-27b vision headers from measurement — all three dual tiers see (#1181) ([#1186](https://github.com/noonghunna/club-3090/pull/1186) by @noonghunna)
- Merge #1185: correct the stale "Vision: ✅ WORKING" header on all 8 qwen3.8-27b vLLM composes (#1181) ([#1185](https://github.com/noonghunna/club-3090/pull/1185) by @noonghunna)
- Merge #1184: args-array-scope gate must export PYTHONUTF8 (#779) ([#1184](https://github.com/noonghunna/club-3090/pull/1184) by @noonghunna)
- Merge #1183: qwen3.8-27b reasoning_effort high -> xhigh, not medium ([#1183](https://github.com/noonghunna/club-3090/pull/1183) by @noonghunna)
- Merge #1094: accept reasoning_effort "high" on the Qwen3.8 vLLM slugs ([#1094](https://github.com/noonghunna/club-3090/pull/1094) by @noonghunna)
- Merge #1182: port the MAMBA_BLOCK_SIZE knob to the other seven qwen3.8-27b composes (+ args-array scope gate) ([#1182](https://github.com/noonghunna/club-3090/pull/1182) by @noonghunna)
- Merge #1170: qwen3.8-27b dual-fast MAMBA_BLOCK_SIZE knob — recovers ~20% effective KV pool on hybrid-GDN ([#1170](https://github.com/noonghunna/club-3090/pull/1170) by @noonghunna)
- Merge #1180: c3 estate-bar VRAM breakdown with per-GPU drill-down (#1118) ([#1180](https://github.com/noonghunna/club-3090/pull/1180) by @noonghunna)
- Merge #1179: regenerate litellm config for the #1175 status change; stop the test hard-coding a status ([#1179](https://github.com/noonghunna/club-3090/pull/1179) by @noonghunna)
- Merge #1177: glm-5.3-flash — wire KV_TYPE on the dual moecache compose (default f16) ([#1177](https://github.com/noonghunna/club-3090/pull/1177) by @noonghunna)
- Merge #1176: glm-5.3-flash dual moecache drafter depth SPEC_N 3 -> 2 (+8-10% decode) ([#1176](https://github.com/noonghunna/club-3090/pull/1176) by @noonghunna)
- perf(glm-5.3-flash): dual moecache drafter depth SPEC_N 3 -> 2 (+8-10% decode) ([ff3f12f](https://github.com/noonghunna/club-3090/commit/ff3f12f64c5c1bad8affdf63fffa707da01776df))
- Merge #1175: moe-cache slugs incubating -> experimental, engine label v1.5 -> v1.6 ([#1175](https://github.com/noonghunna/club-3090/pull/1175) by @noonghunna)
- Merge #1174: hf_fetch — missing hf binary escalates to rung 3, CLI announces failure (#1132) ([#1174](https://github.com/noonghunna/club-3090/pull/1174) by @noonghunna)
- Merge #1173: setup.sh — skip non-numeric WEIGHT_SIZE_GB in the disk gate (#1131) ([#1173](https://github.com/noonghunna/club-3090/pull/1173) by @noonghunna)
- Merge #1172: vram-breakdown — count drafter weights and GLM recurrent state (#1171) ([#1172](https://github.com/noonghunna/club-3090/pull/1172) by @noonghunna)
- Merge #1169: c3 — deferred tab-activation focus must not steal the tab bar or reach past a modal ([#1169](https://github.com/noonghunna/club-3090/pull/1169) by @noonghunna)
- Merge #1168: c3 UX cleanup — five small fixes ([#1168](https://github.com/noonghunna/club-3090/pull/1168) by @noonghunna)
- Merge #1167: c3 UX review — key-hint markup, footer honesty, focus traps, narrow terminals ([#1167](https://github.com/noonghunna/club-3090/pull/1167) by @noonghunna)
- Merge #1166: the reserve is NOT the lever — more slots measured 12.5% slower ([#1166](https://github.com/noonghunna/club-3090/pull/1166) by @noonghunna)
- Merge #1165: declare the engine-read knobs on all 16 moe-cache composes ([#1165](https://github.com/noonghunna/club-3090/pull/1165) by @noonghunna)
- Merge #1164: two v1.6 moe-cache engine findings, both measured on the rig ([#1164](https://github.com/noonghunna/club-3090/pull/1164) by @noonghunna)
- Merge #1163: stop claiming things the code and the record don't support ([#1163](https://github.com/noonghunna/club-3090/pull/1163) by @noonghunna)
- Merge #1162: demote.py — remove a local model, with an end-to-end lifecycle test ([#1162](https://github.com/noonghunna/club-3090/pull/1162) by @noonghunna)
- Merge #1161: view the compose behind a slug — [c] opens it, read-only ([#1161](https://github.com/noonghunna/club-3090/pull/1161) by @noonghunna)
- Merge #1160: Doctor's checks are a keyboard list — ↑/↓ pick, ⏎ runs ([#1160](https://github.com/noonghunna/club-3090/pull/1160) by @noonghunna)
- Merge #1159: Bring & Validate UX pass — visible focus, honest copy, working stages ([#1159](https://github.com/noonghunna/club-3090/pull/1159) by @noonghunna)
- Merge #1158: Route-K — ① accepts a compose you already wrote ([#1158](https://github.com/noonghunna/club-3090/pull/1158) by @noonghunna)
- Merge #1157: ⑤ Promote never passed the compose, so every LOCAL write was refused ([#1157](https://github.com/noonghunna/club-3090/pull/1157) by @noonghunna)
- Merge #1155: state the written layer, pose the default, and un-break the test fixture ([#1155](https://github.com/noonghunna/club-3090/pull/1155) by @noonghunna)
- Merge #1154: make the RAM-derivation refusal loud, and split its two failure causes ([#1154](https://github.com/noonghunna/club-3090/pull/1154) by @noonghunna)
- Merge #1152: keep local models out of the curated port band; document what destroys the layer ([#1152](https://github.com/noonghunna/club-3090/pull/1152) by @noonghunna)
- Merge #1151: make the 30 shebang scripts that are executed +x, and guard it ([#1151](https://github.com/noonghunna/club-3090/pull/1151) by @noonghunna)
- Merge #1149: guard against a caveat promising an upstream fix we already patch ([#1149](https://github.com/noonghunna/club-3090/pull/1149) by @noonghunna)
- Merge #1148: correct the multi4/multi8-max wild-write caveat — same two-fault split as the dual ([#1148](https://github.com/noonghunna/club-3090/pull/1148) by @noonghunna)
- Merge #1146: correct the dual-max wild-write caveat — two faults, one patched, one still live ([#1146](https://github.com/noonghunna/club-3090/pull/1146) by @noonghunna)
- Merge #1139: wire ASYNC_SCHED=off on dual-max — vllm#50021 mitigation (1), drafter kept ([#1139](https://github.com/noonghunna/club-3090/pull/1139) by @noonghunna)
- Merge #1145: honour repo-root .env so the core-promote gate stops being a silent no-op ([#1145](https://github.com/noonghunna/club-3090/pull/1145) by @noonghunna)
- Merge #1143: route BYOM to the local model layer, not the curated catalog ([#1143](https://github.com/noonghunna/club-3090/pull/1143) by @noonghunna)
- Merge #1138: bare passthroughs for VLLM_CACHE_ROOT and VLLM_LOG_STATS_INTERVAL ([#1138](https://github.com/noonghunna/club-3090/pull/1138) by @noonghunna)
- Merge #1135: ship thinking by default across all 22 qwen3.8-27b composes ([#1135](https://github.com/noonghunna/club-3090/pull/1135) by @noonghunna)
- Merge #1136: DeepSeek-V4-Flash-Vision-Exp HAS vision — correct catalog + profile rationale ([#1136](https://github.com/noonghunna/club-3090/pull/1136) by @noonghunna)
- Merge #1121: compose alignment, census double-count fix, corrected DeepSeek-Vision numbers ([#1121](https://github.com/noonghunna/club-3090/pull/1121) by @noonghunna)
- Merge #1119: DeepSeek-V4-Flash-Vision-Exp, portable -t defaults, VRAM component split ([#1119](https://github.com/noonghunna/club-3090/pull/1119) by @noonghunna)
- Merge #1116: GLM-5.3-Flash + Qwen3.8-Flash-Next on the moe-cache engine, pinned to v1.6 ([#1116](https://github.com/noonghunna/club-3090/pull/1116) by @noonghunna)
- perf(bench): per-depth PREFILL_RUNS, default 3,1 ([c9c3b49](https://github.com/noonghunna/club-3090/commit/c9c3b49d8cfc7112657769d454a87d0e49fe20d9))
- perf(setup): skip SHA re-verify when sha+size+mtime+revision are unchanged ([7e963d8](https://github.com/noonghunna/club-3090/commit/7e963d89b1897a5ac81f719c84c67a1d406d881a))
- perf(deepseek-v4-flash): default -ub/-b 2048 -> 4096 after re-measurement ([38a1b81](https://github.com/noonghunna/club-3090/commit/38a1b811ac20022747c64eca35381ac0a3bcf91f))
- Merge #1030: c3 Containers log-follow ([f]) — live tail with pause/resume ([#1030](https://github.com/noonghunna/club-3090/pull/1030) by @noonghunna)
- Merge #1046: test(list-topology-filter) — neutralize per-model default pins ([#1046](https://github.com/noonghunna/club-3090/pull/1046) by @noonghunna)
- Merge c3/add-model-ux: registry uplift + c3 add-model experience ([4d0ce4b](https://github.com/noonghunna/club-3090/commit/4d0ce4bc832af2868bd91b2438e32df92e9a9000))
- Merge master (4e6c3363) into c3/add-model-ux ([65680b1](https://github.com/noonghunna/club-3090/commit/65680b17e6314798a222e6d738fdb5701e15792f))
- Give the llama.cpp lineage the same drafter toggle (closes #1049) (#1050) ([#1050](https://github.com/noonghunna/club-3090/pull/1050) by @noonghunna)
- Unify the spec-decode drafter toggle across all 27 vLLM composes (#1048) ([#1048](https://github.com/noonghunna/club-3090/pull/1048) by @noonghunna)
- promote(qwen3.8-27b): dual-max incubating -> experimental after first boot + verify-full + bench (#1032) ([#1032](https://github.com/noonghunna/club-3090/pull/1032) by @noonghunna)
- bump(vllm-stable): v0.25.1 -> v0.27.1 (#1013) ([#1013](https://github.com/noonghunna/club-3090/pull/1013) by @noonghunna)
- Gate the Inkling moe-cache slugs + ship a residency sibling (#978) (#979) ([#979](https://github.com/noonghunna/club-3090/pull/979) by @noonghunna)
- Gate the moe-cache DeepSeek slugs: they had no host-RAM header (#977) ([#977](https://github.com/noonghunna/club-3090/pull/977) by @noonghunna)
- docs/UPSTREAM: #954 closed without upstream filing; this row is now the tracker ([0e9efad](https://github.com/noonghunna/club-3090/commit/0e9efad69a3bc6c931a4f44c5d9b54a32c175c6d))
- residency: split the drafter out of the static reserve (#953) (#969) ([#969](https://github.com/noonghunna/club-3090/pull/969) by @noonghunna)
- Harness integrity: BENCHMARKS.md false-fail, incomplete bench sampler, hermes reachability preflight (#968) ([#968](https://github.com/noonghunna/club-3090/pull/968) by @noonghunna)
- Retire all single-card llama.cpp + ik-llama qwen slugs and diffusiongemma (#966) ([#966](https://github.com/noonghunna/club-3090/pull/966) by @noonghunna)
- c3: add [w] downloaded-only catalog filter (#965) ([#965](https://github.com/noonghunna/club-3090/pull/965) by @noonghunna)
- Retire two ubergarm-iq4ks and all four mudler-apex slugs (#964) ([#964](https://github.com/noonghunna/club-3090/pull/964) by @noonghunna)
- Retire Ex0bit, byteshape, prithivMLmods/VibeThinker and bytkim slugs (#956) ([#956](https://github.com/noonghunna/club-3090/pull/956) by @noonghunna)
- Detect the model's reasoning switch instead of assuming Qwen's (#957) ([#957](https://github.com/noonghunna/club-3090/pull/957) by @noonghunna)
- Add Inkling-Small: two moe-cache slugs on a dedicated engine pin (#958) ([#958](https://github.com/noonghunna/club-3090/pull/958) by @noonghunna)
- Collapse repeated `-ot` into one comma-separated arg (fixes #948) (#949) ([#949](https://github.com/noonghunna/club-3090/pull/949) by @noonghunna)
- Add 90K prefill, TTFT, peak VRAM and draft acceptance to the DeepSeek row ([75c460a](https://github.com/noonghunna/club-3090/commit/75c460a0fbb56b8ae0d994d22f4c5b4280a79635))
- Record DeepSeek moe-cache quality + canonical bench numbers ([acf8fa0](https://github.com/noonghunna/club-3090/commit/acf8fa075c02c65826dbf2cd0f533ce55df5cca4))
- Add RTX A6000 hardware profile (GA102 / SM 8.6 / 48 GB) (#950) ([#950](https://github.com/noonghunna/club-3090/pull/950) by @noonghunna)
- Ignore .claude/ agent working state ([37d71e8](https://github.com/noonghunna/club-3090/commit/37d71e88cedc2534e89841c11bb2ac408cbe2c8e))
- Print applied residency (and its source) at launch (#933) ([#933](https://github.com/noonghunna/club-3090/pull/933) by @noonghunna)
- Let explicit OT_G<i> env win over auto-sized residency (#932) ([#932](https://github.com/noonghunna/club-3090/pull/932) by @noonghunna)
- Make the CPU-offload RAM gate residency-aware (#930) ([#930](https://github.com/noonghunna/club-3090/pull/930) by @noonghunna)
- services(litellm): route the DeepSeek-Flash slug through the gateway ([3061914](https://github.com/noonghunna/club-3090/commit/3061914e289b1ab8966e42f18a4f96a7e63ec578))
- bump(llama.cpp): server-cuda-b9967 → b10236 (DSpark; unblocks DeepSeek-Flash slugs) (#904) ([#904](https://github.com/noonghunna/club-3090/pull/904) by @noonghunna)
- p2p: scope the runtime messages to the card they apply to (#873 follow-up) ([01d8649](https://github.com/noonghunna/club-3090/commit/01d86496ac7a6fcb3dd3c4f03608912663aae7a6))
- report: tell 2-card PCIe rigs which P2P gate they are behind (#873) ([49ea265](https://github.com/noonghunna/club-3090/commit/49ea2657d502f0b532c2ff18691f64bfed767c2e))
- p2p: wire the transfer check, correct the auto-detect advisory (#873) ([17ca5b5](https://github.com/noonghunna/club-3090/commit/17ca5b517577237f553e2669cde4e3c4bd3a4bb4))
- p2p: correct the BAR1 story with #873's measured numbers ([1cca5e0](https://github.com/noonghunna/club-3090/commit/1cca5e0f0426b7a47bb840be29645d80b1bcc9c2))
- p2p: warn when BAR1 can't back the static-BAR1 P2P mapping (#873) ([ac4f4b1](https://github.com/noonghunna/club-3090/commit/ac4f4b1501b4414e4081378107c165035d3612b7))
- Probe the unlisted scene ports in gpu-mode status (#865) ([d992dca](https://github.com/noonghunna/club-3090/commit/d992dca404c961b9fca7bbe4804dbe2bfa5fe416))
- gpu-mode: say what the status line actually means (#865) ([2e22b28](https://github.com/noonghunna/club-3090/commit/2e22b282b1638da8adee23b9bd9a093225424ef7))
- bench+fix: htsglang mixed-VRAM row (#845) · gpu-mode status drift (#865) ([0cf0dd7](https://github.com/noonghunna/club-3090/commit/0cf0dd785d9d3c0d88b298613d649a2cd5a40113))
- profiles: promote decode_granularity into the model schema (#809 residual) ([81f76eb](https://github.com/noonghunna/club-3090/commit/81f76eba61873b62e35330916e38eb8fbd3a7590))
- bench-agentic: kill the epsilon divide, mirror the #854 ratio guard (#809 residual) ([439fc2e](https://github.com/noonghunna/club-3090/commit/439fc2e0758efa0a532037c623e88e446b02d9a1))
- c3: route the GGUF Bring download through the hf_fetch ladder (#804) ([af7a6e6](https://github.com/noonghunna/club-3090/commit/af7a6e69489e51c9fd6f05548555e49d491c4f01))
- setup: stop counting unverifiable files as SHA-verified (#857) ([27be701](https://github.com/noonghunna/club-3090/commit/27be70115a72f145d2dcf8682f525e6a1e7ad9bd))
- bench/rebench: three-layer interconnect capture + agentic & concurrency parity (#805) ([ab6108c](https://github.com/noonghunna/club-3090/commit/ab6108c43264f3ae83a274e424d6eb6d3c501126))
- downloader: three-rung resilience ladder for the >50 GB refusal (#804) ([5198c0d](https://github.com/noonghunna/club-3090/commit/5198c0d7a47c14a4bb0ec10614f2e494012720d3))
- downloader: verify weights in place + announce why a re-download starts (#812) ([7fe64ae](https://github.com/noonghunna/club-3090/commit/7fe64ae0be8690490410a7bb999820520b2b4947))
- status: flip the six vllm#50021-exposed slugs to ⚠️ Production w/ caveats ([1b2e386](https://github.com/noonghunna/club-3090/commit/1b2e38642b515557a0f2af228ac3086f2efa1db4))
- render: surface pool / hits / evictions in the default perf view ([f7e964d](https://github.com/noonghunna/club-3090/commit/f7e964de10606abc9a5e64c6cd2f342a8b2c3b9b))
- offload-matrix: stop INVALID_BYPASS overstating what it proves ([96fc191](https://github.com/noonghunna/club-3090/commit/96fc191eda5982676c094eaab5d8f18430df551a))
- offload-matrix: reap the layer probe's server on every exit path ([2f9d29f](https://github.com/noonghunna/club-3090/commit/2f9d29f4099c0665d44cfb441fc136a6a8b6fda2))
- offload-matrix: fix the three defects the first real matrix exposed ([a0313a5](https://github.com/noonghunna/club-3090/commit/a0313a53636debe112dc4e4bd434540bf39a818f))
- offload-matrix: make prefix caching an explicit, recorded dimension ([81928a1](https://github.com/noonghunna/club-3090/commit/81928a1e2252728b28ce3e35f964bb12db0c48c5))
- concurrency-probe: report NaN aggregate when a round had errors ([28a1494](https://github.com/noonghunna/club-3090/commit/28a1494062a2f9a37d6fc7bf9b03d1b19f81ee02))
- fixup(spark-dashboard): keep DOCKER_GID parameterized, drop unrelated UPSTREAM.md row ([e9b5595](https://github.com/noonghunna/club-3090/commit/e9b5595bc94d479ff4a94bbd301886dd63ff3d46))
- concurrency-probe: report TTFT + derived prefill tok/s per round and in verdict/RESULT ([6f52fef](https://github.com/noonghunna/club-3090/commit/6f52fef40de2727b3490c3216875711e700cab76))
- add offload-matrix: sweep CPU-offloaded MoE serving configs ([e94f6fa](https://github.com/noonghunna/club-3090/commit/e94f6fa96fdb739643e390a22f96230010dfa0be))
- probe: fail loudly when slot detection fails; add -np and /props detection (#818) (#819) ([#819](https://github.com/noonghunna/club-3090/pull/819) by @noonghunna)
- upstream: record #49757 do-not-vendor-on-v0.25.1 guard (sean's arm-H crash data, #810) ([4f712bf](https://github.com/noonghunna/club-3090/commit/4f712bf8ab39fcf2e523f393891ed9ad68f91b95))
- housekeeping: DTYPE_MATRIX V-scale retraction correction (#765), 43562 re-test trigger amendment, 35B nvfp4 KV stock-pin note ([8cb31b8](https://github.com/noonghunna/club-3090/commit/8cb31b896eca4ae83dd8a4c9e82c65bb9e856d50))
- compose caveats: complete the NVFP4-KV stock-pin reframe on the two sibling slugs ([a5f71b8](https://github.com/noonghunna/club-3090/commit/a5f71b8575892801e260041bf437f2063c83c0e6))
- compose caveats: NVFP4-KV stock-pin reframe + 65K-pin FP8-consequent + WSL allocator + #619 trap set (#765 #613 #617 #619) ([597f642](https://github.com/noonghunna/club-3090/commit/597f64228c3df7ec9e01278e1deb9efd54096d98))
- UPSTREAM: vllm#46329 row — SM120 NVFP4-KV V-scale write fix (jethac); the fix behind #765's 131K+MTP result ([6a4385b](https://github.com/noonghunna/club-3090/commit/6a4385bef8d318b164252898f056608c788d7ae4))
- BENCHMARKS: mixed-arch row corrections — 3090 Ti designation, 290 W cap, parity claim precision (#761) ([e048acd](https://github.com/noonghunna/club-3090/commit/e048acd89b8745f716c02aceafa9375e2f519f75))
- Fix power-cap sweep metrics and GPU limits (#802) ([#802](https://github.com/noonghunna/club-3090/pull/802) by @noonghunna)
- c3: add opt-in master logging (#801) ([#801](https://github.com/noonghunna/club-3090/pull/801) by @noonghunna)
- retire(beellama): deprecate all 10 slugs, remove DEFAULTS + walk entries (#98 won't-fix) (#799) ([#799](https://github.com/noonghunna/club-3090/pull/799) by @noonghunna)
- BENCHMARKS: paulp83's 5090+3090 mixed-arch dual — decode identical to 2x3090 (#761) ([1015622](https://github.com/noonghunna/club-3090/commit/10156225947c2fd03f2b131517aed3846b7da044))
- BENCHMARKS+MULTI_CARD: dual-fast v0.25.1 first-party re-run — version confound resolved (#773) ([7cbdd51](https://github.com/noonghunna/club-3090/commit/7cbdd5148e1d20406ea5a3c9b024ecd00c2e0516))
- BENCHMARKS+DTYPE: #773 round 3 — matched TP pair lands, Whamp v0.25.1 KV depth A/B, stale P2P cells fixed ([343a8bf](https://github.com/noonghunna/club-3090/commit/343a8bffb353637ce6ab83219ff33b4e24363f3d))
- BENCHMARKS: Whamp recovered his P2P state — three-way confound narrows to two ([79bc424](https://github.com/noonghunna/club-3090/commit/79bc424c2404d45759a6c2158cde7778f9fd02a0))
- Revert "docs(dtype): #594 backend-selection — cross-rig confirmation + TQ depth tiers (#773)" ([37502e1](https://github.com/noonghunna/club-3090/commit/37502e17f2256fe722153eec25a2857ab00d04f0))
- status: beellama/qwen-dflash-dual 🧪 -> ⏸️ upstream-gated (#740) ([c5b1db9](https://github.com/noonghunna/club-3090/commit/c5b1db901ca3b97449ee28493ae20550b30cdb1f))
- Guarantee UTF-8 mode for every python3 the scripts run (#779) (#782) ([#782](https://github.com/noonghunna/club-3090/pull/782) by @noonghunna)
- c3: add catalog "offload" column (weight-offload backend facet) (#757) ([#757](https://github.com/noonghunna/club-3090/pull/757) by @noonghunna)
- Make submit-bench.sh work on non-UTF-8 locales, atomically (#777) (#780) ([#780](https://github.com/noonghunna/club-3090/pull/780) by @noonghunna)
- Make test-submit-bench self-contained instead of rig-dependent (#776) (#778) ([#778](https://github.com/noonghunna/club-3090/pull/778) by @noonghunna)
- Route every compose port through ${BIND_HOST:-0.0.0.0} + guard test (#764) ([#764](https://github.com/noonghunna/club-3090/pull/764) by @datanerdie)
- Publish canonical 8-pack pair 118/123; record the +/-3 n=1 noise band ([0d6baad](https://github.com/noonghunna/club-3090/commit/0d6baad4e269153d085313141e56a466dd8cda0c))
- Correct hermesagent attribution: confounded, not variance ([a2ac2fa](https://github.com/noonghunna/club-3090/commit/a2ac2fac7793f3d04b45d5be7b24475d086325b1))
- Wire froggeric template onto the 4 native 35B-A3B vLLM composes (#739) ([#739](https://github.com/noonghunna/club-3090/pull/739) by @noonghunna)
- c3: catalog search covers every display column (raw + label forms) ([23ec939](https://github.com/noonghunna/club-3090/commit/23ec939d1dbccad02a712e8ac275a04c1464270d))
- registry: chat_template facet — template regime queryable per slug ([51eb8d4](https://github.com/noonghunna/club-3090/commit/51eb8d4c03efc90089d26737eeacd206906b233b))
- gpu-mode: gemma scene off the deprecated compose; Tess hybrid corrections; kevin canary row ([a6a214f](https://github.com/noonghunna/club-3090/commit/a6a214f42d929c3253dac894a08faec2bf726974))
- Re-vendor froggeric chat template v19 -> v21.3 (#671: VSCode agent fix) (#738) ([#738](https://github.com/noonghunna/club-3090/pull/738) by @noonghunna)
- gpu-mode: start spark-dashboard in all serving scenes (+ off stops it) ([da68f06](https://github.com/noonghunna/club-3090/commit/da68f065703c7905158b49a9d90bc1858bfd8062))
- spark-dashboard: default DOCKER_GID 999 (community common case) ([4ed7833](https://github.com/noonghunna/club-3090/commit/4ed7833b8bd079e44abf044888c66b78a9df261b))
- services: add spark-dashboard — live GPU + vLLM runtime metrics (:3010) ([9ce4adf](https://github.com/noonghunna/club-3090/commit/9ce4adf72dd57d620d43dc7abc9f5660d8b0dc3c))
- Vendor vllm#48375 + flip prefix-caching default back ON (tiered) — ends the #720 interim (#736) ([#736](https://github.com/noonghunna/club-3090/pull/736) by @noonghunna)
- Add vllm/tess-dual-w4a16: the MTP-revival slug (262K, MTP n=5, #662) (#735) ([#735](https://github.com/noonghunna/club-3090/pull/735) by @noonghunna)
- c3: W4A8 int8-activation opt-in on the serve-confirm modal (#609) (#732) ([#732](https://github.com/noonghunna/club-3090/pull/732) by @noonghunna)
- W4A8 knob: wire multi-fast + document the nvfp4/fp8 exclusion (#609 follow-up) (#731) ([#731](https://github.com/noonghunna/club-3090/pull/731) by @noonghunna)
- W4A8 wiring: shipped serve-time knob on vllm/dual + vllm/minimal (#609) (#730) ([#730](https://github.com/noonghunna/club-3090/pull/730) by @noonghunna)
- Close out the #686 residuals: HF_TOKEN from .env + MoppelMat's 4-card row (#729) ([#729](https://github.com/noonghunna/club-3090/pull/729) by @noonghunna)
- hf(): stall watchdog + stale-lock clearing — fix the #726 lock-wait hang (#728) ([#728](https://github.com/noonghunna/club-3090/pull/728) by @noonghunna)
- Harden the AI Studio installer: prevent the #686 failure classes (#715) (#727) ([#727](https://github.com/noonghunna/club-3090/pull/727) by @noonghunna)
- c3 catalog: provider/GB/act columns + [|] column picker (closes #723, closes #724) (#725) ([#725](https://github.com/noonghunna/club-3090/pull/725) by @noonghunna)
- Deprecate vllm/qwen-27b-dual-balanced (tier-space review) ([c88cca3](https://github.com/noonghunna/club-3090/commit/c88cca337307d4d156f0a7a017f5cd875ee006a7))
- Qwen3-Next: prefix-caching OFF by default (MTP×prefix-cache #710) (#720) ([#720](https://github.com/noonghunna/club-3090/pull/720) by @noonghunna)
- nvfp4: note turbo4_nc KV craters recall on scale-less checkpoint ([0848dfa](https://github.com/noonghunna/club-3090/commit/0848dfa86825b63777586be58d34a163397764cc))
- Promote nemotron-75b-multi-mtp: experimental -> production w/ caveats (#706) (#716) ([#716](https://github.com/noonghunna/club-3090/pull/716) by @noonghunna)
- Harden setup-ai-studio.sh: fail loud on OWUI port-8080 conflict (#686) (#714) ([#714](https://github.com/noonghunna/club-3090/pull/714) by @noonghunna)
- Switch Qwen vLLM KV fp8_e5m2->fp8_e4m3 + HOL threshold on by default (#713) ([#713](https://github.com/noonghunna/club-3090/pull/713) by @noonghunna)
- Add --long-prefill-token-threshold 2048 to gemma-4-26b-a4b concurrent lanes (on-rig validated) (#712) ([#712](https://github.com/noonghunna/club-3090/pull/712) by @noonghunna)
- Env-ify --max-num-batched-tokens across 22 vLLM composes (behavior-identical) (#709) ([#709](https://github.com/noonghunna/club-3090/pull/709) by @noonghunna)
- Fix Nemotron OOM on 4x3090: chunked prefill on + 200K + fp8 KV (#708) ([#708](https://github.com/noonghunna/club-3090/pull/708) by @noonghunna)
- Add nemotron-3-puzzle-75b: experimental vllm/nemotron-75b-multi-mtp (4x3090 NVFP4) (#704) ([#704](https://github.com/noonghunna/club-3090/pull/704) by @noonghunna)



[Pin: `git checkout v0.11.0`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.10.2...v0.11.0)
## v0.10.2 — 2026-07-13


### ✨ Features

- feat(resolver): arch-gate the beellama DFlash single-card default off non-sm_86 (#693) (#696) ([#696](https://github.com/noonghunna/club-3090/pull/696) by @noonghunna)
- feat(c3): route-G [D] downloads GGUF files directly, not via pull.sh (#660) ([#660](https://github.com/noonghunna/club-3090/pull/660) by @noonghunna)
- feat(c3): route-G supports embedded MTP, not just external drafters (#659) ([#659](https://github.com/noonghunna/club-3090/pull/659) by @noonghunna)
- feat(c3): GGUF route-G fit + compose emit (#650) ([#650](https://github.com/noonghunna/club-3090/pull/650) by @noonghunna)
- feat(c3): UI/UX phase 3 — download preflight, jobs chip, route language (#649) ([#649](https://github.com/noonghunna/club-3090/pull/649) by @noonghunna)
- feat(c3): UI/UX phase 2 — B&V stage hierarchy (state → action → details) (#648) ([#648](https://github.com/noonghunna/club-3090/pull/648) by @noonghunna)
- feat(c3): ② Serve spec-dec — engine-driven drafter SELECTOR (not just on/off) (#638) ([#638](https://github.com/noonghunna/club-3090/pull/638) by @noonghunna)
- feat(c3): ② Serve editor — custom values, engine KV, real spec, preview (#637) ([#637](https://github.com/noonghunna/club-3090/pull/637) by @noonghunna)
- feat(c3): ② Serve override editor — retune served-name/ctx/KV/spec/util (#636) ([#636](https://github.com/noonghunna/club-3090/pull/636) by @noonghunna)
- feat(byo): apply-swap — download + serve a Route-C fine-tune (#628) ([#628](https://github.com/noonghunna/club-3090/pull/628) by @noonghunna)
- feat(c3): add Spec Dec column to Catalog + fold into funnel labels ([a62784c](https://github.com/noonghunna/club-3090/commit/a62784c132d559fd0e6328e8f86e788418cf2720))
- feat(nvfp4): SPEC=off toggle for the 27B nvfp4 composes (#617) ([f50db81](https://github.com/noonghunna/club-3090/commit/f50db81ee8bdd8882e3651daf62089167081021f))
- feat(c3): New-cluster setup modal — C2 (#610 Phase C, complete) ([6ea2531](https://github.com/noonghunna/club-3090/commit/6ea2531db829251f5508c4376850e01c5b2ae4b8))
- feat(c3): cluster view in the Operate pane — C1 (#610 Phase C) ([ee573f6](https://github.com/noonghunna/club-3090/commit/ee573f6cc46e47f9639cc6be769ea7fec36dca12))
- feat(cluster): scripts/cluster.sh — GPU-cluster management CLI (#610 Phase A′) ([70c87a1](https://github.com/noonghunna/club-3090/commit/70c87a139b8b1d14ad3fa7ee26dc37ad53269d86))
- feat(estate): UUID-pin estate GPUs + placement assertion (#610 Phase A) ([3970c2d](https://github.com/noonghunna/club-3090/commit/3970c2d7c50c80f000c8b752f569918e210a1b26))
- feat(qwen-moe): NVFP4 35B-A3B community slugs — the unified-memory pairing ([1ba1a89](https://github.com/noonghunna/club-3090/commit/1ba1a89d7ca65e93a3ed95fdb553968f514db7be))
- feat(quality): sandbox preflight hardening + benchlocal-cli in report.sh ([ea9c233](https://github.com/noonghunna/club-3090/commit/ea9c233fefcb406c9553a326ffc5135fc6091e67))
- feat(c3): hide hardware-incompatible slugs by default + warn-before-download ([e09eb3f](https://github.com/noonghunna/club-3090/commit/e09eb3f0afcc38fa2c350694f7e111e1464476e8))
- feat(qwen): NVFP4 community-validated slugs for Hopper/Blackwell (2 composes) ([34b1797](https://github.com/noonghunna/club-3090/commit/34b17975686290b5eabe9ca9202086a1c11352d9))
- feat(c3): add Weights + KV columns to the catalog ([18fcedb](https://github.com/noonghunna/club-3090/commit/18fcedb4fe4e26871a586c8446f64c65a718e48c))
- feat(qwen): flip multi-max to fp8/e4m3 KV + weights-conditional Ampere compat ([fabf9ce](https://github.com/noonghunna/club-3090/commit/fabf9ce1eab19331603912ba1dd0db4497f2bbc5))
- feat: switch dual-max KV from int8_per_token_head to fp8 ([6eaeb2b](https://github.com/noonghunna/club-3090/commit/6eaeb2bd447e3491b47bc2030cb7172411c6290e))


### 🐛 Bug fixes

- fix: restore pre-sweep power limits (#699) ([#699](https://github.com/noonghunna/club-3090/pull/699) by @kevinb361)
- fix(studio): setup-ai-studio no longer silently no-ops when .env lacks LANIP (#686) (#703) ([#703](https://github.com/noonghunna/club-3090/pull/703) by @noonghunna)
- fix(setup): consent-gated hf-CLI install — fixes PEP 668 externally-managed wall on WSL/Ubuntu 24.04 (#701) ([#701](https://github.com/noonghunna/club-3090/pull/701) by @noonghunna)
- fix(nvlink): pcie_p2p no longer claims "engaged" without verifying the driver granted it (#695) ([#695](https://github.com/noonghunna/club-3090/pull/695) by @noonghunna)
- fix(compat): C5 wrongly rejects nvfp4 + fp8_e4m3 KV on Ampere (#686) (#694) ([#694](https://github.com/noonghunna/club-3090/pull/694) by @noonghunna)
- fix(c3): put repo root on sys.path so ② Serve emit can import scripts (#657) ([#657](https://github.com/noonghunna/club-3090/pull/657) by @noonghunna)
- fix(test): sync test-pull-swap.sh emit asserts with P2b env-gating (#656) ([#656](https://github.com/noonghunna/club-3090/pull/656) by @noonghunna)
- fix(c3): route-C swap compose — absolute mounts + runtime-dir location (#655) ([#655](https://github.com/noonghunna/club-3090/pull/655) by @noonghunna)
- fix(c3): route-G GGUF serve — single /models mount + runtime-dir compose (#654) ([#654](https://github.com/noonghunna/club-3090/pull/654) by @noonghunna)
- fix(c3): honest "won't fit" verdict + reachable custom-slug hatch (#653) ([#653](https://github.com/noonghunna/club-3090/pull/653) by @noonghunna)
- fix(c3): honest ② Serve copy + GB disk-fit labels (post-#647/#649 nits) (#651) ([#651](https://github.com/noonghunna/club-3090/pull/651) by @noonghunna)
- fix(c3): UI/UX phase 1 — serve honesty, footer labels, promote preview (#647) ([#647](https://github.com/noonghunna/club-3090/pull/647) by @noonghunna)
- fix(ik-llama): driver-aware cu13/cu12 image select + preflight hint + docs (#633) (#640) ([#640](https://github.com/noonghunna/club-3090/pull/640) by @noonghunna)
- fix(launcher): GGUF verify-glob (#634) + .env engine-image passthrough (#632) (#639) ([#639](https://github.com/noonghunna/club-3090/pull/639) by @noonghunna)
- fix(c3): ② Serve honest for Route-C + [s] advance key (kill the dead-end) (#635) ([#635](https://github.com/noonghunna/club-3090/pull/635) by @noonghunna)
- fix(c3): ⏎ on ① Bring advances to ② Serve when weights present (#631) ([#631](https://github.com/noonghunna/club-3090/pull/631) by @noonghunna)
- fix(c3): hide [D] when brought weights on disk; ② Serve emits swap (#630) ([#630](https://github.com/noonghunna/club-3090/pull/630) by @noonghunna)
- fix(nvfp4): disable deepgemm on consumer cards ([fbf6ab9](https://github.com/noonghunna/club-3090/commit/fbf6ab9022a1f692c68b656ee7553b0469f2c8a7))
- fix(launch): runtime-agnostic GPU pinning via UUIDs — CDI/NixOS support (#610) ([510a76c](https://github.com/noonghunna/club-3090/commit/510a76c885cb83c55d47ea25e9ff6eba1b06efc2))
- fix(quality): precise benchlocal-cli source (sha/describe) — version is blind ([f6a344c](https://github.com/noonghunna/club-3090/commit/f6a344cf4f37ca2c499e91c423990e0323c6aa06))
- fix(c3): real GGUF quant for custom-named packs via quant_label ([d6416a5](https://github.com/noonghunna/club-3090/commit/d6416a55404162a87f3384cfc742d5c5a16332a6))
- fix(c3): derive Weights labels by pattern, not hand-map + ⑂ legend ([1dcba14](https://github.com/noonghunna/club-3090/commit/1dcba14ef6fc078e81393c4c6a181ff2dac646f7))
- fix(c3): width-stable status glyphs + reorder catalog columns ([e60a7ed](https://github.com/noonghunna/club-3090/commit/e60a7eddb845c1877b01533bed477568b61f0372))
- fix(launch): make the switch/launch table derivation stdlib-only (#584) ([b1562dd](https://github.com/noonghunna/club-3090/commit/b1562dd1c77bcbb76205f13202b67980dbd6bc94))
- fix(c3): surface submission-only slugs in the catalog TPS column (⑂-labelled) ([b0c5bc1](https://github.com/noonghunna/club-3090/commit/b0c5bc1d473786a57fe00efd6f94b6a04f108131))
- fix(launcher): read YAML as UTF-8 in registry-emit (switch broke on non-UTF-8 locales) ([0ecf839](https://github.com/noonghunna/club-3090/commit/0ecf839450b2df6364937d9ca2641d4b798d22a4))
- fix(c3): show submission-only baselines in the funnel card + 8pk on ⑂ lines ([c792e7d](https://github.com/noonghunna/club-3090/commit/c792e7ddc1fc02d604028edf47b7b20ad8b3e8fe))
- fix(#535): fail fast + actionable when gpu_memory_utilization doesn't fit free VRAM ([05f1076](https://github.com/noonghunna/club-3090/commit/05f10762659a723f84eae40f4df9e4b83c378b4a))


### 📝 Documentation

- docs(upstream): mark club-3090 #548 CLOSED (cache-untrack fix #572 shipped; upstream AOT-cache-key residual remains) ([59705e2](https://github.com/noonghunna/club-3090/commit/59705e2a9038f54b103f7fb3948c1cefb12c0277))
- docs(bench): fold #642 — internalcore2's virtualized 2×3090 Gen4 x8/x8 (Proxmox passthrough) dual row ([e8d04fc](https://github.com/noonghunna/club-3090/commit/e8d04fc4cbd4c648c92b5c17703e8fc059b96da8))
- docs(tools): dedicated repack_prefix.md — scope, usage, benefits (#700 follow-up) ([180f69c](https://github.com/noonghunna/club-3090/commit/180f69c91d769b4607df05ed237ae123f863cdff))
- docs(upstream): #178 lead — kevinb361 can't repro qwen3_coder corruption (froggeric template + v0.25.0 confounds) ([d2624ca](https://github.com/noonghunna/club-3090/commit/d2624cafa897c6affc2f9295af5badf8a8541c8a))
- docs(upstream): beellama — cameronr running v0.3.1-stable retest; preview tag 404s (digest-pin unaffected) ([40c8bd9](https://github.com/noonghunna/club-3090/commit/40c8bd9d83c5d44806f43ed9a39b1fe74d7dec30))
- docs(upstream): beellama row — launch-gate PR #696 + sm_89-natively-compiled correction ([148e94c](https://github.com/noonghunna/club-3090/commit/148e94cb82c5e5909ac8fb1e50750604129ba077))
- docs: record #693 — beellama/dflash DFlash broken on sm_89 (Ada); steer 4090 to ik-llama ([11bebde](https://github.com/noonghunna/club-3090/commit/11bebde5bec65393b3a4d9c2a8cbb3c39fa28a7a))
- docs: refresh expired Discord invite link (FAQ + README + issue template) ([5eff4eb](https://github.com/noonghunna/club-3090/commit/5eff4eb61bff9b9214f7ece05245a8e09dd9f897))
- docs: cross-link Cliff 3 ↔ LMCache — offload IS the mitigation, not a victim ([101077f](https://github.com/noonghunna/club-3090/commit/101077fdf215f837886f59fed9952903958ab8c5))
- AGENTS.md: log-file rule for long-running tests (no tail/grep pipes) ([2d7c1d0](https://github.com/noonghunna/club-3090/commit/2d7c1d06d74a869639012fdc834a3f4856ce99de))
- AGENTS.md: add 'Running a full eval — two non-overlapping passes' to Tests ([11c979d](https://github.com/noonghunna/club-3090/commit/11c979df9c892a8b2dbe5dc43ef14078cc8d99be))
- docs(pull): document MODEL_DIR storage convention (curated vs BYO tiers) ([3599fab](https://github.com/noonghunna/club-3090/commit/3599fab24d731df3445be0b66b126d080073ada8))
- docs(qwen): sync multi-max fp8 kv header ([23fc84f](https://github.com/noonghunna/club-3090/commit/23fc84f0795a465c25889d76a91a3ec91e6a65a7))
- docs: dedicated CLUSTERS.md — creating & managing multi-model clusters (#610) ([89fa15a](https://github.com/noonghunna/club-3090/commit/89fa15a3b704cd61704231032d4f1fd2912d2bd5))
- docs(nvfp4): correct the KV-scales story — declared, NOT shipped, both models ([efcf81c](https://github.com/noonghunna/club-3090/commit/efcf81c0c42029728138252f027f6e7431c4ad9b))
- docs(dual): de-stale the dual-max row — fp8/e4m3 KV + Production post-#594 ([2e05264](https://github.com/noonghunna/club-3090/commit/2e05264c4b3a3042d133717c8d87cacdaef941f2))
- docs(agents): fix stale guidance + add user-rig framing to AGENTS.md ([196d18a](https://github.com/noonghunna/club-3090/commit/196d18a213ba40c263a44b827c6ddafe248d4873))
- docs: note W8A8 INT8 is Ampere/Ada/Hopper-only (dead on Blackwell sm>=10.0) ([78798eb](https://github.com/noonghunna/club-3090/commit/78798eb6598584cf6953e28706cb7f0760ca9e2e))
- docs(compose): de-stale vLLM version in 5 qwen headers (v0.21/v0.22 -> v0.24) ([0f3ca1c](https://github.com/noonghunna/club-3090/commit/0f3ca1c4cb3aa0c8e8b1d43285b824981966c4b9))
- docs(multi-max): caveat — fp8 KV flip needs fresh 4-card re-validation ([ffbcb64](https://github.com/noonghunna/club-3090/commit/ffbcb64dcff86ef873506c6e10d88a0b2bf87bab))
- docs: fp8/e4m3 KV finding for dual-max (#594) — backend, scale, quality tie ([b56b7bd](https://github.com/noonghunna/club-3090/commit/b56b7bdce37a49d7c9f812ccfb18165960c258cd))
- docs(dual-max): accurate fp8/e4m3 KV header — scale=1.0, FlashInfer, quality tie, soak PASS ([605b8a6](https://github.com/noonghunna/club-3090/commit/605b8a6f9467d3fd86072c1ca9b812f8b0c54fb4))
- docs: cross-engine note — the consumer-vs-datacenter KV limit is vLLM-only ([6af5ccf](https://github.com/noonghunna/club-3090/commit/6af5ccfbf5fdd2b0ebf8db2bc56666d318ba4be6))
- docs: document the weights-vs-KV and consumer-vs-datacenter quant splits ([b0872f5](https://github.com/noonghunna/club-3090/commit/b0872f59898a6335dc48781cff5d45ca9de44c5b))


### 🔧 Pin bumps + upstream

- Add engine-pin-bump.sh — mechanical half of an engine image-pin bump (#681) ([#681](https://github.com/noonghunna/club-3090/pull/681) by @noonghunna)
- Bump llama.cpp pin to server-cuda-b9967 across all composes (+4 think-ON) (#680) ([#680](https://github.com/noonghunna/club-3090/pull/680) by @noonghunna)


### 🛠️ Scripts + tooling

- report.sh: capture motherboard + BIOS in the System section (#690) (#692) ([#692](https://github.com/noonghunna/club-3090/pull/692) by @noonghunna)
- preflight: warn on single-card GPU_MEMORY_UTILIZATION override above default (#641) ([#641](https://github.com/noonghunna/club-3090/pull/641) by @noonghunna)
- tools: add HTTP model-switch service (thin wrapper over switch.sh) ([c22a9d2](https://github.com/noonghunna/club-3090/commit/c22a9d2d84cfe13c14a6784387f7e59f59188de9))


### 🧹 Maintenance

- refactor(pods): rename cluster → pod (#610) + heterogeneous-rig guidance ([65eb109](https://github.com/noonghunna/club-3090/commit/65eb10981289d2d2403ff6fd1e5773a9baa92036))


### 🧹 Other

- Add repack_prefix.py — safetensors key-rename tool for AutoRound INT4 checkpoints (#700) ([#700](https://github.com/noonghunna/club-3090/pull/700) by @BlackBox-Labs)
- docs/nvlink: correct the NVLink decode uplift — it's a prefill lever, not a decode one (#698) (#702) ([#702](https://github.com/noonghunna/club-3090/pull/702) by @noonghunna)
- QUALITY_TEST: methodology — which probe for which comparison question ([c74d626](https://github.com/noonghunna/club-3090/commit/c74d626a45e279148f486b438c70354266c5a685))
- BENCHMARKS: de-blind single-nvfp4 ceiling on the #613 5090 row (@paulp83 #617) ([f86e063](https://github.com/noonghunna/club-3090/commit/f86e06393a83ec5cdbbf9a0aba0e42fba7a7e21e))
- De-blind single-nvfp4 ceiling: MTP-on ~98K on headless 5090 (#617 @paulp83) ([655bde1](https://github.com/noonghunna/club-3090/commit/655bde1b696c7df192e54fba5e5e9db0591794c5))
- Record Tess vLLM recipe arms: precision is the lever (FP8 111/117, nvfp4 recipe a wash) ([969382d](https://github.com/noonghunna/club-3090/commit/969382daa1a2be1e718bf58e629a2ce9186f1a28))
- QUALITY_TEST: pass@1 vs pass@N — the churn-harvest ceiling ([8244b21](https://github.com/noonghunna/club-3090/commit/8244b21920aa187c70fdf9d81dc8666212636d02))
- Re-tier tess4-model-floor per Sean's b9967 x3 data + the A0 amendment ([11af94a](https://github.com/noonghunna/club-3090/commit/11af94a1130cfba8484e16184642865bbcd56732))
- Record Tess vLLM A0 baseline: 106 off / 113 on — fallback triggered, slug stays 🧪 ([334b20c](https://github.com/noonghunna/club-3090/commit/334b20cf017160c5d31872ca55c324c434d10325))
- Promote Tess dual llama.cpp compose to Production (refresh: OFF 116 / ON 117) ([5621d9a](https://github.com/noonghunna/club-3090/commit/5621d9a12922b3497a0d85f5d43d62dac8733eb5))
- nvfp4 composes: document the unsloth (compressed-tensors) provider variant ([f19139f](https://github.com/noonghunna/club-3090/commit/f19139fbef61e0b725497a3d815da7167accfa3c))
- QUALITY_TEST: both-modes probe example + measured scenario-set runtimes ([be2ce99](https://github.com/noonghunna/club-3090/commit/be2ce99223cb98abf81bb7a6ecb3913635e30356))
- Wire benchlocal scenario selection + incremental/resume through the quality stack (#683) ([#683](https://github.com/noonghunna/club-3090/pull/683) by @noonghunna)
- BENCHMARKS: Tess dual b9967 re-bench + EAGLE3-vs-MTP external A/B (MTP wins) ([fed2ff7](https://github.com/noonghunna/club-3090/commit/fed2ff75e6cd9011da2b7bbfc64da433f94a37f0))
- Docs: pin policy trigger (2) — stability pins; fix stale llama.cpp/vLLM pin rows ([f9667e9](https://github.com/noonghunna/club-3090/commit/f9667e9e98f395d725bd80732c1dbeadffcd049b))
- Tess dual compose: date the streaming+thinking caveat as non-repro on b9967 ([c02c28e](https://github.com/noonghunna/club-3090/commit/c02c28e2d37556d2faa7b2e794b0d8c66c91d007))
- BENCHMARKS: add EAGLE3-GGUF draft provenance to the #674 single-4090 row ([6da2456](https://github.com/noonghunna/club-3090/commit/6da2456b4d9e2c179fe1ab4fedef4a40dd9ffbc2))
- BENCHMARKS: fix stale Tess intro pin (b9246 → b9967, missed by #680) ([f2345fc](https://github.com/noonghunna/club-3090/commit/f2345fc4f17cf990ee348fd235c24ad47629f76a))
- BENCHMARKS: add single-4090 Tess-4 + Eagle3 8-pack quality row (#674) ([#674](https://github.com/noonghunna/club-3090/pull/674) by @seanyourhighness)
- Add vllm/tess-dual-nvfp4: first vLLM Tess slug (fastest Tess on 2x24GB) (#679) ([#679](https://github.com/noonghunna/club-3090/pull/679) by @noonghunna)
- Add rerun-failed-packs.sh: re-test only failing packs + flake verdict (#678) ([#678](https://github.com/noonghunna/club-3090/pull/678) by @noonghunna)
- tess-dual-mtp: record first-party REASONING_BUDGET A/B result in header ([e8f5c3d](https://github.com/noonghunna/club-3090/commit/e8f5c3d689955c2714f482f29232e8ccec522b09))
- tess-dual-mtp: default REASONING_BUDGET=16384 (inert while thinking off) ([e3f6f02](https://github.com/noonghunna/club-3090/commit/e3f6f023566d3b00b13b86cd6923f8e157c8dced))
- c3: render caveats status as an orange checkmark instead of ❗ ([525f5a0](https://github.com/noonghunna/club-3090/commit/525f5a00cb40669b47e641e28102b2e1c7de24a6))
- Promote vllm/qwen-35b-a3b-dual-nvfp4-fast: experimental -> caveats (#676) ([#676](https://github.com/noonghunna/club-3090/pull/676) by @noonghunna)
- KV scales settled: unsloth checkpoint scales LOAD on the hybrid (and tie) ([86fb581](https://github.com/noonghunna/club-3090/commit/86fb58156906f4b4a5319f54536a0d7499a7f7c9))
- Add vllm/qwen-35b-a3b-dual-nvfp4-fast: Ampere-validated unsloth NVFP4 MoE slug (#675) ([#675](https://github.com/noonghunna/club-3090/pull/675) by @noonghunna)
- Add BENCHMARKS row: unsloth 27B NVFP4 provider A/B — tie with nvidia export ([f0c773e](https://github.com/noonghunna/club-3090/commit/f0c773e44760d5125e049b8221e2487c7af288a4))
- Docs pass: lightweight-path checklist + retire nightly/Genesis examples ([87627fd](https://github.com/noonghunna/club-3090/commit/87627fdf54cbbdd7e4f1e0256a57e039b04e6a30))
- Add BENCHMARKS row: unsloth 35B-A3B NVFP4-Fast ties AutoRound tier on 2x3090 ([280a4e8](https://github.com/noonghunna/club-3090/commit/280a4e847572e930fd7c691244c7888cc7ec76ad))
- Correct Tess-4-27B arch description: hybrid attention, not uniform GQA ([8b68541](https://github.com/noonghunna/club-3090/commit/8b68541af08e1780f3c2bbbaeaa7babab608cbe7))
- Add spec-sweep.sh: standardized draft-depth n-sweep for spec-decode drafters (#673) ([#673](https://github.com/noonghunna/club-3090/pull/673) by @noonghunna)
- PROVENANCE: record froggeric v21.3 rejection (hermes-timeout gate failure) ([fee2b40](https://github.com/noonghunna/club-3090/commit/fee2b40340596f94ae484a73d22762b5b14d903c))
- BENCHMARKS: NVFP4-on-Ampere row (Marlin W4A16 fallback, 2x3090) ([76dbc00](https://github.com/noonghunna/club-3090/commit/76dbc009a9fe6a301a95abc1930c778012123895))
- NVFP4: unhide on fallback-capable hardware (fallback_sm + hw_fallback badge) (#670) ([#670](https://github.com/noonghunna/club-3090/pull/670) by @noonghunna)
- concurrency-probe: report aggregate tok/s (verdict + RESULT + sweep) (#669) ([#669](https://github.com/noonghunna/club-3090/pull/669) by @noonghunna)
- bench-agentic: don't let a truncated tool call poison the ramp (#665) (#667) ([#667](https://github.com/noonghunna/club-3090/pull/667) by @noonghunna)
- Promote qwen-35b-a3b-single-nvfp4 → ⚠️ Production w/ caveats (#666) ([#666](https://github.com/noonghunna/club-3090/pull/666) by @noonghunna)
- announcement template: add §7 'Run the evals' section ([da063d7](https://github.com/noonghunna/club-3090/commit/da063d7714d527c1c2f4f541227f607b4a2e842c))
- rebench-full: replace fragile --help with a self-contained usage() (#664) ([#664](https://github.com/noonghunna/club-3090/pull/664) by @noonghunna)
- Record Tess-4-27B MTP n-sweep: n=2 is the sweet spot ([977d34f](https://github.com/noonghunna/club-3090/commit/977d34fe8d6f9d785b37930823e864378711a8a4))
- Add Tess-4-27B to the catalog (llama.cpp dual, external MTP, 262K) (#661) ([#661](https://github.com/noonghunna/club-3090/pull/661) by @noonghunna)
- deriver: resolve HF_HOME from MODEL_DIR so bare pull.sh lands on the model disk (#646) ([#646](https://github.com/noonghunna/club-3090/pull/646) by @noonghunna)
- deriver: include a dedicated MTP head in the weight download set (#645) ([#645](https://github.com/noonghunna/club-3090/pull/645) by @noonghunna)
- c3+pull: detect in-progress downloads + per-repo lock (#617) (#644) ([#644](https://github.com/noonghunna/club-3090/pull/644) by @noonghunna)
- c3: bring [D] download parity with the catalog path (#617) (#643) ([#643](https://github.com/noonghunna/club-3090/pull/643) by @noonghunna)
- Re-derate 27B nvfp4 single default: SPEC=on + 65K (keep MTP's 2x) ([f4cbd5a](https://github.com/noonghunna/club-3090/commit/f4cbd5a5a2f7147640a059a4675f2344e69e45f2))
- Detect MTP head in BYO Route-C swap instead of blanket spec-drop ([fdbd68b](https://github.com/noonghunna/club-3090/commit/fdbd68bc3a66401ae8d0016844b45028f5a7b0ae))
- Promote vllm/qwen-27b-multi-max to Production (v0.24.0 4-card gate) ([10f5b55](https://github.com/noonghunna/club-3090/commit/10f5b55adb250e4a6b2d13f7bb642fbda788b017))
- data(nvfp4): 35B-A3B 5090 baseline — corroborate #619 with #612 (120K NIAH) ([ef51f77](https://github.com/noonghunna/club-3090/commit/ef51f7778f5af4c4db9f7d88d45f7d8b5e840780))
- data(nvfp4): first NVFP4 validation — 35B-A3B single on RTX 5090 (#619) ([c3f32f8](https://github.com/noonghunna/club-3090/commit/c3f32f8fd642e1d880f6ca4b65354c8d7fb4d33e))
- data(baselines): ingest guybrush's full 8-pack on 2x5090 dual-max — 109/150, cross-arch parity ([55c468d](https://github.com/noonghunna/club-3090/commit/55c468d15c095c3115cd185fdff713bfb6edfc19))
- Record dual-max's 5090 fp8 quality (102/150, guybrush01 #571) ([7cb11cd](https://github.com/noonghunna/club-3090/commit/7cb11cda912761226c4b569c77ef4d7af3453d24))
- Record multi-fast's measured 4-card quality (108/150, @ryanmpelletier #584) ([cbe544a](https://github.com/noonghunna/club-3090/commit/cbe544a3c63ac8a57aa7210a69a8303e0b44cebb))
- Promote vllm/qwen-27b-multi-max to Production w/ caveats (@Whamp #446) ([796ceaf](https://github.com/noonghunna/club-3090/commit/796ceaf6af80397c0b962be42039bc9c8ab86fb7))
- Promote vllm/qwen-27b-dual-max to Production (soak completes the gate) ([7174ad9](https://github.com/noonghunna/club-3090/commit/7174ad91c46af4e0c3e60954ee4b536da088565e))
- DeepGEMM: cover fp8-dynamic weights too (agents-a1) — all fp8 slugs 5090-safe ([7e474f4](https://github.com/noonghunna/club-3090/commit/7e474f4c2b96a123f32328b06b409d15f0f71d8d))
- fp8 composes: add VLLM_USE_DEEP_GEMM pass-through parity + drift guard ([f3b55a0](https://github.com/noonghunna/club-3090/commit/f3b55a03afc70e6969e26c030c5d82c8468dfcdf))
- Promote vllm/qwen-27b-multi-fast to Production + induct 4x3090 baseline (#584) ([b8f2d2b](https://github.com/noonghunna/club-3090/commit/b8f2d2b927c5441d086e8f3787b453b86f94ecbd))
- dual-max: induct 2x3090 baseline row + correct the stale ~56 TPS probe ([fd56fe7](https://github.com/noonghunna/club-3090/commit/fd56fe7ad50c4f01e9e0f79d4a336d589a1362b3))
- ① Bring dogfood r2: clean labels · titled fields · selected-slug detail card ([235ab0b](https://github.com/noonghunna/club-3090/commit/235ab0bd68d1a56cc333242498ba471e678e0075))
- ① Bring: ONE starred recommendation — smallest fitting topology wins ([4eb238d](https://github.com/noonghunna/club-3090/commit/4eb238d778fc7789b702dc89580fbccc94ca54b9))
- deriver inventory: distinct gguf artifacts sharing a quant token stay separate ([81beaec](https://github.com/noonghunna/club-3090/commit/81beaec132b02e2532714944fb6e3a415e392f3d))
- ① Bring: staged artifact-first funnel (design §2b, F1-3) ([2da7d92](https://github.com/noonghunna/club-3090/commit/2da7d928e11d9306dc4a11274e82c5122c38a084))
- deriver: artifact inventory — bring-funnel stage-1 INSPECT (F1-1) ([a2f6165](https://github.com/noonghunna/club-3090/commit/a2f616521d015b29d71272eef66abf4844f01561))
- baselines: quality_env harness provenance on quality rows (friction #8) ([48238e4](https://github.com/noonghunna/club-3090/commit/48238e4cbbe85b2ef2e2ff8cc335a8de9136c23b))
- ④ Measure: sibling-class bar fallback for NEW models (T2 friction #9) ([213d803](https://github.com/noonghunna/club-3090/commit/213d803178c441189828c0637de5d3c4edb85740))
- catalog-baseline --from-bundle: ingest volunteer bundles (slice 3b) ([3970549](https://github.com/noonghunna/club-3090/commit/3970549ff7c7086f5cc32d49aa6e29bf1a47cb4b))
- Baselines slice 3a: cross-rig submissions schema (slug × rig-class) + tier ([3841582](https://github.com/noonghunna/club-3090/commit/3841582728bfb62946195694d2e7beeef45d6ef6))
- fp8w on Blackwell: auto-disable DeepGEMM + --force the arch-ab arm ([deb58a5](https://github.com/noonghunna/club-3090/commit/deb58a5f55acf538b60216bf42ccb9ae9756cf93))
- Phase 2: inject GPU_MEMORY_UTILIZATION floor for unified-memory cards ([47b43f9](https://github.com/noonghunna/club-3090/commit/47b43f9a3a3d98c2f8caeef8044f458603b252d2))
- Phase 2: validation-grade concurrency-probe (per-stream TPS, VALIDATE, SWEEP) ([4667330](https://github.com/noonghunna/club-3090/commit/4667330425042b30c02be4996418dd8bd1abeeca))
- Phase 2: PRO 6000 + DGX Spark envelopes, fix Blackwell detector ([e4b15fa](https://github.com/noonghunna/club-3090/commit/e4b15fa67b70bae73c3d6cc00d2e71b2574c4240))
- Phase 2: heterogeneous rigs clamp the envelope to the smallest-VRAM card ([19df532](https://github.com/noonghunna/club-3090/commit/19df532441d8092a126644db13f821d283a9b3f4))
- Phase 2: seed computed 5090 concurrency envelopes from kv-calc ([babf1aa](https://github.com/noonghunna/club-3090/commit/babf1aa69c1a60d2ad8ea186626c12dd50800e60))
- concurrency-probe: success = tokens generated, not non-empty content ([dcf10b6](https://github.com/noonghunna/club-3090/commit/dcf10b6cdcc89c2c054c63e1e870fcca19e061a5))
- Phase 2 (concurrency-only): memory-envelope MAX_NUM_SEQS injection + probe ([65c150d](https://github.com/noonghunna/club-3090/commit/65c150d562b446116a7c1072772b68e9898553f5))
- Gate nvfp4 KV to datacenter Blackwell only (sm_100/103) — found on #571 ([6f674fa](https://github.com/noonghunna/club-3090/commit/6f674fa2ce6a9b8e2a6eb342cd823cdbb60dac7d))
- p2p verdict: point WARN/INFO at docs/PCIE_P2P.md; doc catches up with the automated verdict ([b0c8933](https://github.com/noonghunna/club-3090/commit/b0c8933800ab4e951793d10164bee8db3ed3ae1b))
- Interconnect verdict: warn when P2P hardware sits idle (#488 matrix) ([218a0a9](https://github.com/noonghunna/club-3090/commit/218a0a9a92a809c0fde20cc4f8e0d1bfb3896266))
- Docs: PHB-arm anomaly corroborated board-specific (#488, chriskerley datapoint) ([e8a8e78](https://github.com/noonghunna/club-3090/commit/e8a8e7886e404fe56e30f2d4c868c397d70a8ddf))
- Docs: syangsao water-cooled byteshape cross-rig row (#445) ([afe56e3](https://github.com/noonghunna/club-3090/commit/afe56e35a5dc52c72e876e514b39899f321a8a50))
- Un-track A1's compiled torch cache — it crashed Blackwell boots ([717cb43](https://github.com/noonghunna/club-3090/commit/717cb431a91fe68084cbd0498d3fc3d60220c1c7))
- Docs: first Blackwell A1 row (#567) + sumo quality (#552) + sm_120 FP8 tracking ([6b7001a](https://github.com/noonghunna/club-3090/commit/6b7001aae61a2a1a7418fb1f9ffa13c76f213dcb))
- STRESS_FAST mode + honest dual-rig VRAM margins (dogfood findings) ([2790a7a](https://github.com/noonghunna/club-3090/commit/2790a7adcb73725ddc93a4e3fcf823431ac31b75))
- arch-ab: refuse the e4m3 arm below sm_8.9 (found dogfooding on sm_86) ([2477f53](https://github.com/noonghunna/club-3090/commit/2477f53e2f36838a8fe2e55c5509372d1217df3e))
- arch-ab: rig report gains the kv-calc calibration matrix ([47a9dac](https://github.com/noonghunna/club-3090/commit/47a9dacc1c7ec44d7b563069a4a26050b35aa8b0))
- arch-ab: include the redacted rig triage report in the bundle ([a98a246](https://github.com/noonghunna/club-3090/commit/a98a2468bfc1ebe67d141b09b847941cd7d02a59))
- Add arch-ab.sh: cross-rig KV-dtype A/B runner for #246 (lean tier) ([b569b62](https://github.com/noonghunna/club-3090/commit/b569b62d894d4909f4fc5319da20d038cdfd7846))
- Launcher arch-aware KV dtype injection for pilot slugs (#246 Phase 1) ([e8bcfd8](https://github.com/noonghunna/club-3090/commit/e8bcfd8da13bfa260577f243b1d165a81f1c9422))
- Re-gate beellama/gemma-dflash on the official pin; fix rebench-full n=3 ([5ea64bc](https://github.com/noonghunna/club-3090/commit/5ea64bc5393b724c0a33a7cb92b4bed9d3b605d5))
- Seed baselines wave-2: 5 rows + A1 decode-pair fix + gap dispositions ([a627efa](https://github.com/noonghunna/club-3090/commit/a627efa470ba1f23709c1b20a32c9479a6ae72ac))
- quality/baselines: rescore-materialization practice — artifacts carry the accepted truth ([d19d00b](https://github.com/noonghunna/club-3090/commit/d19d00b9d379f9d47e6f7c43e83c6e466f39fbce))
- catalog-baselines slice 2c: canonical two-depth prefill/TTFT probe + anchor calibration ([34b31c0](https://github.com/noonghunna/club-3090/commit/34b31c0aa4394c223139eeaa08a49410acc0c524))
- catalog-baselines slice 2b: c3 'yours vs the bar' overlay + bar provenance/staleness detail ([c6f56e0](https://github.com/noonghunna/club-3090/commit/c6f56e0c884629c1156f899a2482d830bb940a4d))
- catalog-baselines slice 2a: induction tool + rebench auto-record + completion prompt ([1d97445](https://github.com/noonghunna/club-3090/commit/1d974459c934b867c5c9dbc79dda3cdeb50962bc))
- catalog-baselines slice 1: baselines.yml + registry-emit join + guards; catalog drops the BENCHMARKS scrape ([75b2955](https://github.com/noonghunna/club-3090/commit/75b29556c18ef62cf624244e57c1eee19130c3e6))
- beellama docs: sm_120 root cause + Anbeeld#85 ask + verified self-build recipe ([c2c06e4](https://github.com/noonghunna/club-3090/commit/c2c06e47a7610b6cbcf295298ef54273d929a852))
- BENCHMARKS: Agents-A1 cross-rig row — @sumo-dandan #552 (x4 OCuLink eGPU, 250W) ([1c0ea8f](https://github.com/noonghunna/club-3090/commit/1c0ea8fcb6635e455c268ebfac920bd3bab56cb9))
- agents-a1: hardware-metadata header + Blackwell caveat (#548 follow-up) ([ff96f89](https://github.com/noonghunna/club-3090/commit/ff96f895066862fa0e1a547148cb21ac8d094f9e))
- c3/gpu-mode: preview-clip fix + scene-boundary hardening (F2+F5, T1-lite tail) ([b00b5a0](https://github.com/noonghunna/club-3090/commit/b00b5a0955edfd0372bfb1b878fa8e03423d540f))
- c3/tui-core: [Y]-copy the visible live-log tail + pane-specific placeholders (F4+F8) ([da11b4c](https://github.com/noonghunna/club-3090/commit/da11b4cf5671cd51001c447e1ef4920fbfc8d765))
- estate_cli: probe per-instance liveness so a leftover plan can't fake conflicts (F7) ([a939fb1](https://github.com/noonghunna/club-3090/commit/a939fb1831d34372a535b59fb277cd93ea33af28))
- c3: keep the catalog's money columns on-screen at 120-140 cols (F6) ([f163dca](https://github.com/noonghunna/club-3090/commit/f163dca673a9603bf9fd5d2c9191f1def8543709))
- c3: Evidence pane doubles as the live gate-run observer (F10 MVP) ([a6ff86f](https://github.com/noonghunna/club-3090/commit/a6ff86febac4484f8e7e268ed8741a6f9aea8df9))
- c3/detect: grade slug matches so shape guesses never masquerade as identity (F9) ([4390340](https://github.com/noonghunna/club-3090/commit/43903400408247551d0baa9e55abef95ab455434))
- c3+switch: show/copy the serving API URL; fast-flip booting→ready (F3/F3b) ([d3836ec](https://github.com/noonghunna/club-3090/commit/d3836ecd8728225684dc8f6226a772ff040c5ebc))
- Promote Agents-A1 to the catalog: vllm/agents-a1-dual (production w/ caveats) ([6926dfd](https://github.com/noonghunna/club-3090/commit/6926dfde48cf0ade07d041af0473cda99b0c22e1))
- deriver: resolve bit-width from compressed-tensors config_groups ([15a4e75](https://github.com/noonghunna/club-3090/commit/15a4e75180c56f174ac1399d35382a89b4016a20))



[Pin: `git checkout v0.10.2`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.10.1...v0.10.2)
## v0.10.1 — 2026-07-02


### ✨ Features

- feat(gemma): v0.24.0 overlay-free 31b dual (cyankiwi, MTP-off) ([2535bb9](https://github.com/noonghunna/club-3090/commit/2535bb9a3d0194f48e1369f0970ed22c1d29daf5))


### 🐛 Bug fixes

- fix(studio): derive + pin COMFYUI_OUTPUT_DIR from COMFYUI_ROOT (#510 render-mount) (#534) ([#534](https://github.com/noonghunna/club-3090/pull/534) by @noonghunna)
- fix(studio): pin COMFYUI_ROOT to .env so ComfyUI mounts the models tree (#510, #530) (#531) ([#531](https://github.com/noonghunna/club-3090/pull/531) by @noonghunna)
- fix(studio): pull HiDream + Chroma weights in the ai-studio roster (#510) (#529) ([#529](https://github.com/noonghunna/club-3090/pull/529) by @noonghunna)
- fix(quality-test): preflight sandbox images + document the build step (#492) (#494) ([#494](https://github.com/noonghunna/club-3090/pull/494) by @noonghunna)
- fix(ai-studio): derive ComfyUI paths from MODEL_DIR + make gpu-mode portable (#493) ([#493](https://github.com/noonghunna/club-3090/pull/493) by @noonghunna)


### 📝 Documentation

- docs(quant): add QUANTIZATION §4b tier trade-space ([8d4a6ec](https://github.com/noonghunna/club-3090/commit/8d4a6ecc11953d693c82375f6b46c44a2ec7c676))
- docs(gemma-31b): reflect the v0.24.0 bf16 consolidation ([f7214fb](https://github.com/noonghunna/club-3090/commit/f7214fb4d354445942d8ca79a9cd697f01543865))
- docs(ai-studio): add design rationale + 3 complements from the production-agent design ([81181fc](https://github.com/noonghunna/club-3090/commit/81181fc4fa513706fedab0b3974bf1288dae7780))
- docs(ai-studio): explain storyboard continuity + add a troubleshooting section ([f28dde4](https://github.com/noonghunna/club-3090/commit/f28dde4167f821a2cfca0125387c9a90a709b4e4))
- docs(ai-studio): rewrite director flow as behavioral + add Character Bible / continuity / research ([01cb15b](https://github.com/noonghunna/club-3090/commit/01cb15b17e9766659f0c56d72ccc3be12f1dd7bd))
- docs(ai-studio): flag Production Director as WIP / not production-ready ([b494b50](https://github.com/noonghunna/club-3090/commit/b494b509c3ee4fac7b2517db1fb6cae3f50dc7f1))
- docs(ai-studio): add "Current challenges / known limitations" to agents doc ([a517324](https://github.com/noonghunna/club-3090/commit/a517324a261f01bbbac0817bba5757cf94c34f58))
- docs(ai-studio): add agents-architecture.md (director decision flow) ([38487e5](https://github.com/noonghunna/club-3090/commit/38487e5c410990b777af96a8d258604e613fb421))
- docs: correct --no-thinking help — four packs default thinking-on ([fa66758](https://github.com/noonghunna/club-3090/commit/fa66758b94120d4592072ef9ef38ce53b7015375))
- Document LMCache RAM gate formula (L1 + 28) in compose caveat ([c4bd455](https://github.com/noonghunna/club-3090/commit/c4bd45581c95c40b916f5299c551975ed423b098))


### 🔧 Pin bumps + upstream

- Bump vllm-stable v0.22.0 → v0.24.0 (overlay-free; marlin-pad native) (#533) ([#533](https://github.com/noonghunna/club-3090/pull/533) by @noonghunna)


### 🛠️ Scripts + tooling

- setup-ai-studio.sh: make the "sign up then install the pipe" step unmissable (#510) (#527) ([#527](https://github.com/noonghunna/club-3090/pull/527) by @noonghunna)
- report.sh: add --studio flag (AI Studio / ComfyUI container log tails) (#526) ([#526](https://github.com/noonghunna/club-3090/pull/526) by @noonghunna)


### 🧹 Other

- serve: neutral primary model name (qwen3.6-27b / gemma-4-31b), keep -autoround alias ([7e9f5cb](https://github.com/noonghunna/club-3090/commit/7e9f5cb9302b117f8abbf7c135b9654aa992ba86))
- patches: de-register vllm-marlin-pad (merged upstream, native in v0.24.0) ([ae4d1fc](https://github.com/noonghunna/club-3090/commit/ae4d1fcad6621a8b61a30e8e2e4bb970e6ba35f6))
- c3: hide deprecated slugs in catalog by default ([h] toggles) ([8b43b48](https://github.com/noonghunna/club-3090/commit/8b43b485f9b3b53da81871b15efb15e265dfe7c4))
- hygiene(qwen composes): align stale Engine-profile headers vllm-nightly-clean -> vllm-stable ([126e5c5](https://github.com/noonghunna/club-3090/commit/126e5c5afbbe47c8d6f141745cb1d20f68f47a6a))
- bump(diffusiongemma): :gemma branch digest -> stock vLLM v0.24.0 ([68c6ea8](https://github.com/noonghunna/club-3090/commit/68c6ea80fb102730c28c7bcfdafe27e2e269e63b))
- consolidate(gemma-31b): single bf16 dual slug on v0.24.0, retire v0.22.0 composes ([6cfcbc6](https://github.com/noonghunna/club-3090/commit/6cfcbc6bc07dfbca06b1b77ca97e7bb5058316cf))
- fold(gemma-12b): dual-bf16 onto vllm-stable v0.24.0, MTP-off ([dea4579](https://github.com/noonghunna/club-3090/commit/dea457968ee1662ed0519837d6d3969ca6093cc6))
- fold(gemma-26b): MTP-off on v0.24.0 dual (Gemma-4 MTP×tools broken) ([93b1642](https://github.com/noonghunna/club-3090/commit/93b1642ada4a17c1e9c3eb5106ec52aeaf31803c))
- BENCHMARKS: W8A8 row is an experimental data point, not a shipped slug ([852b561](https://github.com/noonghunna/club-3090/commit/852b5610119fbe9dc5a6d8ad85f345a93c47b1d1))
- BENCHMARKS: add v0.24.0 dual-max FP8 + W8A8 rows (8-bit decode vs prefill corners) ([1f4028e](https://github.com/noonghunna/club-3090/commit/1f4028eaffd73914f273eafc898291ea1b1b35b7))
- studio(tts): chmod 0644 the TTS + narrate outputs so the host can read them (#501) ([#501](https://github.com/noonghunna/club-3090/pull/501) by @noonghunna)
- Fix #512: portable LAN-IP detection + persist to .env (CachyOS / GNU inetutils) (#525) ([#525](https://github.com/noonghunna/club-3090/pull/525) by @noonghunna)
- Director: make the LLM the intent driver, demote keyword detection to a bare fallback (#524) ([#524](https://github.com/noonghunna/club-3090/pull/524) by @noonghunna)
- Director: web research for documentaries (SearXNG-grounded facts) + honesty fix (#523) ([#523](https://github.com/noonghunna/club-3090/pull/523) by @noonghunna)
- Director Batch 3: semantic plan critic before render (Codex F5/F6/F7) (#522) ([#522](https://github.com/noonghunna/club-3090/pull/522) by @noonghunna)
- Director Batch 2: structured LLM intent controller (natural multi-turn conversation) (#521) ([#521](https://github.com/noonghunna/club-3090/pull/521) by @noonghunna)
- Director Batch 1: creation-question gate, pinned-lane capabilities, sizing + valve fixes (#520) ([#520](https://github.com/noonghunna/club-3090/pull/520) by @noonghunna)
- Planner: detect documentary vs narrative format, suppress invented protagonist (#519) ([#519](https://github.com/noonghunna/club-3090/pull/519) by @noonghunna)
- Production assemble: fix sub-frame cut xfade collapsing multi-shot films (#514) ([#514](https://github.com/noonghunna/club-3090/pull/514) by @noonghunna)
- Production planner: scale director token budget by shot count (#513) ([#513](https://github.com/noonghunna/club-3090/pull/513) by @noonghunna)
- Production: wire LTX-2.3 / Sulphur / 10Eros video lanes into the executor (#511) ([#511](https://github.com/noonghunna/club-3090/pull/511) by @noonghunna)
- Production lane: conversational director + persona in AGENTS.md (#509) ([#509](https://github.com/noonghunna/club-3090/pull/509) by @noonghunna)
- Production lane: qualify (size + propose) → confirm → build (#508) ([#508](https://github.com/noonghunna/club-3090/pull/508) by @noonghunna)
- Fix: Production lane chit-chat gate — don't render a film from 'hello' (#507) ([#507](https://github.com/noonghunna/club-3090/pull/507) by @noonghunna)
- Studio setup: zero-config defaults — portable MODEL_DIR + fail-fast + shared LAN-IP (#506) ([#506](https://github.com/noonghunna/club-3090/pull/506) by @noonghunna)
- Studio setup: de-rig standalone scripts — fix #503 model path + #504 LAN IP (#505) ([#505](https://github.com/noonghunna/club-3090/pull/505) by @noonghunna)
- Studio Production: stack + OWUI lane + keyframe tiers + Character Bible (Tier A) (#502) ([#502](https://github.com/noonghunna/club-3090/pull/502) by @noonghunna)
- Studio Production Agent v0b-core + v0b-images (#497, #499) ([6ee5e32](https://github.com/noonghunna/club-3090/commit/6ee5e32baeb8e5ea4ff328b929150794e3293c8e))
- Studio Production Agent v0a — executor spike (offline + live PASS) (#496) ([#496](https://github.com/noonghunna/club-3090/pull/496) by @noonghunna)
- BENCHMARKS: fold @guybrush01 dual-5090 8-pack quality onto cross-rig row ([2886de4](https://github.com/noonghunna/club-3090/commit/2886de4687285b7634c23b8bb9619993e82cdf77))
- Add model-scope dropdown + group-by-model to c3 Catalog (#495) ([#495](https://github.com/noonghunna/club-3090/pull/495) by @noonghunna)



[Pin: `git checkout v0.10.1`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.10.0...v0.10.1)
## v0.10.0 — 2026-06-26


### ⚠️ Cliffs, gotchas, regressions

- c3 Phase R / R3b-1 fixups: temp unlink-on-decline + lane-native [v] regression test ([4ec2b2b](https://github.com/noonghunna/club-3090/commit/4ec2b2b6341fe85ae1eff652692a9ac49f4039b6))


### ✨ Features

- feat(lmcache): add NVLink auto-detection to dual-lmcache compose ([ea833ad](https://github.com/noonghunna/club-3090/commit/ea833ad134c98ef38152fd30ff93e0cc024bcd71))
- feat(vibethinker-3b): add llamacpp/vibethinker-3b-single (Q8, incubating) ([d3cacfa](https://github.com/noonghunna/club-3090/commit/d3cacfad0c1155066c09893b6ab2939ecb4ba6e2))
- feat(catalog): add 🐣 Incubating status tier + VibeThinker-3B (incubating) ([35a6965](https://github.com/noonghunna/club-3090/commit/35a69650fed92376d8f3d2bca920fdd034f2448d))
- feat(qwen3.6-27b): add beellama/carnice-v2-dual-q8-mtp dual compose (#403) ([186ab9b](https://github.com/noonghunna/club-3090/commit/186ab9b2b6155936ef3d7ee365f00cae253710d6))


### 🎯 New models + serving paths

- Add gemma12b single-card gpu-mode scene + litellm route (#469) ([#469](https://github.com/noonghunna/club-3090/pull/469) by @noonghunna)
- Add guard test: conditional compose entrypoints must $$-escape runtime bash ([1b87ebe](https://github.com/noonghunna/club-3090/commit/1b87ebe05e760fdb6c027341ec7210ef827c209b))
- Add llamacpp/qwen27b-pi-reasoning-single (Qwen3.6-27B Pi-style coding agent, mainline llama.cpp + MTP) (#425) ([#425](https://github.com/noonghunna/club-3090/pull/425) by @noonghunna)
- Add opt-in LMCache KV-offload compose (vllm/qwen-27b-dual-lmcache, incubating) (#421) ([#421](https://github.com/noonghunna/club-3090/pull/421) by @noonghunna)


### 🐛 Bug fixes

- fix(lmcache): forward env tuning knobs ([c90e4f2](https://github.com/noonghunna/club-3090/commit/c90e4f2e18ddd455576080ff6ebba8a195a4b6ad))
- fix(nvlink): strip only expandable_segments on custom-AR path ([f5d5dca](https://github.com/noonghunna/club-3090/commit/f5d5dca09a4b907b9c5aafb611c1bb090af11bc3))


### 📝 Documentation

- docs: add PCIE_P2P.md — PCIe topology & enabling P2P (no NVLink) ([df419c9](https://github.com/noonghunna/club-3090/commit/df419c9bd7f4d518ed8ef4fc9199863c50201dfd))
- README: add a getting-started subsection for the c3 TUI ([069ac27](https://github.com/noonghunna/club-3090/commit/069ac27256b0e1f5027a071d139add8536139d1e))
- docs(lmcache): fold cross-rig findings — warm-L2 compute-bound + aborted-prefill caveat ([7b0c4d4](https://github.com/noonghunna/club-3090/commit/7b0c4d4abc12eda7e7db28fa63fc520856b4bdf2))
- docs(c3): first-run Settings step (Model Dir + HF token) + S keybinding ([50bed70](https://github.com/noonghunna/club-3090/commit/50bed7047633df08ea29b5ddc5ca4e061e95bfad))
- docs(ai-studio): Krea 2 is a real image lane (was "dropped") ([7daef3e](https://github.com/noonghunna/club-3090/commit/7daef3ec1ec5d07777416f379da9e762d0aa0175))
- docs: note the image-lane quality ceiling + optional HQ upgrade path ([852820d](https://github.com/noonghunna/club-3090/commit/852820d2c3631e5053c4b45a22a12da81eec723e))
- docs: AI Studio requirements + Wan tuning + director placement ([11984d1](https://github.com/noonghunna/club-3090/commit/11984d19dac66d0222d0aa66f4bdbf462808fff7))
- docs: Z-Image + Wan2.2 lanes (11 lanes); Krea2 dropped (cloud-only) ([5c2ed40](https://github.com/noonghunna/club-3090/commit/5c2ed400d25b40f7ee653e06594c7b606dddf1ef))
- docs: ai-studio consolidation pass (one scene, lanes inside it) ([813ddf9](https://github.com/noonghunna/club-3090/commit/813ddf94d8a22648fee9ccc8cd7cf56a4de25ac4))
- docs(upstream): add ParserEngine tracker rows (#45413, #45588) ([0596283](https://github.com/noonghunna/club-3090/commit/05962838cfeb37436875c43eebb84bb65abd82c4))
- docs(upstream): clarify #40812 is merged-but-insufficient; point at #43923 ([611587d](https://github.com/noonghunna/club-3090/commit/611587dff3912095097af01d5d5a91ca5bcf3b8f))
- docs: mark transformers>=5.8.0 / gemma4_assistant upstream row resolved (#453) ([#453](https://github.com/noonghunna/club-3090/pull/453) by @steamEngineer)
- docs: fix vLLM upstream table render (drop stray blank line) (#452) ([#452](https://github.com/noonghunna/club-3090/pull/452) by @steamEngineer)
- docs(vibethinker-3b): add measured one-shot-coding scores (HE+ 97%, LCB 83%) ([8b3aa13](https://github.com/noonghunna/club-3090/commit/8b3aa13f54b1780b60f1d053512b65735b9efaa8))
- docs: add ANNOUNCEMENT_TEMPLATE.md (Announcements-post skeleton) ([a728832](https://github.com/noonghunna/club-3090/commit/a728832f606631ef0c8e9c17a13cbf77d12c411b))


### 🛠️ Scripts + tooling

- report.sh: surface P2P engagement as a labeled field (#491) ([#491](https://github.com/noonghunna/club-3090/pull/491) by @noonghunna)
- setup.sh: let WEIGHT_KEY bypass the friendly model-name dispatch ([f9d8f8d](https://github.com/noonghunna/club-3090/commit/f9d8f8d485d1e94686b4a4f7dd6a9b2ffc97d1ca))
- weights.py: add `list --json` (download-state source for c3) ([1730e04](https://github.com/noonghunna/club-3090/commit/1730e0405b96da3aa09ac317b5c4db56f5ea997c))


### 🧹 Other

- BENCHMARKS: add @oven1231231234 dual-3090 NVLink-vs-PHB A/B (PCIe 3.0 x16) ([4032645](https://github.com/noonghunna/club-3090/commit/4032645ee45c31e9a37b3164e7ae208294903bf8))
- Standardize 27b served-model-name → qwen3.6-27b-autoround (#490) ([#490](https://github.com/noonghunna/club-3090/pull/490) by @noonghunna)
- gpu-mode: align power-cap default 230W -> 250W (completes #483) (#489) ([#489](https://github.com/noonghunna/club-3090/pull/489) by @noonghunna)
- Add nvidia-power-cap.service for boot-time GPU power cap (#483) (#485) ([#485](https://github.com/noonghunna/club-3090/pull/485) by @alexpolo1)
- BENCHMARKS: add Ornith-1.0 section (9B + 35B rows) ([c9f651e](https://github.com/noonghunna/club-3090/commit/c9f651ecffe0af72e91fb1e11722df2bd1d052fe))
- Add Ornith-1.0-35B experimental slug (ik-llama/ornith35b-dual) (#479) ([#479](https://github.com/noonghunna/club-3090/pull/479) by @noonghunna)
- BENCHMARKS: add @Whamp 4× 3090 TP=4 multi4 rows (#446) ([291fa74](https://github.com/noonghunna/club-3090/commit/291fa740ffce58a450795ca57ffadcadaa76363c))
- BENCHMARKS: add @guybrush01 dual-5090 cross-rig row (Qwen3.6-27B, first Blackwell) ([2c686e9](https://github.com/noonghunna/club-3090/commit/2c686e96b6484f05f913eca6b2cb5ca61fb92395))
- Add Ornith-1.0-9B experimental slug (ik-llama/ornith9b-single) (#477) ([#477](https://github.com/noonghunna/club-3090/pull/477) by @noonghunna)
- c3: adaptive estate poll — fast GPU, regime-gated docker (burst/steady/idle) (#476) ([#476](https://github.com/noonghunna/club-3090/pull/476) by @noonghunna)
- Director placement lever: CPU / GPU0 / GPU1 (c3 Settings) (#473) ([#473](https://github.com/noonghunna/club-3090/pull/473) by @noonghunna)
- Wire SearXNG web search + Qdrant vector DB into Open WebUI (#472) ([#472](https://github.com/noonghunna/club-3090/pull/472) by @noonghunna)
- Lazy-load step-voice + scene-wire it into ai-studio (#471) ([#471](https://github.com/noonghunna/club-3090/pull/471) by @noonghunna)
- Make the OWUI model picker scene-accurate (studio lanes + LLMs) (#470) ([#470](https://github.com/noonghunna/club-3090/pull/470) by @noonghunna)
- gpu-mode: rename model scenes to qwen27b / qwen35b-a3b / gemma-31b ([33a1f71](https://github.com/noonghunna/club-3090/commit/33a1f71c8198b54cfe22af8504893085cc005526))
- gpu-mode: add the 35b-a3b scene (parity with 27b/gemma/deckard) ([9f1f3a9](https://github.com/noonghunna/club-3090/commit/9f1f3a9e37a2b1a907f73b596573b8668293593a))
- gpu-mode: fix `gpu-mode gemma` (undefined fn aborted before start) + litellm port ([2b17aa5](https://github.com/noonghunna/club-3090/commit/2b17aa5070d4040a4a2aa8d86fb543d9d3fed33a))
- c3: distinguish "booting" from "API not reachable" in Doctor (all engines) ([1ce5a5f](https://github.com/noonghunna/club-3090/commit/1ce5a5f717f303ec9b73f0d5ad958085fbe8e64c))
- owui: wire LiteLLM gateway (:4000) as a chat connection ([f5ec5c3](https://github.com/noonghunna/club-3090/commit/f5ec5c3201ebad2e6e6575df3ce91dec903a6144))
- c3: scene-preview box auto-grows to fit all services (not a cap) ([9459536](https://github.com/noonghunna/club-3090/commit/94595368d215983df4a3bfe88a785292a85c7458))
- c3: cap scene-preview services with "+N more" (ai-studio truncation) ([9299e6f](https://github.com/noonghunna/club-3090/commit/9299e6fc1447a8ea36fee357e697049642c0739c))
- serve-cockpit: declare PyYAML dependency (fixes c3 diagnose-estate crash) ([0cc9d9c](https://github.com/noonghunna/club-3090/commit/0cc9d9c5c4cbf64c5ca098c695178d2bd715149e))
- ai-studio: wire the Krea 2 Turbo image lane (validated on v0.26.0) ([978052a](https://github.com/noonghunna/club-3090/commit/978052abfc6768647d52a5588f23eba7054d8113))
- comfyui entrypoint: fix dubious-ownership blocking the pin checkout ([e738c7c](https://github.com/noonghunna/club-3090/commit/e738c7c59b24e0031132e712fd9c6c322436447a))
- Bump ComfyUI pin to v0.26.0 + queue Krea 2 download ([2693d93](https://github.com/noonghunna/club-3090/commit/2693d937f8bbf1d26ccca654d6ff93d188383ff5))
- detect_nvlink: auto-enable PCIe P2P when nvidia-smi reports it OK ([446c7d9](https://github.com/noonghunna/club-3090/commit/446c7d97428f80587a1e70cf887d7cc5f785c676))
- studio: one-command setup-ai-studio.sh + auto-install the OWUI pipe ([aad1e69](https://github.com/noonghunna/club-3090/commit/aad1e69d0989dccf1381394b57588acac9675880))
- c3: make fresh-clone install work + rewrite stale README + repo pointer ([37c680d](https://github.com/noonghunna/club-3090/commit/37c680d5d28f68eed6d4f7bcee7ac0a5fd9b7c80))
- studio: Wan2.2 full parity — recipe fix, 720p valve, i2v, long-clip chaining ([0ff83b8](https://github.com/noonghunna/club-3090/commit/0ff83b8fae0cda90ccebf745d8531ac462f86644))
- studio: download scripts + manifest rows for Z-Image + Wan2.2 ([5fb8fa1](https://github.com/noonghunna/club-3090/commit/5fb8fa1c7f0930c97da411af21b6fea2ea24d439))
- studio: add Z-Image + Wan2.2 uncensored lanes; unify OWUI lane naming ([9b16ef9](https://github.com/noonghunna/club-3090/commit/9b16ef919c6efac4eeaa01060897307c6df36bf3))
- cockpit: ai-studio missing-models modal + video⊕voice GPU guard ([75dbc0a](https://github.com/noonghunna/club-3090/commit/75dbc0a8f52ae6861f863eee93bae0d1287ee2c2))
- studio: add the 10Eros uncensored video lane (A/B vs Sulphur) ([a4230b3](https://github.com/noonghunna/club-3090/commit/a4230b3861746d9a40e72331121b16b610e7049d))
- studio: consolidate image/video into one `ai-studio` gpu-mode scene ([3fc2685](https://github.com/noonghunna/club-3090/commit/3fc26857f200d692effd189fd2c490a48ef275e2))
- cockpit: give report/full-report/cap-sweep their own Doctor cards ([ef8cba8](https://github.com/noonghunna/club-3090/commit/ef8cba83b12ba0322eceb9f4ca5f76793878b26a))
- studio: preflight the models before starting (gpu-mode + cockpit) ([757c1da](https://github.com/noonghunna/club-3090/commit/757c1daba3b4c8223cc9b4687b4637ed5cab1804))
- studio: fetch the director / Kokoro / Step-Audio models for a fresh install ([cece4ec](https://github.com/noonghunna/club-3090/commit/cece4ec4fbb22d3c4e960677ff515f2c50ed3114))
- cockpit/gpu-mode: comfyui engine label, drop power-cap strip + solo scene, list studio sidecars ([cae021d](https://github.com/noonghunna/club-3090/commit/cae021d6ead9e38c59376b95d3ec8cf4a6cee6c5))
- cockpit: show engine + port for comfyui/qdrant (port-range + non-engine ports) ([ee954e1](https://github.com/noonghunna/club-3090/commit/ee954e140495688737517b7cd50558267a6476c4))
- cockpit: guide studio setup when comfyui-local image is missing ([016bf36](https://github.com/noonghunna/club-3090/commit/016bf36fd50982bfc6bd63cc06f950e011dd7016))
- comfyui: parameterize host paths for portability (${COMFYUI_ROOT} / ${MODEL_DIR}) ([ac31c7e](https://github.com/noonghunna/club-3090/commit/ac31c7e91f08489c56ed112052459a9a91c125f7))
- cockpit: fix per-service stop/start to target the real container + project ([c52ab09](https://github.com/noonghunna/club-3090/commit/c52ab09b4885d51f48519ce6d9e696e7da26ccae))
- stack: remove retired ollama service entirely ([9b73a4c](https://github.com/noonghunna/club-3090/commit/9b73a4ccfd652c2bab2330ca83b62b9c39f717aa))
- cockpit: Containers shows service status/engine/port + start; de-dup Orchestration ([727d90b](https://github.com/noonghunna/club-3090/commit/727d90b06fc0896cdcebca55aa02b4a0541d4cb2))
- cockpit: live status bullets on Orchestration services (read-only) ([1b4e2af](https://github.com/noonghunna/club-3090/commit/1b4e2af4bcf1de7467742e96a6886d26ed2a2148))
- cockpit: cluster Orchestration scenes by group (models → studio → ops) ([0b58a48](https://github.com/noonghunna/club-3090/commit/0b58a48e93abecb7fe53b5e2aa19d0ce9bdbfbb3))
- gpu-mode: collapse the gemma scenes to just 'gemma' ([7bca67c](https://github.com/noonghunna/club-3090/commit/7bca67cbde6fb5c8b2b4d6f43837e852bce43d31))
- gpu-mode scenes: regroup (serving→models), drop bigmodel + diffusiongemma ([5fb2252](https://github.com/noonghunna/club-3090/commit/5fb22527c2e8cd38ee6f3df2b8c9f466a2734c9a))
- c3 Orchestration scenes: footer-only confirm, clearer override, real 'off' ([0896bd9](https://github.com/noonghunna/club-3090/commit/0896bd9721373ea5db9e67e81de155b682bad082))
- c3 Orchestration: power-cap menu, remove prune, move cap-sweep to Doctor ([38227ce](https://github.com/noonghunna/club-3090/commit/38227cea93d158acbbb0ddc2ea0af5416440ff0f))
- c3: unify MODEL_DIR convention between the cockpit and setup.sh ([f03b514](https://github.com/noonghunna/club-3090/commit/f03b5146646d5c8018905fde5087dfdbdcd5a451))
- c3 Download: ignore backup cruft (*.bak/*.old/~) in the progress byte-count ([acacfda](https://github.com/noonghunna/club-3090/commit/acacfdaaf1fbfb7e53d3a1cab6105461c92efe12))
- c3 Download: live progress moves + state survives a catalog refresh ([32fadef](https://github.com/noonghunna/club-3090/commit/32fadef1925e078be3c34a28234ae36a1176875a))
- c3 Download: registry-driven companion artifacts (DFlash draft / mmproj) ([639525b](https://github.com/noonghunna/club-3090/commit/639525bd85ade48efbf1e7390e84de6c046db3d4))
- c3 Settings: show [S] in the footer + honor MODEL_DIR / HF_TOKEN env vars ([2aae1d0](https://github.com/noonghunna/club-3090/commit/2aae1d0fcce9068dcfdf84906a6bcba8422c72b0))
- c3 Download UX: [S] Settings (model dir + HF token) + not-set banner ([340896c](https://github.com/noonghunna/club-3090/commit/340896c574a4e89d3a03d4d024c1262a7a895357))
- c3 Download UX: Download-vs-Start pop-up, listing glyph, download worker ([8947d59](https://github.com/noonghunna/club-3090/commit/8947d597df5f638b1309de3a88e6cea13e3d3982))
- profiles: wire hf_repo for 5 verified weight variants ([eb81c5f](https://github.com/noonghunna/club-3090/commit/eb81c5f0af750f176b4da313442081e1301991a7))
- c3 Download UX (service): download plan + progress + disk-fit ([a28d3d1](https://github.com/noonghunna/club-3090/commit/a28d3d13b09890f5f393768da4d42aafddb95f49))
- c3 Download UX (data layer): per-slug weights-on-disk state ([e8d99a5](https://github.com/noonghunna/club-3090/commit/e8d99a553c99e9e774db688ef85b4c88e4084c63))
- c3: fix slug-match prefix shadow, idle-service reconcile, hint overflow, copy, experimental Force-Start ([53a570f](https://github.com/noonghunna/club-3090/commit/53a570f3059bedc48932e0b886620d117440462d))
- c3: [Y] copy-to-clipboard + shift+arrow horizontal scroll ([d256a05](https://github.com/noonghunna/club-3090/commit/d256a058e92da1dbb6a021f98a4e229e5c2bfd07))
- c3 Doctor: "is it serving correctly?" — verify / verify-full reads ([d05f132](https://github.com/noonghunna/club-3090/commit/d05f132b0a879b1139203870b4ddc733f494b667))
- c3 serve pop-up: state-aware Stop/Start/warned-Start; drop Fit column ([8ad9a00](https://github.com/noonghunna/club-3090/commit/8ad9a00d21a86022a65905f914a466c85b71a03b))
- c3 Catalog: topology column, multi-word filter; Modes/tab-bar arrow refinements ([ba22ccd](https://github.com/noonghunna/club-3090/commit/ba22ccd4b0f70dd4ec524027a155e7853769ff07))
- c3 cockpit: stopped-drill clear, arrow-navigable Modes, lane no-yank ([303d9b6](https://github.com/noonghunna/club-3090/commit/303d9b6bdef78c6222ca44c98dd9e5d31ad3186c))
- c3 cockpit: arrow-key focus descent (↓ into content, ↑ back to tab bar) ([0232797](https://github.com/noonghunna/club-3090/commit/02327971adfd2818fcbc2ce0633c1c935f43fdf2))
- c3 cockpit: fix keyboard focus/navigation (footer + tab bar) ([6bca4e6](https://github.com/noonghunna/club-3090/commit/6bca4e6f6120af498384dcb37ce8a91845346c54))
- c3 cockpit UX Tier-1: footer/binding hygiene (Codex review) ([982e034](https://github.com/noonghunna/club-3090/commit/982e034ca7d46b9e62ce22be2d8e7647df6a4db8))
- c3 cockpit: merge Run+Operate; Bring & Validate visible by default ([b3b842a](https://github.com/noonghunna/club-3090/commit/b3b842a6127d05977775f497eec41e06db548de7))
- c3 cockpit live-use fixes: table cursor preserve, curated profile dropdown, disk/RAM in the left rail ([ba984ca](https://github.com/noonghunna/club-3090/commit/ba984cadbccf6f2039586203c54aee29db48271d))
- c3 cockpit UX batch 5: estate telemetry — disk/RAM bars, studio-* services, GPU-VRAM attribution ([24b672f](https://github.com/noonghunna/club-3090/commit/24b672f1468b6a7c297df78c200c5f8d07f584c9))
- c3 cockpit UX batch 4b: inline previews + registry-derived profile dropdown ([171058c](https://github.com/noonghunna/club-3090/commit/171058c4471c5069aee579e745d61156f05e405b))
- c3 cockpit UX batch 4a: navigation & discoverability + an unsafe-gate Enter safety fix ([78facde](https://github.com/noonghunna/club-3090/commit/78facdee867f32c5340e3354c1448bd3dc4fdc49))
- c3 cockpit UX batch 3: honesty + serving actions (fit-vs-live-VRAM, real running config, targeted stop) ([bb2c30e](https://github.com/noonghunna/club-3090/commit/bb2c30ebca5528277853051e84472a5558efe363))
- c3 cockpit UX batch 2: perception loop — live surfaces reflect writes + fail honestly ([049ede8](https://github.com/noonghunna/club-3090/commit/049ede882048f45b1196c3bf306e817063676df7))
- c3 cockpit UX batch 1: serving panel, full service list, calm Containers, power/cap on cards ([dfe9004](https://github.com/noonghunna/club-3090/commit/dfe90043b0659d06e61f90dd179e7d5a92659b02))
- c3 Phase R / R4: in-app Contribute door (runtime surface toggle + persistence) ([ca67481](https://github.com/noonghunna/club-3090/commit/ca67481b02bcb4ce8832bf6908e443159d477dd0))
- c3 Phase R / R3b-2: ④ measure-vs-curated-bar + producer full-validation report ([a6df0c2](https://github.com/noonghunna/club-3090/commit/a6df0c2c0fab759cc3d0e17fe7f3c8c6f5c82124))
- c3 Phase R / R3b-1: producer "Bring & Validate" lane — ①–⑤ stages + ② Serve ([2c3c93d](https://github.com/noonghunna/club-3090/commit/2c3c93d9409a3741e617580459daff1e223dbf47))
- c3 Phase R / R3a: surface-gate the producer lane (consumer = Run + Operate) ([ddd70b6](https://github.com/noonghunna/club-3090/commit/ddd70b6c5431f597bc420496b05f2314035efaea))
- c3 Phase R / R2b: consumer share-back — rig report [R] / submit bench [B] / problem [!] ([2a5397a](https://github.com/noonghunna/club-3090/commit/2a5397ace4379ca3078383bd84f8042500567c6f))
- c3 Phase R / R2a: rename Estate → Operate + move Doctor into Operate ([250cd50](https://github.com/noonghunna/club-3090/commit/250cd50a93b8bc090cf62bf62274bd7046ee9c32))
- c3 Phase R / R1: fold Discover + Serve + Benchmarks into one Run mode ([8762442](https://github.com/noonghunna/club-3090/commit/8762442fc56274ecaf5a9ce218bd8a621be001cd))
- c3 Phase R / R0 fixups: surface gate before _ALWAYS_ON + de-flake gate tests ([e706f64](https://github.com/noonghunna/club-3090/commit/e706f6458733dc9a8ffee4df76c639a91147815a))
- c3 Phase R / R0: surface scaffolding (consumer | producer) ([b04093e](https://github.com/noonghunna/club-3090/commit/b04093e3306d61c9df7f519c56d64189e91c5880))
- Fix NVLink boot crash when compose pre-sets expandable_segments ([a4b8bd1](https://github.com/noonghunna/club-3090/commit/a4b8bd1d12b66fc6025b0455fa4fd93a3e96ef70))
- Fix estate GPU visibility overrides (#447) ([#447](https://github.com/noonghunna/club-3090/pull/447) by @Whamp)
- c3: auto-load container drill detail on select + consistent Esc ([1252921](https://github.com/noonghunna/club-3090/commit/12529211cb5e028d228568665539a6d9bd81fe6a))
- c3 catalog: instant first-paint + batched fit via kv-calc --fit-all ([24c1f19](https://github.com/noonghunna/club-3090/commit/24c1f194d4767b8af88c2d1c5b1b114dc23a10c4))
- Add kv-calc --fit-all: batch fit for all registry slugs in one process ([6653660](https://github.com/noonghunna/club-3090/commit/665366054f82d1077385d4a9b913b1e6e8081d34))
- Speed up c3 catalog load ~10x (parallelize per-slug enrichment) ([65a7f36](https://github.com/noonghunna/club-3090/commit/65a7f3616f5a3e46c99ff588ffaf85269fe5df12))
- Fix LMCache compose entrypoint for Compose v5 interpolation ([#429](https://github.com/noonghunna/club-3090/pull/429) by @steamEngineer)
- Fix c3 cockpit keyboard hotkeys: context-gated footer + focus ([e881738](https://github.com/noonghunna/club-3090/commit/e881738d3e82ee02305c2c113e4a901ad851225b))
- Phase 5 (v2): wire the c3t-Evaluate / promote-to-catalog / optimizer hooks ([b7b4b7d](https://github.com/noonghunna/club-3090/commit/b7b4b7d5fa2235cabf983d88a96a30f1f09ad795))
- Phase 4 (v1.5): wire the Validate mode + Estate write-extras ([581da4f](https://github.com/noonghunna/club-3090/commit/581da4f71d0fcafd0aeab2142660b00a0e272d43))
- Phase 3: wire cockpit panes to real data + reconcile-gated actions ([e5823bc](https://github.com/noonghunna/club-3090/commit/e5823bca0232f960cfa9901f501320fefde78d94))
- Phase 2b: add --json/CLI contracts to 7 stack scripts (additive) ([d09a063](https://github.com/noonghunna/club-3090/commit/d09a063317b1af94eb49084bc2545ee973463aae))
- Phase 2a: extract club3090_tui_core, repoint c3t + cockpit ([8bcbcd1](https://github.com/noonghunna/club-3090/commit/8bcbcd1846bca142a385ae84d67f757912ec1ada))
- Apply Codex Phase-1 review: harden registry shell call + mark bench mock ([450ece0](https://github.com/noonghunna/club-3090/commit/450ece0fa7048da516db208a02f02089660b0c6b))
- Mirror c3t shell: wider rail + persistent Estate status card ([21c66a6](https://github.com/noonghunna/club-3090/commit/21c66a6b13fd4613f5927a908fabeb7c8db34227))
- Enrich Phase-1 cockpit with representative visual mockups ([128c0ed](https://github.com/noonghunna/club-3090/commit/128c0ed8c5cd77e0a457bef3d68a535328e59321))
- Clarify c3 ⏎ action (per-mode) + fix mode-rail truncation ([b966f00](https://github.com/noonghunna/club-3090/commit/b966f005aee214980b4fd10049ee80497df8d5e0))
- Add serve cockpit (c3) — Phase 1 walking skeleton ([b520dfb](https://github.com/noonghunna/club-3090/commit/b520dfb9801bbb4160bc37aa32de3b50251cf0d8))
- Add NVLink auto-config to qwen3.6-35b-a3b dual (Production — rebench-gated) ([491226f](https://github.com/noonghunna/club-3090/commit/491226feadb12f54955539c75ec79c7466f8743c))
- Add NVLink auto-config to gemma-4-26b-a4b + diffusiongemma duals ([7481aa7](https://github.com/noonghunna/club-3090/commit/7481aa7351700067a90ca094eda2c899ee4c7eb2))
- Fix NVLink auto-detect dead on Docker Compose v5.1+ ([9a188b8](https://github.com/noonghunna/club-3090/commit/9a188b816b3d1b977f7f789e7e7dcad0aab16f63))
- Add c3t — the club-3090 test-console TUI (built by Qwen Max from the spec) (#428) ([#428](https://github.com/noonghunna/club-3090/pull/428) by @noonghunna)
- Record measured pi-reasoning rebench-full results + BENCHMARKS row ([79173b1](https://github.com/noonghunna/club-3090/commit/79173b12d5e5221be258efbd67051dde9b0ab1ca))
- quality-test / rebench-full: forward --max-tokens to benchlocal-cli (#426) ([#426](https://github.com/noonghunna/club-3090/pull/426) by @noonghunna)
- Correct pi-reasoning bench framing: 230W power-cap artifact, MTP head ≡ base ([78c4038](https://github.com/noonghunna/club-3090/commit/78c40388502735dbeb795e05a15969dc145aeab6))
- Pull gate: actionable messages for uncurated derives of curated models (#424) ([#424](https://github.com/noonghunna/club-3090/pull/424) by @noonghunna)
- LMCache: in-repo L2 default + LMCACHE_L2=1 toggle, preflight disk-check, corrected sizing (#422) ([#422](https://github.com/noonghunna/club-3090/pull/422) by @noonghunna)
- Correct LMCache L2 docs with measured numbers (fs adapter, ~125 KB/token, 4.8s rehydrate) ([9901129](https://github.com/noonghunna/club-3090/commit/9901129781ed6019aec15209a39c65d10cca46ad))



[Pin: `git checkout v0.10.0`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.9.0...v0.10.0)
## v0.9.0 — 2026-06-15


### ✨ Features

- feat(weights): optional revision: pin in weights-fetch schema (#319) (#408) ([#408](https://github.com/noonghunna/club-3090/pull/408) by @deucebucket)
- feat(bench-agentic): decouple context ramp from tool-call success (#255) (#396) ([#396](https://github.com/noonghunna/club-3090/pull/396) by @noonghunna)
- feat(rebench): make the 8-pack opt-in via --with-8pack-thinking (default-skip) (#338) (#395) ([#395](https://github.com/noonghunna/club-3090/pull/395) by @noonghunna)
- feat: add Qwen3.6-40B-Deckard to catalog (llamacpp/deckard40B-dual-mtp) ([5dafaa6](https://github.com/noonghunna/club-3090/commit/5dafaa61fea207302aac4b273df667d92162ad65))
- feat(vllm): opt-in offline/air-gap support across vLLM composes (#318) ([edd77cf](https://github.com/noonghunna/club-3090/commit/edd77cfd465e7da038349894fbeb330ed7eeea61))


### 🎯 New models + serving paths

- Add llamacpp/hauhaucs-35ba3b-dual uncensored MTP compose (🧪) (#410) ([#410](https://github.com/noonghunna/club-3090/pull/410) by @noonghunna)
- Add Carnice-V2-27B beellama single-card compose (beellama/carnice-v2-single-q5km-mtp) (#406) ([#406](https://github.com/noonghunna/club-3090/pull/406) by @noonghunna)
- Add experimental DiffusionGemma dual fp8 vLLM compose + patches ([83e8353](https://github.com/noonghunna/club-3090/commit/83e8353ed48963ff8c89fda8b12d54be6b807dd4))
- Add Qwen3.6-27B fast/max tiers across dual + multi4 (4 slugs) (#340) ([#340](https://github.com/noonghunna/club-3090/pull/340) by @noonghunna)
- Add Qwen3-Omni-30B-A3B vLLM-Omni compose (non-registry, 2x3090) (#317) ([#317](https://github.com/noonghunna/club-3090/pull/317) by @noonghunna)


### 🐛 Bug fixes

- fix(gpu-mode): stop gemma-4-12b chat in video-studio + comfyui modes ([#376](https://github.com/noonghunna/club-3090/pull/376) by @noonghunna)
- fix(35b-a3b): bump preview-single gpu-mem 0.92->0.95 for v0.22.0 boot ([195bd47](https://github.com/noonghunna/club-3090/commit/195bd470abb2ab8452061d88fc79d5f02504d155))
- fix(35b-a3b): correct AutoRound INT4 hf_repo (#316) ([121330c](https://github.com/noonghunna/club-3090/commit/121330c95e83600b7b83fc5da974b58808b18cfd))


### 📝 Documentation

- docs(UPSTREAM): #39598 MTP-streaming tool-call drop is un-mitigated on v0.22.0 (P64 retired); #145 closed ([8e38f7a](https://github.com/noonghunna/club-3090/commit/8e38f7a5ecd5b7d25e0c67a533ae021bee2d4d41))
- docs(BENCHMARKS): add author-rig Cerebellum-v3 data point (35B-A3B, #390/#393) ([85087ad](https://github.com/noonghunna/club-3090/commit/85087ad5b55dd8526c6e268f79489847eb655695))
- docs(UPSTREAM): mark #40361 closed-superseded by #45295; track v0.23.0 pin ([18656e7](https://github.com/noonghunna/club-3090/commit/18656e7b8d215e28fc02f6e7ea4ce2b7f198dbaf))
- docs(ARCHITECTURE): drop pinned version on 'surfaces (current)' marker ([fb114bf](https://github.com/noonghunna/club-3090/commit/fb114bfde9e451cb339415b1fd20dce650d34c8b))
- docs(README): refresh 35B-A3B row + drop stale NEW v0.7.3 tags ([a36d2c0](https://github.com/noonghunna/club-3090/commit/a36d2c0911d9d10be2231925b2d2e035987fef33))
- docs(README): un-stale 35B-A3B vLLM-dual row (preview→Production, 262K) ([0689fc4](https://github.com/noonghunna/club-3090/commit/0689fc4875969447b571d760b06c3f4063e29cc2))
- docs(README): correct 35B-A3B llama.cpp ❌→✅ (mainline serves the MoE; #390) ([559a3fe](https://github.com/noonghunna/club-3090/commit/559a3febf72ef11779b470a5fe0223b927a17aca))
- docs(ai-studio): add architecture diagrams to README/image/audio ([81b7157](https://github.com/noonghunna/club-3090/commit/81b71579ca8cd0f908ee07ccc92344ddf0930d9a))
- docs(ai-studio): scope the umbrella to image/video/audio — text is the core stack ([fd81dc2](https://github.com/noonghunna/club-3090/commit/fd81dc26de23e4b6a24cf8f4c6979a4d43e66bda))
- docs: relocate Studio docs into docs/ai-studio/ + add overview & audio (#386) ([#386](https://github.com/noonghunna/club-3090/pull/386) by @noonghunna)
- docs(video-studio): boxed architecture diagram + Quickstart/First-run (match IMAGE_STUDIO) ([96794a0](https://github.com/noonghunna/club-3090/commit/96794a064c8a3264579ab1331ab195eac660e5b7))
- docs(video-studio): add a user-facing 'How to prompt' section ([4abdadd](https://github.com/noonghunna/club-3090/commit/4abdaddf0e6f1f1416f75499c7a4b70993ec98f7))
- docs: reconcile DUAL/MULTI_CARD for the qwen fast/max tiers (#340) ([c51dc23](https://github.com/noonghunna/club-3090/commit/c51dc23dde57fe60a129219cdbb1bd40ff5d252b))
- docs(ADDING_MODELS): quant & arch gotchas checklist (Step 1) ([21d01bd](https://github.com/noonghunna/club-3090/commit/21d01bdaad06b0723518200268ed333d7182d82e))
- docs: quant-fidelity (KLD/QAT) + the Ampere KV-dtype traps (int8-PTH native, fp8-guard) ([3382a47](https://github.com/noonghunna/club-3090/commit/3382a47f40d21fd68635e044fa4db7f1a4c90c49))
- docs(upstream): repoint Gemma engine-pin row to vllm-gemma-stable + add vllm-stable row (#324 fidelity) ([09a4482](https://github.com/noonghunna/club-3090/commit/09a448238d53d1c30573ab612288421a864a742c))
- docs(adding-models): extend coherence rules — patch roles, engine identity/channels, test matrix ([b314ea9](https://github.com/noonghunna/club-3090/commit/b314ea97a7a5dfc96f9897117188647869518954))
- docs(internals): drop stale /opt/ai vLLM-clone path (marlin-pad overlay is vendored) ([4730406](https://github.com/noonghunna/club-3090/commit/47304065f45c10f7bb7ca344ee8e9d3a530f391a))
- docs: drop stale /opt/ai vLLM-clone instructions (marlin-pad is vendored + auto-mounted) ([47f6291](https://github.com/noonghunna/club-3090/commit/47f6291ad2947de6e0dd40814ccdf7d30ff16a93))
- docs(faq,dual-card): image/video gen guidance + 2x3090 multimodal lessons ([924883c](https://github.com/noonghunna/club-3090/commit/924883c560a629762fa5e85edea14002a9ebb1bc))
- docs(qwen3-omni): add image/video gen options, UI recommendations, 2x3090 lessons ([8c1370b](https://github.com/noonghunna/club-3090/commit/8c1370b6879eea22e7a250e33350c8227fb91cc4))
- docs(qwen3-omni): correct text decode to ~164 tok/s (12 was the audio path) ([4eed607](https://github.com/noonghunna/club-3090/commit/4eed6070042a8c469c596967c347c51360a98cdb))
- docs: document the compose filename convention (serving-feature delta) ([edc44c4](https://github.com/noonghunna/club-3090/commit/edc44c4367fe9b423776a803a83fcdf31f69c4c4))
- docs(ADDING_MODELS): document the registry slug-naming convention ([28794da](https://github.com/noonghunna/club-3090/commit/28794dabffddff566fed7ab24fd6e4ba32875b8b))
- docs(UPSTREAM): record gemma4 p-RoPE fix shared on vllm#39914 ([d391f32](https://github.com/noonghunna/club-3090/commit/d391f3272f211811aae9f885edabaee06b8cfeba))
- docs(ADDING_MODELS): accommodate Codex registry-onboarding review ([d080757](https://github.com/noonghunna/club-3090/commit/d080757c2dc29c75b3bc08cd27dcfb5402443edd))
- docs(WSL_SETUP): add 'Expose the API to your local network (LAN)' section ([d11f29d](https://github.com/noonghunna/club-3090/commit/d11f29dcf6765336078740263cc9472388025b10))
- docs(UPSTREAM): track Gemma-4-12B unified 256K large-prefill OOB (vllm#39914) ([960cbf4](https://github.com/noonghunna/club-3090/commit/960cbf4763c936330f6291c74d49062ee73d2800))


### 🛠️ Scripts + tooling

- verify-full: add streaming tool-call check + a reusable streaming probe (#404) ([#404](https://github.com/noonghunna/club-3090/pull/404) by @noonghunna)
- setup.sh: make Genesis opt-in, stop the default stale-pin clone (#182) (#399) ([#399](https://github.com/noonghunna/club-3090/pull/399) by @noonghunna)
- scripts: auto-detect served model from /v1/models in verify/bench (#372) (#388) ([#388](https://github.com/noonghunna/club-3090/pull/388) by @noonghunna)
- setup.sh: add diffusiongemma-26b-a4b dispatch (fetch fp8 weights) ([8ffa46d](https://github.com/noonghunna/club-3090/commit/8ffa46d51dd50099c385b413968eed6af42d8e77))
- bench.sh: FORCE_TOKENS — bench at a fixed/larger output size ([0948e6b](https://github.com/noonghunna/club-3090/commit/0948e6bbea6f692b29a503d651d89ac08eff404f))
- switch.sh --owui: auto-register a launched model in Open WebUI ([111c72b](https://github.com/noonghunna/club-3090/commit/111c72b0eabd741d689dd474c3a4c8ecad83a93b))
- preflight: resolve ${VAR:-default} model paths in compose-deps check ([345f24e](https://github.com/noonghunna/club-3090/commit/345f24ee1d7f83a915b1aac40013cca59684f70b))
- preflight: detect endpoint by engine port, not a model-name allowlist (#310) ([f48a7ff](https://github.com/noonghunna/club-3090/commit/f48a7ff51411cf547a1fed5a1e48851f20e522c3))


### 🧹 Maintenance

- test(weights): opt-in HF-repo resolve guard (#320) (#409) ([#409](https://github.com/noonghunna/club-3090/pull/409) by @deucebucket)
- chore: make setup script work with WEIGHTS=FP8 and qwen3.6-27b (#369) ([#369](https://github.com/noonghunna/club-3090/pull/369) by @hlo-world)
- chore(327): archive the Qwen3.6-27B DFlash path + deprecate vllm-nightly-dflash ([cc3e906](https://github.com/noonghunna/club-3090/commit/cc3e906f8ca8338f8acbb38b43e98b9b0035daad))
- chore(254): deprecate the now-unused Genesis nightly engines + patches [Phase 3+4] ([baac1ac](https://github.com/noonghunna/club-3090/commit/baac1acafdcd07ec36e5fc51c8c3514e3e424b09))
- chore(254): archive 15 Genesis/nightly composes + migrate the cascade [WIP: 5 test fixtures] ([b5ef9e6](https://github.com/noonghunna/club-3090/commit/b5ef9e697fe42982a05ba94f4a8e90b76c0b3ef2))
- chore(254): migrate qwen-a3b-preview-single off purged nightly-clean -> vllm-stable ([36ee7bb](https://github.com/noonghunna/club-3090/commit/36ee7bbd9470f651fca9ecd9b8abee2bb707bc98))
- refactor(vllm): reconcile vLLM engines to v0.22.0 — two-engine split (#254) ([a9ffb53](https://github.com/noonghunna/club-3090/commit/a9ffb532efcea285982d036bfde07b301ca44ffc))


### 🧹 Other

- BENCHMARKS: add DiffusionGemma 26B-A4B section + cross-rig row (#405) ([0542de8](https://github.com/noonghunna/club-3090/commit/0542de8c573d672d6e687d289c715e61c93850fd))
- Fix soak-test container auto-detect: match by engine port, not model allowlist (#405) (#414) ([#414](https://github.com/noonghunna/club-3090/pull/414) by @noonghunna)
- Pin hauhaucs-35ba3b-dual weights to morikomorizz commit 49a080d (#319) (#413) ([#413](https://github.com/noonghunna/club-3090/pull/413) by @noonghunna)
- qwopus-coder compose: sanitize /opt/ai/hf-download.sh leak in Quick-start -> generic hf download ([69f8632](https://github.com/noonghunna/club-3090/commit/69f8632083d58e651097c77002800638fa4b8eaa))
- deckard-40b: anti-loop sampling defaults (rep-penalty 1.1 + repeat-last-n 256) + DRY opt-in (#402) ([#402](https://github.com/noonghunna/club-3090/pull/402) by @noonghunna)
- ik-llama: migrate spec-dec flags to --spec-type + digest-pin the image (#401) ([#401](https://github.com/noonghunna/club-3090/pull/401) by @noonghunna)
- Add curated quality-baseline corpus + auto-diff (#252 Phase 1) (#397) ([#397](https://github.com/noonghunna/club-3090/pull/397) by @noonghunna)
- catalog: add beellama/qwopus-coder (Qwopus3.6-27B-Coder, KVarN-4) — first KVarN compose (#391) ([#391](https://github.com/noonghunna/club-3090/pull/391) by @noonghunna)
- beellama: bump pin v0.3.0 → v0.3.2-preview (commit-pinned) + validate (#389) ([#389](https://github.com/noonghunna/club-3090/pull/389) by @noonghunna)
- setup: fix fp8 weights nits after #369 (typo, help string, manual_note) ([eae0e36](https://github.com/noonghunna/club-3090/commit/eae0e36f81877170f06549fb4017dfa635af1e9a))
- openwebui: pin OWUI task models to the qwen director (not the generation pipe) ([d7c6e6d](https://github.com/noonghunna/club-3090/commit/d7c6e6d7b1aefe8e1f42a642c88b9934285228f3))
- studio(pipe): ignore OWUI internal task prompts — stop rendering them as images ([0dddfa7](https://github.com/noonghunna/club-3090/commit/0dddfa790eb9824fc4202eb245cc1d43f872e2f7))
- studio(pipe): drop the visible <!--SPEC--> refine marker — read 'Prompt used:' instead ([892324f](https://github.com/noonghunna/club-3090/commit/892324f436f35dc850f40aa7c47bc24c7b558242))
- studio: add push-pipe-to-owui.sh — update the installed OWUI function in one command ([d67a067](https://github.com/noonghunna/club-3090/commit/d67a06773c0596b31761aa732ec795e3cd51f7f1))
- studio(pipe): intent-gate the director — don't render on greetings/small-talk (#387) ([#387](https://github.com/noonghunna/club-3090/pull/387) by @noonghunna)
- studio: add 🎙️ Voice lane — Step-Audio-EditX premium clone (isolated service) (#385) ([#385](https://github.com/noonghunna/club-3090/pull/385) by @noonghunna)
- studio: add ✨ HiDream-O1 image lane (top-quality / photoreal) (#384) ([#384](https://github.com/noonghunna/club-3090/pull/384) by @noonghunna)
- studio: add 🔊 SFX lane (Stable Audio Open) — sound effects + ambient (#383) ([#383](https://github.com/noonghunna/club-3090/pull/383) by @noonghunna)
- studio: add 🎵 Music lane (ACE-Step) — songs + instrumentals ([#382](https://github.com/noonghunna/club-3090/pull/382) by @noonghunna)
- studio: integrated voices for video — Kokoro TTS + layer-aware audio mixdown ([#381](https://github.com/noonghunna/club-3090/pull/381) by @noonghunna)
- studio: add Chroma uncensored image lane (the "Sulphur for stills") ([#380](https://github.com/noonghunna/club-3090/pull/380) by @noonghunna)
- studio: fix OWUI native 🖼️ image button via ComfyUI reverse-proxy shim ([#379](https://github.com/noonghunna/club-3090/pull/379) by @noonghunna)
- studio: fix image-lane _min_caption fallback (empty arrays hard-block) ([#378](https://github.com/noonghunna/club-3090/pull/378) by @noonghunna)
- studio: add 🖼️ Image lane (Ideogram-4) with JSON-caption director ([#377](https://github.com/noonghunna/club-3090/pull/377) by @noonghunna)
- studio: in-chat 60s+ via orchestrator (auto-chain segments -> one video) ([#375](https://github.com/noonghunna/club-3090/pull/375) by @noonghunna)
- studio: extend-chain tool for 60s+ video (proven, seamless joins) ([#374](https://github.com/noonghunna/club-3090/pull/374) by @noonghunna)
- studio: video lane (LTX-2.3 / Sulphur) — Director pipe, gallery, gpu-mode, docs ([86f7e5e](https://github.com/noonghunna/club-3090/commit/86f7e5e835441e1d9aad4f445f82d14dc84b5c69))
- comfyui: claim pip cache for container uid so it persists across recreates ([#370](https://github.com/noonghunna/club-3090/pull/370) by @noonghunna)
- soak-helper: count silent-empty by completion_tokens, not decode_tps ([#368](https://github.com/noonghunna/club-3090/pull/368) by @noonghunna)
- quality-test: add --no-thinking (symmetric force-off for reasoning A/B) ([#367](https://github.com/noonghunna/club-3090/pull/367) by @noonghunna)
- soak-test: add beellama- to container auto-detect glob (#362) ([#366](https://github.com/noonghunna/club-3090/pull/366) by @noonghunna)
- UPSTREAM: dgemma #45163 — add promote-to-caveats trigger (hold at experimental for now) ([ffd525a](https://github.com/noonghunna/club-3090/commit/ffd525a7f673fd0ece4d662fd861a3f4d28a0417))
- dgemma: adopt official vllm/vllm-openai:gemma image (drop 120-file sideload) ([0cfd099](https://github.com/noonghunna/club-3090/commit/0cfd099b37f254ef817c7a9462373b0b8f3bbe2b))
- gpu-mode: add `dgemma` mode (DiffusionGemma 26B-A4B dLLM, dual-card) ([f8ad9a0](https://github.com/noonghunna/club-3090/commit/f8ad9a01c1d25e3daa96ff556f225f5b306b7e9f))
- Wire DiffusionGemma into the catalog via stock-nightly sideload ([af1e909](https://github.com/noonghunna/club-3090/commit/af1e909b04ee9c4504d143ab2483c9344615c219))
- gpu-mode: add `deckard` mode (uncensored 40B, dual-card) ([1cee8eb](https://github.com/noonghunna/club-3090/commit/1cee8eb43d600c6929be06dad301f00d5cbc0354))
- test-measurement-record: make BENCH_MOCK capture hermetic (#478) ([71a05fd](https://github.com/noonghunna/club-3090/commit/71a05fd444e9e723eaf3d1ee87eaf93c4e09a737))
- Promote Deckard-40B to ✅ Production; fix arch + slug naming ([93acbf9](https://github.com/noonghunna/club-3090/commit/93acbf979f897383630b68be2e6bf199d16949fa))
- Deckard-40B: fix provenance — GGUF is PiehSoft's, wire hf_repo fetch ([d6725fa](https://github.com/noonghunna/club-3090/commit/d6725faf0259a344277175070557f9609a0ec002))
- Deckard-40B: record soak PASS + final 105/150 (gates all green) ([20e1d6f](https://github.com/noonghunna/club-3090/commit/20e1d6f36272e1cfc844c7b205b2720030f22a59))
- Fix deckard40B compose: pin b9570, disk-count 45, status word ([881a449](https://github.com/noonghunna/club-3090/commit/881a449d4172d32c58d1d1a9e51e1396c5776b83))
- image-studio setup: real preflight (docker/GPU/disk/hf/chat-model) before heavy work ([caca7b8](https://github.com/noonghunna/club-3090/commit/caca7b8cba3a8903f2a6e3d9cb679d6c2a5eaa0b))
- image-studio P1 follow-up: setup UX, LiteLLM route, architecture docs ([18902fa](https://github.com/noonghunna/club-3090/commit/18902fa49571e124d86f50d60a1d2416bff1a996))
- image-studio P1 docs: add IMAGE_STUDIO.md + index/README/FAQ pointers ([c28470c](https://github.com/noonghunna/club-3090/commit/c28470c5f869b7e698ec908c61c2550c806f4ddc))
- image-studio P1: pin ComfyUI commit + drop hardcoded OWUI secret ([092b7c7](https://github.com/noonghunna/club-3090/commit/092b7c7a46f822f3f159dbcdfefa5c5e4118226a))
- Add image-studio bundle P1: Ideogram-4 + gemma-12b chat + gpu-mode mode ([9981b28](https://github.com/noonghunna/club-3090/commit/9981b286980ab0a2733ec4ab77c768aba71877a8))
- Add vllm/qwen-27b-dual-balanced + record 3-way 8-pack A/B (tie) (#343) ([#343](https://github.com/noonghunna/club-3090/pull/343) by @noonghunna)
- Set 31B w4a16 default MTP n=4->3 (n-swept optimum) + update A/B record ([31dc2c4](https://github.com/noonghunna/club-3090/commit/31dc2c47569dd8e152b69f95f7957907731cb21c))
- Record 31B w4a16 8-pack A/B: 109/150 vs autoround 105 (comparable quality, weaker MTP) ([97b678e](https://github.com/noonghunna/club-3090/commit/97b678e4056f334c34222959dfd5e5255bc98aca))
- Experimental Gemma-4 QAT W4A16 vLLM composes + kv-calc int4 fix (#339) ([#339](https://github.com/noonghunna/club-3090/pull/339) by @noonghunna)
- gemma-26ba4b-single: promote INT8-PTH single → ⚠️ Production-w/-caveats (gate PASS) ([3a5ece7](https://github.com/noonghunna/club-3090/commit/3a5ece7bb55e35f950cfd15e66d4ef65767bd84b))
- gemma-26ba4b: add --reasoning-parser gemma4 (single int8 + dual) ([0375d89](https://github.com/noonghunna/club-3090/commit/0375d8977201504a3c16d684261a2177ea66af16))
- Repoint vllm/gemma-26ba4b-single to INT8-PTH long-ctx (#465) ([e2efb75](https://github.com/noonghunna/club-3090/commit/e2efb757a9eef7cae0486747e12487a0d6c4b83c))
- gpu-mode: add power-cap on/off/status controls ([87190f9](https://github.com/noonghunna/club-3090/commit/87190f90fac27fdc28498bb4d103eee23bb9c0b4))
- kv-calc: per-sequence KV-pool floor (capped at 1 GB), fix KV-light false-FAIL ([95e47fe](https://github.com/noonghunna/club-3090/commit/95e47fedc950ab5f7618756f069f95638191d565))
- Enable MTP on gemma-4-26b-a4b single + ladder both to max ctx (#326) ([95e1448](https://github.com/noonghunna/club-3090/commit/95e1448217cb7bc2f5db8c6adb318d4a76b6455c))
- Wire gemma-4-26b-a4b AWQ on stock vLLM v0.22.0; retire AutoRound (#326) ([48eaf82](https://github.com/noonghunna/club-3090/commit/48eaf8283c1e5ed3cd383fe0657383208f83bb04))
- Fix Genesis cleanup test fixtures ([6b26bd7](https://github.com/noonghunna/club-3090/commit/6b26bd7ffdd3f044115510a318f442cfdd31bd34))
- gemma-4-12b: record soak PASS in the 2 GGUF single-card headers ([5387614](https://github.com/noonghunna/club-3090/commit/5387614ad7f1f6bb27cc48652a652b94089dcfb9))
- gemma-4-12b: promote the two vLLM MTP composes to ⚠️ Production w/ caveats ([90c67dc](https://github.com/noonghunna/club-3090/commit/90c67dcc9f2a288359f16636bab23ee79eb201ec))
- gemma-4-12b: normalize gemma-12b slug naming + prune the no-MTP bases ([87b43f1](https://github.com/noonghunna/club-3090/commit/87b43f14d6573f607052d114b59583eed4ca52e3))
- gemma-4-12b int8: add 8-pack quality (105/150) to BENCHMARKS + compose headers ([4c390e7](https://github.com/noonghunna/club-3090/commit/4c390e7e22f6cd048805fbdc70fda3845664874a))
- gemma-4-12b: add single-card int8 MTP variant (n-swept) + register it ([077584a](https://github.com/noonghunna/club-3090/commit/077584ac0ab4580e6cf62b0ae45c82d947df9347))
- gemma-4-12b: add single-card vLLM INT8 compose (full 256K on one 3090) ([b444189](https://github.com/noonghunna/club-3090/commit/b4441892d397eab391a9930d8ec35a00c16de01e))
- gemma-4-12b: drop vendored p-RoPE overlay — upstream config fix supersedes it ([942c5c8](https://github.com/noonghunna/club-3090/commit/942c5c891fe3f310fb9af9c222922358ba923d4f))
- gemma-4-12b: fold rebench-full verdict into vLLM compose headers + BENCHMARKS ([8c4bcab](https://github.com/noonghunna/club-3090/commit/8c4bcab6f3b51c4cf2bb5c69afb547bd0ba9d69d))
- BENCHMARKS: Gemma-4-12B section (256K all-engine; vLLM 256K+MTP via p-RoPE overlay) ([96e9852](https://github.com/noonghunna/club-3090/commit/96e9852f80adcd410fb7f1a121420f91b546468d))
- gemma-4-12b: register single-card slugs beellama/gemma-12b + llamacpp/gemma-12b ([8b459af](https://github.com/noonghunna/club-3090/commit/8b459afa5862bfd4f416f1d96e0d0ee69ab546ec))
- gemma-4-12b vLLM: 256K via vendored gemma4 p-RoPE long-ctx overlay (#39914) ([872bb89](https://github.com/noonghunna/club-3090/commit/872bb898081d4053d7ac6e45974526aa88d327d1))
- gemma-4-12b mainline llama.cpp: single-card 256K (override-kv, q8_0 KV) ([8c1f811](https://github.com/noonghunna/club-3090/commit/8c1f811dd2244900dcce17a7e6ccad8e874c2dd5))
- gemma-4-12b composes: scrub internal /opt/ai/hf-download.sh from quick-start docs ([ab825e5](https://github.com/noonghunna/club-3090/commit/ab825e5ea46a1f8ee2c5dd3e8af32b00185d2985))
- gemma-4-12b beellama single-card: 256K via --override-kv (native p-RoPE) ([a63ccb0](https://github.com/noonghunna/club-3090/commit/a63ccb0195b7dc35864531cbfa53ae24fe7090c3))
- kv-calc: address Codex review notes (gemma4_unified calibration) ([7f5ef72](https://github.com/noonghunna/club-3090/commit/7f5ef72a40e092c982a6f298304128db461e9021))
- kv-calc: calibrate gemma4_unified global-KV per-token to measured anchor ([0f6f861](https://github.com/noonghunna/club-3090/commit/0f6f86195eb47069c3acfe78a00bf9a705fc5a42))
- Wire gemma-4-12b into curated catalog (vLLM gemma4-unified, bf16 + MTP) ([aff9890](https://github.com/noonghunna/club-3090/commit/aff989072089e8afe9b0c8f3466a93fecc3a19c8))



[Pin: `git checkout v0.9.0`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.8.7...v0.9.0)
## v0.8.7 — 2026-06-03


### ⚠️ Cliffs, gotchas, regressions

- Retract beellama v0.3.0 prose-DFlash "regression" — net-positive on tok/s ([f2b9dc2](https://github.com/noonghunna/club-3090/commit/f2b9dc2de45203747e7918dcda15d29f19c95da1))


### ✨ Features

- feat(35b-a3b): byteshape IQ4_XS ik-llama single-card preset — validated (#299) ([#299](https://github.com/noonghunna/club-3090/pull/299) by @noonghunna)
- feat(beellama): release v0.3.0 Q8_K_XL dual composes (experimental) + centralize image pin (#296) ([#296](https://github.com/noonghunna/club-3090/pull/296) by @noonghunna)
- feat(gemma): gemma duals → vLLM v0.22.0 (rebase #40391 lean + re-instate #42006) (#287) ([#287](https://github.com/noonghunna/club-3090/pull/287) by @noonghunna)
- feat(beellama): add beellama.cpp DFlash as first-class compose engine (#268) ([#268](https://github.com/noonghunna/club-3090/pull/268) by @noonghunna)
- feat(switch): hardware-filter --list by GPU count; add --all (#267) ([#267](https://github.com/noonghunna/club-3090/pull/267) by @noonghunna)
- feat: model-default resolver + user-pinnable defaults (PR-B) (#266) ([#266](https://github.com/noonghunna/club-3090/pull/266) by @noonghunna)
- feat(registry): slug health/availability flag (#265) ([#265](https://github.com/noonghunna/club-3090/pull/265) by @noonghunna)
- feat(switch): group --list by model · topology (#264) ([#264](https://github.com/noonghunna/club-3090/pull/264) by @noonghunna)
- feat(qwen3.6-35b-a3b): promote dual → 262K + vision Production (vllm/qwen-35b-a3b-dual) (#259) ([#259](https://github.com/noonghunna/club-3090/pull/259) by @noonghunna)


### 🐛 Bug fixes

- fix(nvlink): add NVLINK_MODE=pcie_p2p for PCIe P2P without NVLink (#290) (#291) ([#291](https://github.com/noonghunna/club-3090/pull/291) by @noonghunna)
- fix(report): detect beellama- containers in report.sh auto-detection ([8cb5027](https://github.com/noonghunna/club-3090/commit/8cb50273d9a04636c64c491801549f05227dcbef))
- fix(gemma): wire --reasoning-parser gemma4 on both duals (#289) ([#289](https://github.com/noonghunna/club-3090/pull/289) by @noonghunna)
- fix(kv-calc): shard qwen3-next-moe weights by TP (#260) (#261) ([#261](https://github.com/noonghunna/club-3090/pull/261) by @noonghunna)


### 📝 Documentation

- docs: surface the mandatory compose Profile header to contributors ([8f3ae5c](https://github.com/noonghunna/club-3090/commit/8f3ae5c62faf83a84997eae55cabcaa6e7da97ad))
- docs(BRING_YOUR_OWN): BYO models aren't registered — boot composes directly ([3b8e469](https://github.com/noonghunna/club-3090/commit/3b8e469f9f7dfd3b715656e3cda7bb211b36b9fe))
- docs(BRING_YOUR_OWN): note INT8 KV is a vendored patch, not a stock dtype ([6ddfaca](https://github.com/noonghunna/club-3090/commit/6ddfaca166b256c4ac0f78a6b9e083fc3a1cfa6d))
- docs(BRING_YOUR_OWN): split KV-quant guidance by engine ([a2d0af6](https://github.com/noonghunna/club-3090/commit/a2d0af6053a63e2c6fbc1a1c8a953d5f20734167))
- docs: add BRING_YOUR_OWN — serve/tune/validate your own model ([93e6cd8](https://github.com/noonghunna/club-3090/commit/93e6cd807db9214862a8c36f451acec834976dec))
- docs(CONTRIBUTING): broaden one-per-PR rule to feature/concern scope ([557e615](https://github.com/noonghunna/club-3090/commit/557e6157c440a3f1d7840ac128b9ed0923265266))
- docs(CONTRIBUTING): require one model per compose PR ([497c341](https://github.com/noonghunna/club-3090/commit/497c341a958deec6f05813a3c6303a4880254817))
- docs(FAQ): fix Copilot LLM Gateway entry — vllm/tools-text retired ([aa458bb](https://github.com/noonghunna/club-3090/commit/aa458bb34a66806f50365508726054c7f40249ea))
- docs(FAQ): agent stops mid-task → set client temperature to 0.6 (#232) ([6bc91b5](https://github.com/noonghunna/club-3090/commit/6bc91b5cc50ee3a0c2c8a2e8b09029bb4d1b0c02))
- docs: deprecate vLLM dual-dflash composes, redirect DFlash to beellama (#297) ([b7955ac](https://github.com/noonghunna/club-3090/commit/b7955acab3e3b7914b603b2f1ad0e5b70d3235c3))
- docs(beellama): point gemma-dflash-dual v0.3.0 override at Anbeeld's official image ([533d2c3](https://github.com/noonghunna/club-3090/commit/533d2c320543782dedf36fd70c35b5dd55b0971c))
- docs(bench): @hlo-world PCIe-P2P A/B validates NVLINK_MODE=pcie_p2p (#291/#290) ([55eb500](https://github.com/noonghunna/club-3090/commit/55eb500f63ea8633d197c2c49645556b9c2abb79))
- docs(beellama): correct prose-regression attribution — v0.3.0-wide, not SWA ([44358d1](https://github.com/noonghunna/club-3090/commit/44358d135a0ec3255a06b45d5761f8ceca2c7a97))
- docs(beellama): record v0.3.0 dual-3090 validation — multi-GPU DFlash fixed ([8da27fd](https://github.com/noonghunna/club-3090/commit/8da27fdbdf5c7ec2394e5d5ddf566ce7fa6b12f3))
- docs(gemma): record bf16-mtp 8-pack (reasoning-on 111/150) + cross-config quality summary ([b2d7d8f](https://github.com/noonghunna/club-3090/commit/b2d7d8fb7f1d04584ef5ff5376723478d6851f9a))
- docs(gemma): record int8-mtp v0.22.0 closeout — bench, soak PASS, 8-pack quality + reasoning A/B ([0abba3a](https://github.com/noonghunna/club-3090/commit/0abba3a8757e08b9d9246c73943647a8ba19c499))
- docs(FAQ): clarify model-switch scope — supported models only ([8356a11](https://github.com/noonghunna/club-3090/commit/8356a11e82036938acc42484fe69e0024e8db3f0))
- docs(FAQ): add 'how to switch to / try a different model' entry ([2aeec74](https://github.com/noonghunna/club-3090/commit/2aeec74301fcbf1735e344656f507e66a1d747d7))
- docs(quality-test): document failure-reason reading; fix drifted Failure-breakdown sample ([77c1cd6](https://github.com/noonghunna/club-3090/commit/77c1cd6c012485c642238648527dc70113dab2e1))
- docs(ik-apex-fit-mtp): warn RAM-constrained systems on --cache-ram + MTP OOM (#243) ([c61cfc4](https://github.com/noonghunna/club-3090/commit/c61cfc49b7f064cdcf27a7a7095f8f1cbe5cbfe7))
- docs: document quality-test timeout sizing (QUALITY_TEST.md + agent guide) ([9c333f4](https://github.com/noonghunna/club-3090/commit/9c333f42bb9e60315e645256c63bee2455c7aaf5))
- docs(UPSTREAM): add vLLM #39056 row + cross-reference to #39598 streaming fix (#354) ([0ed228c](https://github.com/noonghunna/club-3090/commit/0ed228c605beb2788112f9373b1f5cd93d87ba40))
- docs(hardware): correct turbo3 "quality-neutral" claim — it's avg-distortion, not tail ([572f1c9](https://github.com/noonghunna/club-3090/commit/572f1c96ca507c386ad1b8c1529d0d6e21205ffe))
- docs(faq): add "which KV-cache quant should I use?" entry ([6b85575](https://github.com/noonghunna/club-3090/commit/6b85575d711ee4e55bcde1af634d91356d99295e))
- docs(cliffs): NIAH certifies retrieval, not KV-quant tail quality ([a307846](https://github.com/noonghunna/club-3090/commit/a307846eb74b6614a09e225216a470956727a164))
- docs(bench): single-card 1x 3090 llama.cpp Gemma-4 rows (mainline FA_ALL_QUANTS + beellama DFlash) ([6b011f6](https://github.com/noonghunna/club-3090/commit/6b011f60909cab2d2e17fb51a4f08859a59d44cc))
- docs: flip CLAUDE.md/AGENTS.md symlink + document localhost requirement for sandboxed agentic packs ([#240](https://github.com/noonghunna/club-3090/pull/240) by @noonghunna)
- docs: make AGENTS.md a symlink to CLAUDE.md (one source, matches the /opt/ai convention) ([ef1d9b8](https://github.com/noonghunna/club-3090/commit/ef1d9b8a1c8c830b20cd6c17750fa593d87386ab))
- docs: link the docs index + ARCHITECTURE from the repo agent entry points ([dc7c613](https://github.com/noonghunna/club-3090/commit/dc7c613262023596991160dab721baaf0852cb4b))
- docs: formalize the add-a-model workflow for the post-refactor architecture + agent discoverability ([37871c6](https://github.com/noonghunna/club-3090/commit/37871c631729018165ce19dd1cdbf1c14e027ccb))


### 🔧 Pin bumps + upstream

- Bump vllm/minimal + vllm/dual to stable v0.22.0 (off nightly) (#277) ([#277](https://github.com/noonghunna/club-3090/pull/277) by @noonghunna)


### 🛠️ Scripts + tooling

- preflight: detect beellama + check spec-draft-model drafter GGUF ([180adb0](https://github.com/noonghunna/club-3090/commit/180adb083eae957e9c4434f2bf70cb54e3874472))
- switch.sh --list: show max context per slug (+ registry<->compose drift) (#283) ([#283](https://github.com/noonghunna/club-3090/pull/283) by @noonghunna)
- gpu-mode.sh: align with dual prune — drop dead 27b modes, gemma -> int8 default (#280) ([#280](https://github.com/noonghunna/club-3090/pull/280) by @noonghunna)
- setup.sh: reject extra positional args instead of silently ignoring them (#273) ([#273](https://github.com/noonghunna/club-3090/pull/273) by @noonghunna)
- quality-test.sh: forward --progress to benchlocal-cli, default ON (#248) ([#248](https://github.com/noonghunna/club-3090/pull/248) by @noonghunna)
- soak-test.sh: add qwen3.6-35b-a3b to container auto-detect glob (#244) ([#244](https://github.com/noonghunna/club-3090/pull/244) by @noonghunna)
- quality-test.sh: stop hardcoding --timeout-per-case 60 (benchlocal-cli #41) (#245) ([#245](https://github.com/noonghunna/club-3090/pull/245) by @noonghunna)


### 🧹 Maintenance

- refactor(gemma): rename dual slugs + ladder gemma-bf16-mtp to 131K (#286) ([#286](https://github.com/noonghunna/club-3090/pull/286) by @noonghunna)
- chore(beellama): default to published ghcr image (sm86-b9459-07ac3ce) (#270) ([#270](https://github.com/noonghunna/club-3090/pull/270) by @noonghunna)
- chore: retire vllm-club3090 image references (stack on stock vLLM) (#269) ([#269](https://github.com/noonghunna/club-3090/pull/269) by @noonghunna)
- chore(vllm): remove redundant nvlink-* dual composes (NVLink auto-detected) (#257) ([#257](https://github.com/noonghunna/club-3090/pull/257) by @noonghunna)
- chore(litellm): prune dead routes, add 35B-A3B dual, drop wildcard (#263) ([#263](https://github.com/noonghunna/club-3090/pull/263) by @noonghunna)
- chore(35b-a3b): drop the built-in-MTP A/B compose (vllm/qwen-a3b-preview-mtp) (#262) ([#262](https://github.com/noonghunna/club-3090/pull/262) by @noonghunna)


### 🧹 Other

- rebench: add fail-fast verify-full preflight + fix runtime skip set (#306) ([#306](https://github.com/noonghunna/club-3090/pull/306) by @noonghunna)
- rebench-full: swap aider step for think-ON 8-pack + live tee (#303) ([#303](https://github.com/noonghunna/club-3090/pull/303) by @noonghunna)
- Repoint stale single-card launcher hints off deprecated vLLM composes ([bb9f9f2](https://github.com/noonghunna/club-3090/commit/bb9f9f23a002ea5e1ae439189872060bf62fb586))
- beellama: refresh stale b9459 image refs to v0.3.0 ([#300](https://github.com/noonghunna/club-3090/pull/300) by @noonghunna)
- Add Results Card doc — standard format for sharing config results ([cabdf12](https://github.com/noonghunna/club-3090/commit/cabdf1286bb744c256ef2c5f19be0738d464de8b))
- Operational robustness (#281): orphan-safe switch.sh · reboot-surviving vLLM · multi-GPU power sweep (#285) ([#285](https://github.com/noonghunna/club-3090/pull/285) by @noonghunna)
- beellama Gemma-4 ctx: single 128K (caveats) + dual 262K parked/upstream-gated (#284) ([#284](https://github.com/noonghunna/club-3090/pull/284) by @noonghunna)
- Prune dual vLLM composes: qwen-27b -> one config; gemma-31b default -> gemma-int8 (#279) ([#279](https://github.com/noonghunna/club-3090/pull/279) by @noonghunna)
- Gemma vLLM -> v0.22.0: bump dual gemma-mtp, deprecate gemma-mtp-tp1 (#278) ([#278](https://github.com/noonghunna/club-3090/pull/278) by @noonghunna)
- Deprecate Genesis vLLM composes; vLLM single default → vllm/minimal (#276) ([#276](https://github.com/noonghunna/club-3090/pull/276) by @noonghunna)
- Align gemma sampling default to model card (top_k -1 -> 64) (#275) ([#275](https://github.com/noonghunna/club-3090/pull/275) by @noonghunna)
- Promote beellama/gemma-dflash to single-card Gemma-4-31B default (#272) ([#272](https://github.com/noonghunna/club-3090/pull/272) by @noonghunna)
- Promote beellama/dflash to single-card Qwen3.6-27B default (#271) ([#271](https://github.com/noonghunna/club-3090/pull/271) by @noonghunna)
- bench-agentic: anchor TTFT-growth to first warm turn (exclude cold-start) ([#114](https://github.com/noonghunna/club-3090/pull/114) by @noonghunna)
- Revive agentic context-depth benchmark ([a9cf70e](https://github.com/noonghunna/club-3090/commit/a9cf70effd756a6eb16d2e07c3d4c42bcb823053))
- Prune Gemma vLLM variants (9->3) and pin survivors to v0.21.0 ([#253](https://github.com/noonghunna/club-3090/pull/253) by @noonghunna)
- Fail loud on hollow measured records in measurement_record (#251) ([#251](https://github.com/noonghunna/club-3090/pull/251) by @noonghunna)
- Add measurement-record producer for bench runs (#249) ([#249](https://github.com/noonghunna/club-3090/pull/249) by @noonghunna)
- BENCHMARKS: flag Gemma mainline-llama.cpp 36.8 TPS row as does-not-reproduce (13.6/15.4 re-bench) ([95da8e1](https://github.com/noonghunna/club-3090/commit/95da8e1f85a1e3db827b107032dbe453922abaee))
- BENCHMARKS: post-PR #38 chain rebench for ik-llama/iq4ks-mtp (8-pack 101→107, aider 19→18 noise) ([8351956](https://github.com/noonghunna/club-3090/commit/8351956d9b9bcfdedde9fccfe995cc9098589769))
- scripts/preflight.sh: surface 4090 / 5090 hint with FAQ deep-link (#247) ([#247](https://github.com/noonghunna/club-3090/pull/247) by @noonghunna)
- docs/README: refresh supported-models table — single-card Gemma 4 31B + 35B-A3B now in production ([285c632](https://github.com/noonghunna/club-3090/commit/285c632442b72227c40231ea84c6731f001e2dc3))
- docs/README: add above-the-fold cross-rig callout for 4090 / 5090 owners ([eea717f](https://github.com/noonghunna/club-3090/commit/eea717fd5b68308fe29f23ab3fe70c192a7d899a))
- docs/FAQ: refresh 4090 / 5090 entries with cross-rig measurements ([2f0a54c](https://github.com/noonghunna/club-3090/commit/2f0a54c99503f1d02b49d06b4563d8807aa85a88))
- Add ik-llama apex-fit-q8q5 variant for Qwen3.6-35B-A3B (#242) (#243) ([#243](https://github.com/noonghunna/club-3090/pull/243) by @noonghunna)



[Pin: `git checkout v0.8.7`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.8.6...v0.8.7)
## v0.8.6 — 2026-05-26


### ✨ Features

- feat(ik-llama): PRISM-PRO-DQ + APEX-MTP presets, conformed to the <quant>/ layout ([458c473](https://github.com/noonghunna/club-3090/commit/458c473908242aab349a19529d2606feb28b2e3e))


### 🐛 Bug fixes

- fix(profiles): cover the new ik-llama PRISM/APEX presets in the compat catalog ([aa2a965](https://github.com/noonghunna/club-3090/commit/aa2a965bb93ea7c9cf50f6ef16a9bb1a14ce13f0))
- fix: post-PR-A compose-path fixes for gpu-mode.sh + 2 patch READMEs ([b23846e](https://github.com/noonghunna/club-3090/commit/b23846ea36c71ea2d86d3343eb2d367fa5d58b22))
- fix(registry+bench): sync vision defaults to the 2026-05-25 re-tune (#438) ([b116750](https://github.com/noonghunna/club-3090/commit/b116750ef16850ee2472f857cde4dbea6bd09c0a))
- fix(vision): re-tune single-card vision defaults to measured-safe (1M-px + 160K/150K) ([c9b7dd3](https://github.com/noonghunna/club-3090/commit/c9b7dd3999de78cf2847677e60503d1dafec5af9))
- fix(vllm/dual): pin to stable v0.21.0, drop all source overlays (#407 pin-drift) ([cf1f14f](https://github.com/noonghunna/club-3090/commit/cf1f14fbc781ec7fbfca060c791144dd79ab6308))


### 📝 Documentation

- docs+scripts: finish <quant>/ path migration across full repo sweep ([eaa7a8c](https://github.com/noonghunna/club-3090/commit/eaa7a8c1ad4dc36d39d6935944136cc0734e4ef2))
- docs(switch): correct ik-llama/iq4ks-mtp usage comment 262K -> 200K ([2135230](https://github.com/noonghunna/club-3090/commit/2135230f8f02fde978c897526c9b55618c22c7fd))


### 🧹 Maintenance

- refactor(launch): derive launcher tables from the registry + <engine>/default resolver ([a0520e2](https://github.com/noonghunna/club-3090/commit/a0520e2060966a3b63efadf95401f684417b4c62))
- refactor(compose): insert <quant> layer + make the registry the single source of truth ([9821c94](https://github.com/noonghunna/club-3090/commit/9821c94efb4ac837dcaaa6f5805a14b0c8b0a05d))



[Pin: `git checkout v0.8.6`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.8.5...v0.8.6)
## v0.8.5 — 2026-05-24


### ✨ Features

- feat(llama.cpp): Structured-CoT bounded-thinking compose + grammar-dialect fix (#214) ([#214](https://github.com/noonghunna/club-3090/pull/214) by @noonghunna)
- feat(kv-calc): opt-in --kv-breakdown architecture cache planning layer (#213) ([#213](https://github.com/noonghunna/club-3090/pull/213) by @noonghunna)
- feat(ik-llama/two-stage): ctx default 131072→200000 + promote 🧪→⭐ code option (#212) ([#212](https://github.com/noonghunna/club-3090/pull/212) by @noonghunna)


### 🐛 Bug fixes

- fix(rebench-report): surface ceiling VRAM margin in verify-stress section (#184) ([1055c91](https://github.com/noonghunna/club-3090/commit/1055c9162fe49f96025c21f4508dca8c009e4775))
- fix(switch): shell env wins over .env (MODEL_DIR etc.) + CRLF-tolerant (#425) ([9a27de8](https://github.com/noonghunna/club-3090/commit/9a27de83d7e6aff293d9f423bc926ff9366ed993))
- fix(ik-llama/two-stage): default ngram n_max 64→4 (tuned code-decode optimum) (#210) ([#210](https://github.com/noonghunna/club-3090/pull/210) by @noonghunna)
- fix(#168): scope report.sh kv-calc calibration to the running model ([477873a](https://github.com/noonghunna/club-3090/commit/477873af93e35c6978b42abf11b890935909ae5b))
- fix(#169): distinct default container_name per llama.cpp/ik single variant ([9e5f200](https://github.com/noonghunna/club-3090/commit/9e5f200449ceb87a64838e60e8f074d468326ed3))


### 📝 Documentation

- docs(BENCHMARKS): 4090 ik-two-stage cross-rig row + 4090 ctx-derate note (#184) ([703fa3c](https://github.com/noonghunna/club-3090/commit/703fa3cc119b590198551da7c844f906c00505cb))
- docs(README): direct docker-compose fallback when launch/switch error + default capture to --full ([27e818f](https://github.com/noonghunna/club-3090/commit/27e818f559f125d3ab438a62f4db84bf353dd45c))
- docs(BENCHMARKS): add thinking-on vs no-think code-gen baseline (Qwen3.6-27B) ([d8adf55](https://github.com/noonghunna/club-3090/commit/d8adf55b4b582ff70dffbaf536f7cad8bf0e3d8a))
- docs(README): Windows/WSL2 signpost at top of Quick start ([f954692](https://github.com/noonghunna/club-3090/commit/f954692676107aef38e7794ea3150079db9c8817))
- docs(WSL): add Diagnostics section — suggest pciutils, set lspci/WSL2 expectation ([d36eb63](https://github.com/noonghunna/club-3090/commit/d36eb633c6d7e5ace99faa40dc9725ae0ccf6ad6))
- docs(WSL,FAQ): clarify club-3090 needs WSL2 — native Windows = upstream engine only ([6fa639b](https://github.com/noonghunna/club-3090/commit/6fa639bb5ad85231de55446775139a9851e5c845))
- docs(README,WSL): fold reasoning suite into Benchmarks; add native llama.cpp + overhead-reduction to WSL guide ([80527f9](https://github.com/noonghunna/club-3090/commit/80527f99708a1c0af972b8e8b3507c341faa98c8))
- Document reasoning quality suite ([605f1df](https://github.com/noonghunna/club-3090/commit/605f1df52e4f7bb2a85cd676ebe56827c163ef9d))
- docs: add WSL2/Windows from-scratch setup guide (#187) ([3c1a6e9](https://github.com/noonghunna/club-3090/commit/3c1a6e962a1206f920e28009c4055fa11f9dcc08))
- docs(README): add Benchmarks + Diagnostics sections ([37574fe](https://github.com/noonghunna/club-3090/commit/37574fe4c00a39059631069876e4131842588601))
- docs(diagnostics): redact internal paths in structured-cot-bench.md ([3b270b9](https://github.com/noonghunna/club-3090/commit/3b270b99a35636070cba0f15b25ae1cdec4715c1))
- docs: promote iq4ks-two-stage 🧪→⭐ (code, 200K) + BENCHMARKS row ([7e6eaf8](https://github.com/noonghunna/club-3090/commit/7e6eaf8f005a84ef968ead7a0138267298834706))
- docs(SINGLE_CARD): add measured two-stage TPS (~59/~98, code +35% vs MTP-only) ([b10096c](https://github.com/noonghunna/club-3090/commit/b10096cca016fe6e4782a7d7f83055801dcedf10))
- docs(SINGLE_CARD): mark the #167-blocked vLLM configs in "Pick a config" ([cb19d68](https://github.com/noonghunna/club-3090/commit/cb19d6829c49af606970676b2840fadefdcc36ed))
- docs(README): drop SGLang from the headline engine claims (blocked, not a route) ([678fd00](https://github.com/noonghunna/club-3090/commit/678fd006c5036ab930f3aaf3a32d0c996eb28170))
- docs(README): single-card "recommended" → llamacpp/default (was #167-blocked vllm/default) ([44c08b6](https://github.com/noonghunna/club-3090/commit/44c08b614668771a3cc637c7222197b90ab4b821))
- docs(DUAL_CARD): distinguish decode-concurrent vs long-prefill-overlap (#208) ([36767f1](https://github.com/noonghunna/club-3090/commit/36767f1dff66d1e7dac5e180a8b229144a935f32))
- docs(README): fix stale 'llama.cpp single = full 262K' → 200K in supported-models cell ([2a8357f](https://github.com/noonghunna/club-3090/commit/2a8357f2815423f3ae6ab0919c9c59211f870413))
- docs+registry: surface ik-llama on the single-card front door + fix stale max_ctx ([7f73361](https://github.com/noonghunna/club-3090/commit/7f733618e60899cb6878f16a5ba32b96daabd91c))
- docs(BENCHMARKS): refresh llamacpp/mtp row to the 200K thinking-off rebench ([2eca18d](https://github.com/noonghunna/club-3090/commit/2eca18d23399759cf38d08a28c49cbb4ecffa0cd))
- docs(#169 branch): fix stale 262K→200K cross-refs in single compose headers ([62a0f4b](https://github.com/noonghunna/club-3090/commit/62a0f4be63144dfe5d652861a650b7917cdc2f6f))
- docs: correct single-card llama.cpp/ik_llama ctx 262K -> 200K (shipped default) ([c7fc9ca](https://github.com/noonghunna/club-3090/commit/c7fc9ca638ab6b80a110fffff5637bfc0842aa4c))


### 🧹 Maintenance

- chore: retire the club-3090 pre-built vLLM image (workflow + docs) ([7003e61](https://github.com/noonghunna/club-3090/commit/7003e6141b8399fb2fe14019241f6f5d171e84a9))


### 🧹 Other

- Add profile-backed model weight fetch registry ([5f37ae6](https://github.com/noonghunna/club-3090/commit/5f37ae6d4d299e0ece942c6475d1b8ae7b275a4d))
- Generalize compose model preflight ([99d264b](https://github.com/noonghunna/club-3090/commit/99d264b2c460247091b8f10c4853e988f2a9ff90))
- Expose benchlocal reasoning suite ([caf6fc2](https://github.com/noonghunna/club-3090/commit/caf6fc2b723c46c70a6dcd38d2778f1d5e1e469c))



[Pin: `git checkout v0.8.5`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.8.4...v0.8.5)
## v0.8.4 — 2026-05-23


### ✨ Features

- feat(verify-stress): capture prefill throughput during NIAH rungs (#199) ([07d478c](https://github.com/noonghunna/club-3090/commit/07d478c1abfb9873cb106708ee05aa94473866f0))
- feat(eval): expose request-level thinking toggles (#196) ([#196](https://github.com/noonghunna/club-3090/pull/196) by @noonghunna)
- feat(scripts): pass --sampling-from-server through quality-test.sh + rebench-full.sh ([dd1f070](https://github.com/noonghunna/club-3090/commit/dd1f07062642e7a583b19c4e977885ea8404f404))
- feat(compose): expose sampling defaults via env (#194) ([#194](https://github.com/noonghunna/club-3090/pull/194) by @noonghunna)
- feat(setup): WEIGHTS=gguf to fetch the llama.cpp GGUF (not just the vLLM model) (#191) ([#191](https://github.com/noonghunna/club-3090/pull/191) by @noonghunna)
- feat(ik-llama): wire iq4ks-mtp + iq4ks-mtp-vision into launch.sh + switch.sh (#189) ([#189](https://github.com/noonghunna/club-3090/pull/189) by @noonghunna)
- feat(models): add ik_llama Qwen3.6-27B IQ4_KS composes — text 262K + vision 160K (#180) ([#180](https://github.com/noonghunna/club-3090/pull/180) by @noonghunna)


### 🐛 Bug fixes

- fix(rebench): basename model id for the aider/litellm step (ik_llama full-path id → 0/30) ([3b20ce3](https://github.com/noonghunna/club-3090/commit/3b20ce3c7cb53f49512f2af098fe175db5683d8b))
- fix(soak,preflight): recognize llama-cpp / ik-llama containers in autodetect (#403) ([d9fdab2](https://github.com/noonghunna/club-3090/commit/d9fdab296103e240527210fb5af131361fe07223))
- fix(compose): ik iq4ks-mtp header — record measured ceiling-ladder result (200K confirmed) ([1d93343](https://github.com/noonghunna/club-3090/commit/1d9334335f278dcef89f0b817815f243e9d42b57))
- fix(compose): lower single-card MTP CTX_SIZE default 262144 → 200000 (llama.cpp + ik_llama) ([2e45928](https://github.com/noonghunna/club-3090/commit/2e45928e4c455115f509555e54c6c0e6223499e4))
- fix(verify-stress): three live-caught bugs in ceiling ladder (#199) ([b84249c](https://github.com/noonghunna/club-3090/commit/b84249c805d7ce9f311e215f227e32049917ce87))
- fix(verify-stress): add CTX_SIZE-scaled ceiling ladder (#199) ([5a825a4](https://github.com/noonghunna/club-3090/commit/5a825a428a43bcd54fa1b6a3e9a91a2767c5be63))
- fix(report): PyYAML/idle-VRAM/P2P/redaction/kv-calc polish + review fixes (#178/#137) ([#192](https://github.com/noonghunna/club-3090/pull/192) by @noonghunna)
- fix(launch): point users at MODEL_DIR/.env when weights aren't found (#190) ([#190](https://github.com/noonghunna/club-3090/pull/190) by @noonghunna)
- fix(llamacpp): pin image to server-cuda-b9246 (rolling tag broke at b9282) (#188) ([#188](https://github.com/noonghunna/club-3090/pull/188) by @noonghunna)
- fix(launch): single-card default suggestion → llamacpp/default (#185) ([#185](https://github.com/noonghunna/club-3090/pull/185) by @noonghunna)
- fix(rebench): always capture sandboxed-pack logs to the per-tag results dir (#179) ([#179](https://github.com/noonghunna/club-3090/pull/179) by @noonghunna)


### 📝 Documentation

- docs: correct ik_llama verdict — ~18-20% FASTER than mainline, not a "tie" (#184) ([b7353da](https://github.com/noonghunna/club-3090/commit/b7353daa52f851e71ea2974b673ed1329372c234))
- docs: add @mgabor3141 X399/TR-1950X dual.yml row + pre-Zen2 CPU-IPC note (#178) ([6e49960](https://github.com/noonghunna/club-3090/commit/6e499609b4566830b603ec024cd311db0bbadcae))
- docs(CLIFFS): document llama.cpp "boots ≠ fills" false ceiling; 200K = max-safe single-card CTX_SIZE ([9be237d](https://github.com/noonghunna/club-3090/commit/9be237da7407478a61a5f6a7212ad686375f86d1))
- docs: QUALITY_TEST.md — fix stale pack-status (sandboxed packs now implemented) ([f6bdc06](https://github.com/noonghunna/club-3090/commit/f6bdc067dc8dc4992f2c67e23d28a8a9ab50a4eb))
- docs: document sampling/temperature eval options (#193/#194 + benchlocal #19/#21) ([9fd634a](https://github.com/noonghunna/club-3090/commit/9fd634a5b5ef13a902b201db60fd5a8bb666cef9))
- docs(single-card): strike Genesis-pinned vLLM rows (blocked by purged pin #167) ([a30bdfd](https://github.com/noonghunna/club-3090/commit/a30bdfd812a8fcd912b3764d49ba1e204351ace7))
- docs(upstream): correct the #40875 row (open tool-call-corruption bug, not "closed coexistence") ([25f130a](https://github.com/noonghunna/club-3090/commit/25f130a2868a1a79329baca8bbe3fca51035e313))
- docs: correct ik_llama claims to the matched-power tie (#184) ([c470d9a](https://github.com/noonghunna/club-3090/commit/c470d9a32dbcbb66b54a214a44abddaf11f8a80f))
- docs: surface WEIGHTS=gguf + switch.sh ik-llama paths (match #189/#191) ([412315d](https://github.com/noonghunna/club-3090/commit/412315d9ccf9fd251dfff3e3d3a88a0347d67315))
- docs(HARDWARE/FAQ): AMD-Vi IOMMU Xid 154 under TP=2 → iommu=pt fix (#178) ([fe86b72](https://github.com/noonghunna/club-3090/commit/fe86b72a73ec94e6a610711f33778465f8c004d1))
- docs: add ik_llama engine page + QUANTIZATION primer; surface IQK quants ([554b85b](https://github.com/noonghunna/club-3090/commit/554b85b8ea3cc7bdb3cb69a0a37f551870e74037))
- docs(BENCHMARKS): @duart dual NVLink Proxmox VFIO-passthrough, stock-upstream no-Genesis (disc #162) ([bc6e20b](https://github.com/noonghunna/club-3090/commit/bc6e20bb8e110372381f5dd930b1e111141e15f2))
- docs(BENCHMARKS): @mgabor3141 dual.yml — Z77/i7-3770K, PCIe 2.0 x4 slowest cross-card link (#178) ([626fa68](https://github.com/noonghunna/club-3090/commit/626fa68a7fa4be0a70f0e53cfe514e86c8e2d7ed))
- docs(mtp-vision): surface the -ub 512 → 192K context recipe in the compose header ([70bf7e7](https://github.com/noonghunna/club-3090/commit/70bf7e74be185a0f20a5d4cacd4c356aa7c4cf08))
- docs: cross-link the -ub vs ctx trade-off into SINGLE_CARD + CLIFFS + FAQ ([035261b](https://github.com/noonghunna/club-3090/commit/035261bc5831090dd2da4190e6262d4679336afd))
- charts: compose names on x-axis + description legend block below ([07c7cd0](https://github.com/noonghunna/club-3090/commit/07c7cd0222dc5ce646703137515a4aad2d0c8908))
- charts: tighten single-card label format (line 1 = variant + ctx, line 2 = modifier) ([9aa8fa7](https://github.com/noonghunna/club-3090/commit/9aa8fa71ab99306ba730d29686e5963a1ef1bebc))


### 🛠️ Scripts + tooling

- scripts: endpoint-first --url/--model/--engine for non-Docker engines (#174) ([#174](https://github.com/noonghunna/club-3090/pull/174) by @noonghunna)
- report.sh: capture image digest + OCI labels (build tag, upstream commit) ([78556f8](https://github.com/noonghunna/club-3090/commit/78556f88158be9e5baeda6fee03e15d5787077b0))


### 🧹 Maintenance

- chore(compose): drop accidentally-committed qwopus3.6-27b-v2 llama.cpp compose ([b8aeb93](https://github.com/noonghunna/club-3090/commit/b8aeb93333e904f2cef01069a0402b34aa8c731e))
- refactor(llamacpp): collapse single-card composes 3→2 (default = mtp alias) (#181) ([#181](https://github.com/noonghunna/club-3090/pull/181) by @noonghunna)


### 🧹 Other

- Fix verify-full to accept reasoning_content ([3a04ae5](https://github.com/noonghunna/club-3090/commit/3a04ae50843c9aa04c7e1f13e37c67de85586554))
- quality-test: respect explicit MODEL/--model, don't clobber from /v1/models (#177) ([#177](https://github.com/noonghunna/club-3090/pull/177) by @noonghunna)
- sglang: park EAGLE-3 path for Qwen3-Next (MTP wins everywhere) (#176) ([#176](https://github.com/noonghunna/club-3090/pull/176) by @noonghunna)
- quality-test: expose --timeout-per-case + bump aider-polyglot-30 to 3600s (#175) ([#175](https://github.com/noonghunna/club-3090/pull/175) by @noonghunna)
- sglang: experimental EAGLE-3 + Qwen3-Next dual-3090 path (Codex-led patch) ([941fa06](https://github.com/noonghunna/club-3090/commit/941fa0644ec3e98ee0fa0a190f87fdec3d923784))
- SINGLE_CARD: refresh Luce DFlash + PFlash watch-list (2026-05-20) ([f9f9640](https://github.com/noonghunna/club-3090/commit/f9f9640a5148df8c451cb99ac3f409a898830bda))
- AGENTS: pin engine images only when we vendor patches ([6810768](https://github.com/noonghunna/club-3090/commit/68107680e092cf04ee4bc3ab086687eed8b433fb))
- llama-cpp: document speed-vs-context trade-off + fix stale ub default ([1b2a76c](https://github.com/noonghunna/club-3090/commit/1b2a76ca897ae8df351989a585d54e9c3940e55e))
- llama-cpp: switch to rolling :server-cuda tag (no patches → no pin needed) ([4a53eda](https://github.com/noonghunna/club-3090/commit/4a53edab43cd649eaa1ac4c80a13bbb5a7b17437))
- llama-cpp: replace orphan llama-cpp:local with upstream pinned image (#170) ([c3e7c7e](https://github.com/noonghunna/club-3090/commit/c3e7c7ed8036810e0c172f8b1cd7332ac33ac924))
- gpu-mode status: probe :8020 + detect engine on :8030 ([db9c5e1](https://github.com/noonghunna/club-3090/commit/db9c5e1bb9bfd01bd37e4c23038c62805db40b26))



[Pin: `git checkout v0.8.4`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.8.3...v0.8.4)
## v0.8.3 — 2026-05-20


### 📝 Documentation

- docs: add LOCAL_AI_PRIMER.md — plain-English on-ramp for newcomers ([b07b2f9](https://github.com/noonghunna/club-3090/commit/b07b2f99e78809641427900044fa73cd41574c0f))


### 🧹 Other

- BENCHMARKS: add llamacpp/mtp + llamacpp/mtp-vision rows ([37c739b](https://github.com/noonghunna/club-3090/commit/37c739b4f9e37e3c3a5eb0fe51b5dd8e6b011abc))
- llama.cpp single: thinking-off policy alignment + MTP profile family ([ed15071](https://github.com/noonghunna/club-3090/commit/ed1507122cfd20627315de99d8258aa494f8cb4a))



[Pin: `git checkout v0.8.3`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.8.2...v0.8.3)
## v0.8.2 — 2026-05-19


### ✨ Features

- feat(pull): v0.8.2 STEP V5 — recommend UX + report-a-failed-pull doc + §9-reconciliation ([c5b5e9b](https://github.com/noonghunna/club-3090/commit/c5b5e9b27e24c04a880a0504b7497e266c2c8044))
- feat(nvlink): auto-detect NVLink on N-GPU topologies; add detection to multi4 + gemma-4-26b dual ([8f8ec1c](https://github.com/noonghunna/club-3090/commit/8f8ec1cebe375cf687550ce1724d1545386f36e4))
- feat(pull): v0.8.2 STEP V4 — optional whichllm hw-detect subprocess (CONTRACT-3, hw-detect-only) ([3917728](https://github.com/noonghunna/club-3090/commit/39177282b793549e6e4f2ac960358f0204c9cc5e))
- feat(switch): v0.8.2 STEP V3 — switch.sh ↔ compose_registry parity (CONTRACT-2b-ii) ([e6503bc](https://github.com/noonghunna/club-3090/commit/e6503bc046e569a7d6adac46dc768418bd14f0a8))
- feat(pull): v0.8.2 STEP V3 — arch-registry expansion + chat-template attribution/drift_guard ([999c93f](https://github.com/noonghunna/club-3090/commit/999c93fe8c3629b484d5901de7e58dda84ad39b4))
- feat(pull): v0.8.2 STEP V2 — surface pointer + --submit-last/--submit (gh + gh-less, consented, F5 reuse) ([e1cdcb5](https://github.com/noonghunna/club-3090/commit/e1cdcb53c7c9ff32e5eb101df15944d0f99747d2))
- feat(pull): v0.8.2 STEP V1 — capture-on-hard-block pt1-gate emitter + BaseCaptureBundle protocol lift ([20f1557](https://github.com/noonghunna/club-3090/commit/20f1557d2992fa2d0362e0e95ee9b9264199cc38))
- feat(report): lspci PCIe/P2P diagnostics subsection (LnkSta/ACS/topology) (#148) ([af2e45a](https://github.com/noonghunna/club-3090/commit/af2e45ae96376a781b15f9cf8c6896e1b3ecf5ae))


### 🐛 Bug fixes

- fix(pull): v0.8.2 STEP V5 — recommend must not label a fits-clean model "DOES NOT FIT" ([26949d7](https://github.com/noonghunna/club-3090/commit/26949d7fa845979f2234a961abb53b3fedef3062))
- fix(pull): v0.8.2 STEP V3 — deliver CONTRACT-2's engine-supported broadening (TRC two-class) ([d78b9a9](https://github.com/noonghunna/club-3090/commit/d78b9a94963c581061c01b413827630cd65aafdd))
- fix(pull): v0.8.2 STEP V2 — gh-less issue body must not carry the absolute capture path ([52451ca](https://github.com/noonghunna/club-3090/commit/52451ca0b0b190eb6c194917f9aa7a0dba8155e0))
- fix(launch): force LC_NUMERIC=C so the VRAM-budget printf survives comma-decimal locales (#159) ([186dc93](https://github.com/noonghunna/club-3090/commit/186dc93fae60d7047a790033176f1c3c2e0bd54a))
- fix(deriver): correct stale "GGUF not supported until v0.8.1" message — now misleading post-v0.8.1-ship ([344ab87](https://github.com/noonghunna/club-3090/commit/344ab87dd3723cf0fc30834141c2ccb17f25f507))


### 📝 Documentation

- docs(architecture): bring current-state docs up to v0.8.2 (recommend / submit on-ramp / arch-registry / hwdetect) ([c5c8f46](https://github.com/noonghunna/club-3090/commit/c5c8f469b09ef17252cf2a4fd0a587ae9e9a2adf))
- docs(generator): state plainly that generated-compose capacity is the reference profile's, NOT fit-adapted ([247b1dc](https://github.com/noonghunna/club-3090/commit/247b1dcfe859f0da439d1bc41d21cd3e9efb8970))
- docs(pull): v0.8.2 STEP V6 — correct §9/headline to the true bundled release scope ([b791271](https://github.com/noonghunna/club-3090/commit/b79127176f34f67258e0dc50b1992032fa1c653e))
- docs: fix duplicate MULTI_CARD.md entry in docs index ([966a8d1](https://github.com/noonghunna/club-3090/commit/966a8d142f0c66f9a5ccde3d9adca39b575e5482))
- docs: reorder docsindex (GSD first), add FAQ TOC + promote troubleshooting ladder, add tool-calling example ([a891b39](https://github.com/noonghunna/club-3090/commit/a891b3921f8fd598237d4649b68dd552419583e8))
- docs: add GETTING_STARTED.md, Gemma 4 model READMEs, restructure main README with quick start first ([6368bae](https://github.com/noonghunna/club-3090/commit/6368bae648684c6e2c9645dc96bcf5aa7f5d1b05))
- docs: fix stale NVLINK_MODE comment, INTERNALS.md cliff status, and dead companion repo link ([28bd0e8](https://github.com/noonghunna/club-3090/commit/28bd0e89703b1c5052990dd071d4debb758867ce))
- docs(container-runtimes): Proxmox passthrough — NVLink is the fragile path, not Proxmox (#161) ([3f066a0](https://github.com/noonghunna/club-3090/commit/3f066a044dceb918709fa32a931511980b2cb0fc))
- docs(benchmarks): add @hlo-world dual-3090 PCIe x4 dual-dflash-noviz row (#158) ([135f2c4](https://github.com/noonghunna/club-3090/commit/135f2c48fd25b782a7f5c74b4ca828cb4682f812))
- docs(upstream): froggeric v19 re-eval PASSED — ADOPTED (#150) ([ec1fd65](https://github.com/noonghunna/club-3090/commit/ec1fd652e8b02aa1f752d581f6e8c1fd5fdef0f3))


### 🧹 Maintenance

- chore(chat-template): re-vendor latest froggeric Qwen3.6 template for re-eval (#150) ([8a9ea6c](https://github.com/noonghunna/club-3090/commit/8a9ea6ca45489ad8520d65a097203d4da1d78989))



[Pin: `git checkout v0.8.2`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.8.1...v0.8.2)
## v0.8.1 — 2026-05-17


### 🐛 Bug fixes

- fix(patch-attribution): register vendored gemma-4-31b pr41800 overlay (follow-up to #153/#154) ([b4b20ff](https://github.com/noonghunna/club-3090/commit/b4b20ff7b64394a4dbf9a4303c8bec9da95fc54f))
- fix(gemma-4-31b): vendor missing vllm-pr41800 overlay into the model tree (closes #153) ([9c79192](https://github.com/noonghunna/club-3090/commit/9c7919253d01615b9e1d54b31eacc08540bbb6fd))
- fix(pull): argparse usage errors exit 64, not 2 — distinguishable from honest hard-stop (#370) ([820eb38](https://github.com/noonghunna/club-3090/commit/820eb3845c2ed442e88be7312efc524e277094e5))


### 📝 Documentation

- docs(examples): correct "thinking on by default" — shipped composes set enable_thinking=false (#372) ([46bb271](https://github.com/noonghunna/club-3090/commit/46bb271737db263ad225b1fb10c3dd36b5aa389f))
- docs(hardware): newer-driver 3090 caps long-text.yml at MAX_MODEL_LEN=105000 (#149) ([b0774f9](https://github.com/noonghunna/club-3090/commit/b0774f953b24da40c9a4f8b8a79aa1c0f0fc735f))
- docs: fix v0.8.0 docs-fidelity gaps (trc-ack first-run heads-up, exit-code honesty, GGUF message claim) ([78a7dee](https://github.com/noonghunna/club-3090/commit/78a7dee2478e1d86805bf90371f6e586eb482e7e))
- docs: cross-link the v0.8.0 universal pull flow from the existing user guides ([afe56f7](https://github.com/noonghunna/club-3090/commit/afe56f763fccec340b693ed765879eaffcbcfd6f))



[Pin: `git checkout v0.8.1`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.8.0...v0.8.1)
## v0.8.0 — 2026-05-17


### ⚠️ Cliffs, gotchas, regressions

- v0.8.0 Pull-Gate P4-fix: price Tier-1 curated via curated-exact kv-calc spec, not generic-dense (+ non-mocked regression test) ([087a8ea](https://github.com/noonghunna/club-3090/commit/087a8ea6929144ca64b58d499161087111a290ab))


### 🐛 Bug fixes

- fix(verify-full): warm engine before scored checks (closes #352) ([c595496](https://github.com/noonghunna/club-3090/commit/c5954964c5ffa68a8997866296ec83aa349d9219))


### 📝 Documentation

- docs(tq3-mtp): add missing 04-gemma-vs-qwen.png chart ([da9ef5e](https://github.com/noonghunna/club-3090/commit/da9ef5eb108ed01aa436444e4708ba329e8e7662))
- docs: UPSTREAM Gemma4 TurboQuant row — exact config.py:101 mechanism + fix-PR set ([fd8695f](https://github.com/noonghunna/club-3090/commit/fd8695f1ab64082be8818bd72a72ea2d3f710cca))
- docs+hygiene: track Gemma4 native-TurboQuant upstream blocker; gitignore new MoE cache dirs ([f812715](https://github.com/noonghunna/club-3090/commit/f812715d3e8afce1f79969fb76e5ed600a337122))
- docs(KERNEL_MATRIX): add Kernel Selection Philosophy section ([287c766](https://github.com/noonghunna/club-3090/commit/287c76617d5a3432f04425e876889ed6e43b7891))


### 🧹 Other

- Merge PR #147: v0.8.0 — Universal pull (evaluate & serve any safetensors HF model) ([#147](https://github.com/noonghunna/club-3090/pull/147) by @noonghunna)
- v0.8.0 [docs] PULL.md Quickstart (command-first, top-of-doc) + ARCHITECTURE one-liner: stage names are internal, users run one command ([bef766d](https://github.com/noonghunna/club-3090/commit/bef766d4ae2c5a03958c5da3d79bfa6a92ab01dd))
- v0.8.0 [review] pre-tag fixes: scrub internal-path leaks from shipped source + make .pull-captures-corpus tests CI-safe (skip-when-absent) ([49d9bb4](https://github.com/noonghunna/club-3090/commit/49d9bb4313a97d3cacd6cafdaebc5c2903fc4bfb))
- v0.8.0 [docs] ARCHITECTURE.md: add the universal pull→gate→emit→loop pipeline to the mental model + scripts tree (current-state, was stale for v0.8.0) ([1cdda19](https://github.com/noonghunna/club-3090/commit/1cdda195a77558a5cdef166fb7d184538b773140))
- v0.8.0 [UX] §7 two doc tracks: docs/PULL.md (user front-door) + docs/README.md (track spine) + README migration nudge ([a0b3b5c](https://github.com/noonghunna/club-3090/commit/a0b3b5c8b448a028f6037efeb610d4a53da18881))
- v0.8.0 [F] F8-fix: widen §6.1 Tier-1 OOM signature + pt3.actual regexes to real vLLM v0.21.0+ KV-cache-too-large phrasing — on-rig F8 caught classic-torch-only regexes miss the common KV-prediction failure ([f92624d](https://github.com/noonghunna/club-3090/commit/f92624d9a78c18f5b92257a553abdf07e8071dcf))
- v0.8.0 [F] F7: docs/LOOP.md contributor doc (Loop phase, grounded in shipped F1–F6) + CONTRACT-5(i) risk note ([a8b30d6](https://github.com/noonghunna/club-3090/commit/a8b30d67072fe13bad7810c7ef751fc45c369c2f))
- v0.8.0 [F] F6: CONTRACT-5 mandatory content-hash kv_calc_version (G2) + G1 topo-verify + L2 fixture sync ([1ac0481](https://github.com/noonghunna/club-3090/commit/1ac048189d02ccf709942b1c066737f5d9c29e8e))
- v0.8.0 [F] F5: §6.3 canonical-tuple-hash dedup + bounded label scheme + collision-safe submit path (CONTRACT-4) ([5de7224](https://github.com/noonghunna/club-3090/commit/5de7224a731bfefb70cda038cdd8bf3d0d48915d))
- v0.8.0 [F] F4: §6.2 inbound-trust pipeline raw→candidate→validated→Tier-1 + CONTRACT-3a derived-deferral (CONTRACT-3) ([d758f08](https://github.com/noonghunna/club-3090/commit/d758f08fce86d81d80370ad037ce12e2edc54339))
- v0.8.0 [F] F3: G6-A 3-part additive [E] touch (pt1.predicted_b_breakdown, pt3.failure_log_excerpt+actual, container-log capture) + §6.1 Tier-1 (CONTRACT-2) ([b100979](https://github.com/noonghunna/club-3090/commit/b1009793f26f38370ba2a013ed93d2b6044e0b59))
- v0.8.0 [F] F2: §6.1 Tier-2 semantic-fingerprint classifier + Appendix A seed DB (CONTRACT-2 Tier-2) ([9f80d29](https://github.com/noonghunna/club-3090/commit/9f80d29fbe63cd9302221a7d182693b5f803ca82))
- v0.8.0 [F] F1: FInput capture-bundle reader + schema-1 validation + key-normalization (CONTRACT-1) ([1491cbc](https://github.com/noonghunna/club-3090/commit/1491cbc7afaa48df924e2ea27446b7dc3b782c42))
- v0.8.0 [E] E-outcome-fix: honest 3-state manifest outcome (partial-success != failed) — §6.2 partial is a capability-scoped success ([71148d6](https://github.com/noonghunna/club-3090/commit/71148d6054b4616ada57654b7c405cb0c0d50cc6))
- v0.8.0 [E] E3/E4-fix: boot lifecycle as context manager (server stays up for smoke+capture, teardown on ctx-exit) — on-rig E5 caught teardown-in-finally-before-smoke ([f7c405a](https://github.com/noonghunna/club-3090/commit/f7c405a06d4c8c2ef349533d5d9e6ee59455a073))
- v0.8.0 [E] E3-fix: smoke probes the real served-model-name (not literal "derived") + capture failure detail — on-rig E5 caught red-smoke-on-healthy-boot ([16a1e4d](https://github.com/noonghunna/club-3090/commit/16a1e4d944992682ac5c8db9b8f7482730e3b9e6))
- v0.8.0 [E] E2-fix-2: verify *.safetensors against HF API lfs.sha256 (not Xet-redirect-fragile HEAD x-linked-etag) — on-rig E5 caught false no-etag ([3ae74bf](https://github.com/noonghunna/club-3090/commit/3ae74bfdcfc9ddc4378003c04180d934282b8482))
- v0.8.0 [E] E2-fix: download via hf CLI subprocess (not huggingface_hub lib-import) — on-rig E5 caught ModuleNotFoundError ([806a298](https://github.com/noonghunna/club-3090/commit/806a2985226cd1c6ab9f726882e5a610ba2da69f))
- v0.8.0 [E] E5(docs): docs/PULL_EMIT_DERIVED.md (+ private ledger/recon-checklist updates) ([d134d5a](https://github.com/noonghunna/club-3090/commit/d134d5a5fcc2b509e7e259430954c192d18bea44))
- v0.8.0 [E] E4: post-[C1] derived-[E] orchestration + trigger semantics + override force-capture (pt5) ([2ed18aa](https://github.com/noonghunna/club-3090/commit/2ed18aad3fd1f648d4a143d91e9e86d97b785f08))
- v0.8.0 [E] E3: derived boot (HF_HOME mount) + 4 §6 capture emitters + manifest + derived smoke floor ([f327887](https://github.com/noonghunna/club-3090/commit/f327887c3926b8c119afd1d4883f64f40e1b83a6))
- v0.8.0 [E] E2: HF download stage (download_set allowlist + x-linked-etag SHA, no-etag fail-closed, atomic staging) ([7a2ec86](https://github.com/noonghunna/club-3090/commit/7a2ec8664052044677c1724cc46ea78a7cd2988e))
- v0.8.0 [E] E1: generate_from_profile + derived-vllm template + EInput + CONTRACT-5 gate ([411c84f](https://github.com/noonghunna/club-3090/commit/411c84fd8ae692acd99824754b292f387ecf9486))
- v0.8.0 Pull-Gate P5: docs/PULL_GATE.md (two-path model, 6-stratum taxonomy, §4.1 [C1], hardware-SM) ([2582438](https://github.com/noonghunna/club-3090/commit/2582438d0202b0082464cca0bbb1dbee46d2725c))
- v0.8.0 Pull-Gate P4: stratum-5 + [C1] §4.1 total fn + stratum-6 [D] dry-run + pull orchestrator + exhaustive test-pull.sh ([adf7a3b](https://github.com/noonghunna/club-3090/commit/adf7a3bf13e424e96ffb510d318faaf016ebf975))
- v0.8.0 Pull-Gate P3: stratum-2 precondition + [C0] engine-support/runtime/hardware gate + [C2a] disk ([4a1d385](https://github.com/noonghunna/club-3090/commit/4a1d3857f25de46c60ff8c0b7f566733f32a2a6f))
- v0.8.0 Pull-Gate P2: transformers deriver + ModelProfile/confidence + variant-scoped hf_repos schema ([818b79c](https://github.com/noonghunna/club-3090/commit/818b79ccb523aca5034fefe4abddebf5c697dab2))
- v0.8.0 Pull-Gate P1: kv-calc generic-dense family + eligibility predicate + raw_verdict adapter ([1bafcfe](https://github.com/noonghunna/club-3090/commit/1bafcfe4a008c8d4e89763d872a99618e3853112))
- v0.8.0: doc generated composes are not relocatable (run with --project-directory) ([a2fc05e](https://github.com/noonghunna/club-3090/commit/a2fc05e1c873ff4a6a3bc97de7df1685b41e5006))
- v0.8.0 STEP 5: COMPOSE_GENERATOR.md + PATCH_POLICY.md (#141 contributor contract) ([9546f99](https://github.com/noonghunna/club-3090/commit/9546f99303bfcd907618d7778cf36237c33b858e))
- v0.8.0 STEP 3+4: compose generator + 5-triple golden-parity test (#141) ([6d7a043](https://github.com/noonghunna/club-3090/commit/6d7a043d907aedab88cc10c8b97bea75a2c4a81d))
- v0.8.0 STEP 2: extract patch_attribution.py (sound body-only reaches(), test imports it) ([60f3983](https://github.com/noonghunna/club-3090/commit/60f39832834051a294deb445bfc62d5ca90d0486))
- v0.8.0 Phase A-prime: enrich patch/profile data for #141 generator (compose_service_template, genesis_equipped, delivery metadata, drift_guards, drafter/model_slug/trc fold-ins) ([9f23736](https://github.com/noonghunna/club-3090/commit/9f23736f014dbbea74b56a4287836019d0315fb9))
- Add v0.8 Phase A patch attribution data ([91a9622](https://github.com/noonghunna/club-3090/commit/91a9622619ba2b1360676a95e412f30d3e975d7c))



[Pin: `git checkout v0.8.0`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.7.4...v0.8.0)
## v0.7.4 — 2026-05-15


### 🐛 Bug fixes

- fix(vllm-pr35936): make overlay tolerate bf610c2f upstream drift (closes #144) ([421114b](https://github.com/noonghunna/club-3090/commit/421114b9ddb47288365d3c9e27931671a9755a47))


### 📝 Documentation

- docs(BENCHMARKS): @OVDEN13 dual.yml — PCIe Gen 4 x4+x8 asymmetric (#142) ([77802a3](https://github.com/noonghunna/club-3090/commit/77802a3d8ee18bfa72a0a929ba1e22de661d22eb))


### 🧹 Maintenance

- test(launch): re-align engine pin expectations after revert ([e7bca8e](https://github.com/noonghunna/club-3090/commit/e7bca8e035d03240d791626631bdaf7c2c2182fe))


### 🧹 Other

- Reapply "fix(qwen3.6-27b): route non-TQ3 composes to vllm-nightly-clean" ([d780410](https://github.com/noonghunna/club-3090/commit/d7804107c96f04fc0008dbab84332c2438349aa4))
- Revert "test(launch): re-align engine pin expectations after revert" ([0c4260f](https://github.com/noonghunna/club-3090/commit/0c4260f53d5c84da51d758de9c5c2d1d2d99800c))
- Revert "fix(qwen3.6-27b): route non-TQ3 composes to vllm-nightly-clean" ([d32e168](https://github.com/noonghunna/club-3090/commit/d32e168a89f21af0c4c9d447ea196efd0b2e42b6))



[Pin: `git checkout v0.7.4`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.7.3...v0.7.4)
## v0.7.3 — 2026-05-15


### ✨ Features

- feat(report): surface kv-calc calibration verdict ([#143](https://github.com/noonghunna/club-3090/pull/143) by @noonghunna)
- feat(kv-calc): model v0.7.3 MoE architectures ([39e1873](https://github.com/noonghunna/club-3090/commit/39e18733aa8f14c83a1f76d5bed23156fda61568))
- feat(gemma-4-26b-a4b): AWQ + MTP n=4 — +12% narr / +49% code over no-MTP baseline ([6dc9a0d](https://github.com/noonghunna/club-3090/commit/6dc9a0dce1b4ecef787e50808a8a15439cabe209))
- feat(qwen-35b-a3b): preview-MTP compose + bench row — MTP measured SLOWER on MoE ([e1d44bd](https://github.com/noonghunna/club-3090/commit/e1d44bd732cef0757b8d3f0f872b5b0a1a4fe5cc))
- feat(vllm-pr41800): vendor truncate_prompt_tokens overlay across all pre-fix engines (closes #139) ([1d7aad1](https://github.com/noonghunna/club-3090/commit/1d7aad112c097709d954750ab0e725a785ad062a))
- feat(gemma-4-26b-a4b): AWQ path via vLLM PR #40886 overlay ([0053444](https://github.com/noonghunna/club-3090/commit/0053444e84f80ce9f3fb910435c8d627591f59ed))
- feat(estate): add parallel boot mode ([99328b4](https://github.com/noonghunna/club-3090/commit/99328b4cda7ec9efc723a001295525a6d1f86e2a))
- feat(moe): add dual-card composes for Gemma 26B-A4B + Qwen 35B-A3B preview ([2d1b1dc](https://github.com/noonghunna/club-3090/commit/2d1b1dc347c3897f8b902f7ab60c8bd9c97abbeb))
- feat(moe): wire Gemma 4 26B-A4B + Qwen 3.6 35B-A3B composes through fits() ([f7f6f44](https://github.com/noonghunna/club-3090/commit/f7f6f444b9e937396c3de70df7dd6a5b957be80b))
- feat(profiles): split engine-pin policy by Genesis dependency ([15eda8a](https://github.com/noonghunna/club-3090/commit/15eda8a823dd273ee9b238369cba365021b61a29))
- feat(profiles): add Gemma 4 26B-A4B ModelProfile + num_global_kv_heads field ([abf0e32](https://github.com/noonghunna/club-3090/commit/abf0e327f9b877f989fe16c88bda1a457c144e0a))
- feat(profiles): add Qwen 3.6 35B-A3B ModelProfile (MoE schema extensions) ([9378714](https://github.com/noonghunna/club-3090/commit/937871492ae08b58b041a1fded41ab793f0c8549))


### 🐛 Bug fixes

- fix(gpu-mode): mode_off tears down estate-managed instances ([9cd854d](https://github.com/noonghunna/club-3090/commit/9cd854dbcb9b8b215876e0f88443c269072b93b9))
- fix(qwen3.6-27b): route non-TQ3 composes to vllm-nightly-clean ([3b2d940](https://github.com/noonghunna/club-3090/commit/3b2d940d26ec2ffe6daf631e77986898c1d2849d))
- fix(gemma-4-31b): route default/bf16 composes to vllm-nightly-clean ([cf0451a](https://github.com/noonghunna/club-3090/commit/cf0451a7ad5c56bd7b63327aac7178df70cba1fb))
- fix(engines): vllm-nightly-mtp anchors to 01d4d1ad (Sander v7.72.2 PROD pin) ([87f0a0c](https://github.com/noonghunna/club-3090/commit/87f0a0c528473a225f06997bdcb9b79fefa13b04))


### 📝 Documentation

- docs(soak-test): clarify PASS verdict semantics — closes #140 ([9a039d8](https://github.com/noonghunna/club-3090/commit/9a039d8c922d3141102e8244d5468e8de46c6674))
- docs(UPSTREAM): add PR #41800 truncate_prompt_tokens row ([273c017](https://github.com/noonghunna/club-3090/commit/273c017646087fe508626be7ecea5e2106be54be))
- docs(README): add v0.7.3 MoE models to Supported Models table ([e49c939](https://github.com/noonghunna/club-3090/commit/e49c9397481b5fba226323b59c4fa37bdc2aeeab))
- docs(BENCHMARKS): Gemma 4 26B-A4B AWQ first row + AutoRound row demoted ([92b69bd](https://github.com/noonghunna/club-3090/commit/92b69bd220ce8360d2dfd5fdcf89d26ee2264791))
- docs(BENCHMARKS): add v0.7.3 MoE preview section ([bdfb939](https://github.com/noonghunna/club-3090/commit/bdfb939edd98c3872439a7a05dcde13cce7ccaa2))
- docs(HARDWARE): add note on PCIe Gen 3 + older CPU TP=2 headwind ([8cf38b0](https://github.com/noonghunna/club-3090/commit/8cf38b05906e3954405af3db09a822ac87a25ae5))
- docs(KERNEL_MATRIX): add KV Cache Impact subsection ([1a233cd](https://github.com/noonghunna/club-3090/commit/1a233cd9fd05a6ec51adfadae79813bc80cea4b0))
- docs: add KERNEL_MATRIX.md (attention backend + engine support matrix) ([97195fe](https://github.com/noonghunna/club-3090/commit/97195fe443770bc8adc883755fd3baf9933df874))
- docs(kv-math): extend k_v_tensors=N notation to sliding-KV formulas ([b1c68b4](https://github.com/noonghunna/club-3090/commit/b1c68b4fe3211af3442cd3bb7e9fd011e30e5554))
- docs(kv-math): tighten k_v_tensors notation across all 4 formulas ([54d8bf0](https://github.com/noonghunna/club-3090/commit/54d8bf0b3e2b322dbd67e6939ff9f9995c642437))
- docs(kv-math): third-pass Grok polish ([67de3ec](https://github.com/noonghunna/club-3090/commit/67de3eca3eb4b75b43fd0f83d2ed304976b3f1b5))
- docs(kv-math): second-pass Grok polish ([78f94ca](https://github.com/noonghunna/club-3090/commit/78f94cacf006064f68d945122907d30be8723eec))
- docs(kv-math): address Grok review feedback ([3114399](https://github.com/noonghunna/club-3090/commit/31143999837639b5a7d492d2f2b64e164787bcfe))
- docs(kv-math): config-verify Qwen 35B-A3B + Gemma 26B-A4B MoE sections ([6ec6a67](https://github.com/noonghunna/club-3090/commit/6ec6a6761f36cca44ea819434be7205bcb6fdbc6))


### 🧹 Maintenance

- test(launch): align engine pin expectations ([127f4f6](https://github.com/noonghunna/club-3090/commit/127f4f6d8fe104a954b7865a4d7550017a1c629b))



[Pin: `git checkout v0.7.3`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.7.2...v0.7.3)
## v0.7.2 — 2026-05-15


### ✨ Features

- feat(launch): add hardware topology advisor ([d116ba9](https://github.com/noonghunna/club-3090/commit/d116ba9ba3442482e0005bab9067d304b40e5e24))



[Pin: `git checkout v0.7.2`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.7.1...v0.7.2)
## v0.7.1 — 2026-05-15


### ✨ Features

- feat(bench): surface prompt processing throughput ([2a148d7](https://github.com/noonghunna/club-3090/commit/2a148d702b9415129d4c4ec9d3e7d30765927aa4))
- feat(llamacpp): expose batch tuning knobs ([02249ab](https://github.com/noonghunna/club-3090/commit/02249ab1939f354ac062d343efefe32677203174))


### 🐛 Bug fixes

- fix(ci): simplify vllm image workflow, drop smoke-gate (#135) ([ce2617e](https://github.com/noonghunna/club-3090/commit/ce2617e0bc0f56d42caf64e96847d966380be80c))


### 📝 Documentation

- docs(upstream): PR #42102 closed-as-slop; local overlay permanent ([57eb269](https://github.com/noonghunna/club-3090/commit/57eb269cd70935fc3069b85e46ead8f0f0af13dc))



[Pin: `git checkout v0.7.1`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.7.0...v0.7.1)
## v0.7.0 — 2026-05-14


### ✨ Features

- feat(scripts): add diagnose-profile triage ([c2adb39](https://github.com/noonghunna/club-3090/commit/c2adb3970dbdcb3bf227cfc7a1ac58a2de3930a4))
- feat(compose): use profile-sourced vllm image pins ([e6e33ab](https://github.com/noonghunna/club-3090/commit/e6e33ab37235cdfa2d47987e16e00d617564e55d))
- feat(launch): export profile vllm pins ([c306383](https://github.com/noonghunna/club-3090/commit/c3063838bfde3f7811db3edbb9541814aea8f09d))
- feat(profiles): resolve vllm nightly pins ([40f1ef7](https://github.com/noonghunna/club-3090/commit/40f1ef78f8e3ab80a5424ce196c7715df85a0d1a))
- feat(launch): add estate planner orchestration ([c9b153f](https://github.com/noonghunna/club-3090/commit/c9b153f91f3dd4a076395008ad3bfecdd226a452))
- feat(launch): validate single-model profiles ([a142b1c](https://github.com/noonghunna/club-3090/commit/a142b1ce1085c78e8752fa52718af66f7a49f237))
- feat(compat): add profile validator and estate self-test ([6581ccc](https://github.com/noonghunna/club-3090/commit/6581ccca9e8613594dba876ba2472e78d48c9eed))
- feat(compose): accept ESTATE_GPUS and ESTATE_PORT overrides ([a57596e](https://github.com/noonghunna/club-3090/commit/a57596e0764babc6fe91e96af8b6dd746da45e09))
- feat(profiles): ship v0.7.0 data layer ([69825d7](https://github.com/noonghunna/club-3090/commit/69825d7dae0fe1387a04879b31e0d225143b3684))


### 🐛 Bug fixes

- fix(tools): resolve profile image pins in audit ([98535dc](https://github.com/noonghunna/club-3090/commit/98535dc81453e54be03a1f5915bb2367ebab5c27))
- fix(tools): bump engine nightly profiles ([d1acde0](https://github.com/noonghunna/club-3090/commit/d1acde0b28eccb123338d2a9d94e4ef6ff75cc4b))
- fix(ci): keep vllm base arg in image metadata ([1abe65f](https://github.com/noonghunna/club-3090/commit/1abe65fe2810be594d6890ce0f26a3f0a554075f))
- fix(launch): persist estate source of truth ([52e4347](https://github.com/noonghunna/club-3090/commit/52e43470c6ee111dfa97be81e13e229ede715073))


### 📝 Documentation

- docs: document profile-sourced vllm pins ([86445be](https://github.com/noonghunna/club-3090/commit/86445be3e8c24ad829d45c4f1702a0bccf27e4dc))
- docs: document club vllm image pin ([2ae8303](https://github.com/noonghunna/club-3090/commit/2ae8303833497f20d4079a12226ca23c83f71337))
- docs: expand KV_MATH + add ADDING_MODELS workflow ([1f8aaa2](https://github.com/noonghunna/club-3090/commit/1f8aaa2acc72a7cff763fa81ae938d552fffffb2))
- docs(hardware): clarify 3090 stock TDP varies by board SKU ([0d59f94](https://github.com/noonghunna/club-3090/commit/0d59f949e472095e3ecb83ce133eb103d10588d9))


### 🧹 Maintenance

- chore(vllm): use club3090 image in composes ([aebc4f3](https://github.com/noonghunna/club-3090/commit/aebc4f321c3536943bfbd554d2c21ed6824742f9))
- chore(ci): build club vllm image ([e88a2a8](https://github.com/noonghunna/club-3090/commit/e88a2a8d21efd3556739fcb0fb1a26327b7d38cd))
- refactor(kv-calc): consume profile data ([9ccde62](https://github.com/noonghunna/club-3090/commit/9ccde62abe360bfb9170fc88102623dc5e87597e))


### 🧹 Other

- Revert "chore(vllm): use club3090 image in composes" ([c7c40bd](https://github.com/noonghunna/club-3090/commit/c7c40bdf1232ec2a2f8e5b1d98249df33026f46b))



[Pin: `git checkout v0.7.0`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.6.3...v0.7.0)
## v0.6.3 — 2026-05-14


### ✨ Features

- feat: unify dual-card composes with NVLink auto-detection ([e00626a](https://github.com/noonghunna/club-3090/commit/e00626a50e92fe44855c410b86ae3f33ace82f29))


### 🐛 Bug fixes

- fix(scripts): report.sh shows human-readable version via git describe ([0f0a9c8](https://github.com/noonghunna/club-3090/commit/0f0a9c84c513392d889dbf51d05c5edb1f4ba649))


### 📝 Documentation

- docs: cross-rig data — eddie 3090/3090Ti power-cap + alanspires 6×3090 VFIO ([e41323f](https://github.com/noonghunna/club-3090/commit/e41323ffa9c471c6f4d9b771bbb94ff784235342))


### 🧹 Other

- Merge PR #128: unify dual-card composes with NVLink auto-detection ([#128](https://github.com/noonghunna/club-3090/pull/128) by @noonghunna)



[Pin: `git checkout v0.6.3`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.6.2...v0.6.3)
## v0.6.2 — 2026-05-14


### 🐛 Bug fixes

- fix(launch): project TP greater than four ([98f0406](https://github.com/noonghunna/club-3090/commit/98f0406d0f265767b4a6712a1eba293b1e2dc889))



[Pin: `git checkout v0.6.2`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.6.1...v0.6.2)
## v0.6.1 — 2026-05-14


### ✨ Features

- feat(launch): add hardware-aware launcher ([5882bbe](https://github.com/noonghunna/club-3090/commit/5882bbef6f5ed7e8ceea450fa3a6b167a1bf4926))
- feat(tools): extend kv-calc.py to multi-model (Qwen 3.6 + Gemma 4 31B) ([0d48dac](https://github.com/noonghunna/club-3090/commit/0d48dac818ba889f74b74df1c454bb961a123c37))


### 📝 Documentation

- docs: update launch.sh references for v0.6.1 wizard flow ([e299e70](https://github.com/noonghunna/club-3090/commit/e299e70451c8d146214a6560e582d0e174dd0ebc))


### 🧹 Other

- Merge codex/v0.6.1-launch into master ([056dcb6](https://github.com/noonghunna/club-3090/commit/056dcb643914fee6169b02b89cb420b038c29b0f))



[Pin: `git checkout v0.6.1`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.6.0...v0.6.1)
## v0.6.0 — 2026-05-13


### ✨ Features

- feat(scripts): add hardware-aware setup picker ([12a33fb](https://github.com/noonghunna/club-3090/commit/12a33fbdd1b6422429521f887d9f21c2e3da793d))


### 🐛 Bug fixes

- fix(launch): exit cleanly on stdin EOF in wizard prompts ([e05f196](https://github.com/noonghunna/club-3090/commit/e05f1969bcf57547a17cd963a1f21435de80815b))



[Pin: `git checkout v0.6.0`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.5.4...v0.6.0)
## v0.5.4 — 2026-05-13


### 🐛 Bug fixes

- fix(scripts): make submit-bench issue-first ([22bf2e9](https://github.com/noonghunna/club-3090/commit/22bf2e9398c7907aae6b62809bde30e111e4a700))



[Pin: `git checkout v0.5.4`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.5.3...v0.5.4)
## v0.5.3 — 2026-05-13


### ✨ Features

- feat(scripts): add submit-bench flow ([ef77032](https://github.com/noonghunna/club-3090/commit/ef770322f43724f612a80393f547e5da218b5bf7))



[Pin: `git checkout v0.5.3`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.5.2...v0.5.3)
## v0.5.2 — 2026-05-13


### 🎯 New models + serving paths

- Add hardware-aware compose preflight ([2698552](https://github.com/noonghunna/club-3090/commit/26985527f75d8da2a32a8a2f985989d5dcf9e89a))



[Pin: `git checkout v0.5.2`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.5.1...v0.5.2)
## v0.5.1 — 2026-05-13


### 🐛 Bug fixes

- fix(qwen): PR #35936 overlay — sidecar pattern to resolve Genesis RO-mount conflict ([6617e1e](https://github.com/noonghunna/club-3090/commit/6617e1e090a6f52708aaf83821a92b612c4ad869))


### 📝 Documentation

- docs: clarify MODEL_DIR — second drive / HF cache / Windows-WSL ([1678ca0](https://github.com/noonghunna/club-3090/commit/1678ca0c8ba43ea09fad9073639a48337f2ff163))
- docs(upstream): correct stale vllm#40807 row + add #40798/#42215 row ([14ffe45](https://github.com/noonghunna/club-3090/commit/14ffe45667fb0aa292839be05ae3ad0d139d3a04))



[Pin: `git checkout v0.5.1`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.5.0...v0.5.1)
## v0.5.0 — 2026-05-12


### ✨ Features

- feat(qwen): ship froggeric chat-template fixes as default-on ([84498d4](https://github.com/noonghunna/club-3090/commit/84498d47aaf7a2fdb7c0203d53bb64414a64b6c1))
- feat(vllm): add PR #35936 required-tool fallback overlay ([28b16b5](https://github.com/noonghunna/club-3090/commit/28b16b5dc9d602a8e1c4b8d5496aa82cbca7f95d))
- feat(qwen-tq3): add CLUB3090_TQ_K1_SKIP_MTP layer-filter for PR #40914 K+1 dispatch ([6b2a7d5](https://github.com/noonghunna/club-3090/commit/6b2a7d553b6164bb4854e80fc0acdf8dcec18a87))


### 🎯 New models + serving paths

- compose(tq3-mtp-genesis): pin to Genesis v7.72.2 known-good vLLM nightly ([570fa71](https://github.com/noonghunna/club-3090/commit/570fa71240a12ab642693c0570851611e933f8c4))


### 📊 Benchmarks + cross-rig data

- bench(matrix): @ygafarov first heterogeneous Ampere + Blackwell eGPU dual ([1770931](https://github.com/noonghunna/club-3090/commit/1770931729a354bad319c8b58bdee143fe6ebce2))


### 📝 Documentation

- docs(dtype-matrix): more polish — RDNA naming, FP8 maturity caveats, AMD detection ([62b3b45](https://github.com/noonghunna/club-3090/commit/62b3b455a9ea5146cbf5576febd0c8b25a8c0fa1))
- docs(dtype-matrix): polish nuances + add Intel and AMD vendor sections ([3d4548c](https://github.com/noonghunna/club-3090/commit/3d4548c50422da07c16fcba2a59d6f42f268355b))
- docs(dtype-matrix): per-arch hardware accelerator matrix for compose optimization ([9c6d3cf](https://github.com/noonghunna/club-3090/commit/9c6d3cfba1de9d9079d6eafc9ff68c352cac7197))
- docs(faq): add 'INT8 PTH doesn't scale at concurrency — is that a bug?' ([df53287](https://github.com/noonghunna/club-3090/commit/df53287b1c26ec83be8a30eec24baf2bddc993eb))
- docs(tq3-mtp): writeup + charts for the Genesis-backed TQ3+MTP path ([c2b1c93](https://github.com/noonghunna/club-3090/commit/c2b1c93872f84fa9afa3bbe41360dc42be28c066))
- docs(qwen-tq3): close round-4 — #40914 not shippable, route to nomtp + Genesis ([9fba037](https://github.com/noonghunna/club-3090/commit/9fba03788e30151f9bf8c85f279260696954d094))
- docs(qwen-tq3): re-tombstone tq3-mtp.yml after round-3 MTP-skip validation ([063d3e9](https://github.com/noonghunna/club-3090/commit/063d3e943ce8da9cc69bd30c68b87426aca6202e))


### 🧹 Maintenance

- refactor(qwen): rename int8-tq3 → tq3-* family + add no-MTP + Genesis variants ([6182922](https://github.com/noonghunna/club-3090/commit/6182922225dfeee1c28084d1ff917bfd25539520))



[Pin: `git checkout v0.5.0`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.4.0...v0.5.0)
## v0.4.0 — 2026-05-11


### ✨ Features

- feat(rebench-report): close 9 gaps — TL;DR + rig + timings + reproducer + delta + discuss variant ([be7f9aa](https://github.com/noonghunna/club-3090/commit/be7f9aa143e9942bbc331e219542b529e4156512))
- feat(rebench): add REPORT.md synthesizer + container/boot/GPU captures ([18355f4](https://github.com/noonghunna/club-3090/commit/18355f41f68699d76dd50452b32d505119f399d0))
- feat(rebench): halve default soak to 10 sessions × 5 turns (~15-20 min) ([3406894](https://github.com/noonghunna/club-3090/commit/340689427f971dc16856b9d069ff32d4c280da28))
- feat(rebench): one-shot canonical 5-step bench orchestrator ([94a2522](https://github.com/noonghunna/club-3090/commit/94a2522417d514674db78c590c4b899bb3eb9d36))


### 🐛 Bug fixes

- fix(switch): GPU memory pre-flight + widen RUNNING_PATTERN ([4866913](https://github.com/noonghunna/club-3090/commit/4866913a10002e8a3e6d2a2df7e6fda07fb1f953))
- fix(rebench-report): parse aider upstream_per_exercise as dict (not list) ([7c4b310](https://github.com/noonghunna/club-3090/commit/7c4b310cca0c62a55a9603cdd31540763e82191a))


### 📊 Benchmarks + cross-rig data

- bench(head-to-head): matched-config rebench + Qwen INT8 PTH KV compose ([755e519](https://github.com/noonghunna/club-3090/commit/755e5199ffd029336000fbfb80dc342e42c8c6d5))


### 📝 Documentation

- docs(gemma-4-31b): document TQ3 Ampere FA2 head_dim wall + vendor #40108 overlay ([f8c7066](https://github.com/noonghunna/club-3090/commit/f8c706699ca8ae9630c7fda58e23a21183241175))
- docs(benchmarks): Qwen 3.6 27B vs Gemma 4 31B head-to-head on dual 3090 ([edda3b3](https://github.com/noonghunna/club-3090/commit/edda3b3ecac7d460b34081e307ffd843a414b83e))


### 🧹 Maintenance

- chore(composes): bump Qwen pins → 1acd67a7, drop obsolete patch_tolist_cudagraph ([16a1374](https://github.com/noonghunna/club-3090/commit/16a1374053f979363fe4634a73ddd9c90db6061c))
- chore(cliff): skip auto-regen bot commits in changelog parser ([a258e49](https://github.com/noonghunna/club-3090/commit/a258e496bf926892c3a33e6f2f5ee2efb87a9d71))



[Pin: `git checkout v0.4.0`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.3.3...v0.4.0)
## v0.3.3 — 2026-05-10


### 🧹 Maintenance

- chore(changelog): subject-only rendering (drop commit body verbosity) ([eeb946b](https://github.com/noonghunna/club-3090/commit/eeb946b0a7b90462a968c800ecceb2e519b0e7fd))



[Pin: `git checkout v0.3.3`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.3.2...v0.3.3)
## v0.3.2 — 2026-05-10


### ✨ Features

- feat(quality-test): auto-set BENCHLOCAL_HERMES_RESOLVE_LOCALHOST=1 for localhost URLs ([83bf73d](https://github.com/noonghunna/club-3090/commit/83bf73d3ec464f6a366c074a3d43f203ff1e3444))


### 🧹 Maintenance

- chore: trigger v0.3.2 release workflow (GitHub deduped previous tag push) ([255c743](https://github.com/noonghunna/club-3090/commit/255c743dff59149ef83a06a4e63b0e74153c61cb))
- chore(changelog): automate CHANGELOG + release notes from commits via cliff (Option A) ([64b0474](https://github.com/noonghunna/club-3090/commit/64b0474a628d5a91222446d90b4974b14ab3237f))



[Pin: `git checkout v0.3.2`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.3.1...v0.3.2)
## v0.3.1 — 2026-05-10


### 🐛 Bug fixes

- fix(soak-helper): capture `delta.reasoning` alongside `delta.reasoning_content` ([88eb67a](https://github.com/noonghunna/club-3090/commit/88eb67aa18263a5706268a06d66784987ec69069))


### 📝 Documentation

- docs(changelog): v0.3.1 entry for soak-helper delta.reasoning capture ([9db8b26](https://github.com/noonghunna/club-3090/commit/9db8b2603ca2e9638b533f76e9fbc1aa7bf936a3))



[Pin: `git checkout v0.3.1`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v0.3.0...v0.3.1)
## v0.3.0 — 2026-05-10


### ✨ Features

- feat(power-cap-sweep): --include-commit flag stamps club-3090 git SHA in report header (closes #112) ([7d91ac7](https://github.com/noonghunna/club-3090/commit/7d91ac75e05eb01c81a30b35d2aa1290d5dc4b7f))
- feat(qwen3.6-27b): thinking OFF by default across all 21 composes ([29d17ed](https://github.com/noonghunna/club-3090/commit/29d17ed82d5a62191e96284f557686c4baa1cea7))
- feat(setup): interactive MODEL_DIR prompt for fresh TTY users ([3909c2d](https://github.com/noonghunna/club-3090/commit/3909c2d6b826d40a382fe3554cfe068a81145657))


### 🐛 Bug fixes

- fix(qwen3.6-27b): use --default-chat-template-kwargs (not --chat-template-kwargs) ([534d29f](https://github.com/noonghunna/club-3090/commit/534d29f1b1da3ff5f34035e01b496db1c565a81b))
- fix: 4 stale refs missed in 2026-05-10 reorg push (caught by RobH589 #116) ([cf7f195](https://github.com/noonghunna/club-3090/commit/cf7f1959fdd002b4c354aa14ec5ae983aa971c9d))


### 📝 Documentation

- docs(benchmarks): aider-polyglot-30 — Qwen 27B 20/30 (66.7%) > Gemma 4 31B 17/30 (56.7%) ([e08988e](https://github.com/noonghunna/club-3090/commit/e08988e6140ea5afc7be46434f0bd1aa0c02096d))
- docs(recipes): use \$MODEL_DIR placeholder + sensible cross-rig default ([cc3a717](https://github.com/noonghunna/club-3090/commit/cc3a7175243abe43f21a1eb69ca0015b5a10f7f8))
- docs: use \$MODEL_DIR placeholder, not the dev rig's /mnt/models/huggingface/ ([fbf3431](https://github.com/noonghunna/club-3090/commit/fbf343129ccc48d242178a0d5b57d6def7d5651d))


### 🧹 Other

- release: SemVer adoption + v0.3.0 changelog entry ([7080f1f](https://github.com/noonghunna/club-3090/commit/7080f1f89b674a0cc5becd361623a0ab6abdd53d))



[Pin: `git checkout v0.3.0`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v2026.05.10...v0.3.0)
## v2026.05.10 — 2026-05-10


### ✨ Features

- feat(gemma-4-31b): INT8 PTH KV unblocks 262K + AWQ + DFlash compose family ([403b16f](https://github.com/noonghunna/club-3090/commit/403b16f303253430bf58b606da7490d8253b7ef7))


### 🎯 New models + serving paths

- compose: parametrize VLLM_ENFORCE_EAGER, KV_CACHE_DTYPE, P40/P82/PN54 across all variants (#110) ([#110](https://github.com/noonghunna/club-3090/pull/110) by @easel)
- composes: refresh Quality lines with --full sandboxed (8-pack) results ([9dea0eb](https://github.com/noonghunna/club-3090/commit/9dea0ebb7beb72845a6264664bf5da1bc5c65b9f))
- composes: add --full Quality lines on Qwen3.6-27B + Gemma 4 31B duals ([26ff0e5](https://github.com/noonghunna/club-3090/commit/26ff0e58643dae75904f4b1ea4705a5fa32007bc))


### 🐛 Bug fixes

- fix: BIND_HOST opt-in + localhost script fixes (#109) ([#109](https://github.com/noonghunna/club-3090/pull/109) by @easel)


### 📝 Documentation

- docs: WSL2 budget formula + Cliff 3 (DeltaNet SSM-state non-cacheable) ([6e12700](https://github.com/noonghunna/club-3090/commit/6e12700f9a91c92c3c28c35d25be798745016ee0))


### 🛠️ Scripts + tooling

- quality-test.sh: --sandboxed-only passthrough ([7020d96](https://github.com/noonghunna/club-3090/commit/7020d965bdbcc1b4d3bfeadd0c85b030488c1dfd))
- quality-test.sh: --help, --pack passthrough, align with benchlocal-cli v0.5 ([1be02d2](https://github.com/noonghunna/club-3090/commit/1be02d22719e78913470e6ee98a17a2b2d46f152))
- ci: replace Release Drafter with git-cliff for commit-based release notes ([7002e6b](https://github.com/noonghunna/club-3090/commit/7002e6b550fe357859e34bb6ff15d1e9ae493de4))


### 🧹 Other

- reorg: services/ consolidation + gpu-mode under git + ComfyUI + pin tracker + path updates ([00366a5](https://github.com/noonghunna/club-3090/commit/00366a58d761ca797581c1411b06c4f6ab98654c))
- encourage-soak: template dropdown + script ergonomics + report reminder + Notes convention ([c298b60](https://github.com/noonghunna/club-3090/commit/c298b60f762309d3829a0ce3a45b17ac3ca9224a))
- BENCHMARKS: add @ygafarov Strix-Halo + oculink-eGPU x4-PCIe single-3090 row (#113) ([a589058](https://github.com/noonghunna/club-3090/commit/a5890587610404d69819512a32290d87deeb5460))



[Pin: `git checkout v2026.05.10`] · [Full diff](https://github.com/noonghunna/club-3090/compare/v2026.05.09...v2026.05.10)
## v2026.05.09 — 2026-05-09


### ⚠️ Cliffs, gotchas, regressions

- Merge v7.69-cliff2-test: ship Cliff 2 closure recipes (Balanced MTP + Max-context) ([15b84df](https://github.com/noonghunna/club-3090/commit/15b84df717d1a7b193946a1cb8de0945d7f2693d))
- v7.69 + #35975 + Codex P103 gate fix — Cliff 2 closure recipes ([f6613c8](https://github.com/noonghunna/club-3090/commit/f6613c869abd6260825cf3fde17956a867316d43))
- docs + charts: v7.66 + Cliff 1 mech B closed across all 4 TQ3 composes ([ae4846f](https://github.com/noonghunna/club-3090/commit/ae4846fd6345ee414b933a6aa272ee1fdf8c3adc))
- PN30 dst-shaped temp fix: close DS conv state regression class on long-text ([9af1a52](https://github.com/noonghunna/club-3090/commit/9af1a5245adf6ac740b9e2baa7ac515379e158f4))
- PN25 v3: close Cliff 1 mech B (club-3090#16) on long-text via setup-time Genesis backport ([a62ad78](https://github.com/noonghunna/club-3090/commit/a62ad78a4e8a7ce62aec4d11ae967382b188df46))
- walk back: Cliff 1 mech B reproduces on real IDE-agent prompts (club-3090#16) ([b62b6b1](https://github.com/noonghunna/club-3090/commit/b62b6b1de46cab098718d6f671b12480d687ab4c))
- Ship verified Cliff 1 closure on long-text 205K + long-vision 192K ([287de1c](https://github.com/noonghunna/club-3090/commit/287de1c6e8f1500dd9144dce9a9b9fbf601d7d67))
- Cliff 1 P104 + P101 anchor fix outcomes (built on cliff1-fa-clamp branch) ([e6570a7](https://github.com/noonghunna/club-3090/commit/e6570a7d1139c6bf61c91569f55a4844971a7ecb))
- Cliff 1 dual-mechanism: P101+P103 cross-rig test reveals FFN buffer cliff ([573a377](https://github.com/noonghunna/club-3090/commit/573a377690a760f7fed29b80b7633b5526af2095))
- Cliff 1 root cause revised: FA2 softmax_lse sized by max_seqlen ([2d6b69d](https://github.com/noonghunna/club-3090/commit/2d6b69dd50eaa4764f12d6c30cc7d91c4355881b))


### ✨ Features

- feat(preflight): compose-dependency + HF_TOKEN + KV-format checks (#37, #47, #219) ([b6c8708](https://github.com/noonghunna/club-3090/commit/b6c870820978fe641771e631700e11e17bf475d2))
- feat(tools): kv-calc.py — predict per-card VRAM budget for Qwen3.6-27B (#226) ([4e89c6a](https://github.com/noonghunna/club-3090/commit/4e89c6aa40856126ab5803159ad69211a03a1a9a))
- feat(bounded-thinking): Phase 3 grammar A/B complete; DeepSeek scratchpad is the new recommended grammar ([b956c85](https://github.com/noonghunna/club-3090/commit/b956c85477f0f4e9dd00e20c0dfc68bc30ad20b4))
- feat(report.sh): --stress + --soak flags, --full now the canonical "everything" pass ([8a29b95](https://github.com/noonghunna/club-3090/commit/8a29b95da10f7ab45151fba866aa526f2a1796c2))
- feat(qwen3.6-27b/vllm): add dual4 + dual4-dflash composes (TP=4, 4×3090, #44) ([#44](https://github.com/noonghunna/club-3090/pull/44) by @Whamp)
- feat(grammar-eval): land harness for Holiday tagline grammar A/B ([7be8ecc](https://github.com/noonghunna/club-3090/commit/7be8ecc9e0977ae2d27397811a1cbb24b51b4b68))
- feat(soak-test): continuous-mode v2 fixtures + reproduces Cliff 2 at 25K accumulated context ([8d5bfd8](https://github.com/noonghunna/club-3090/commit/8d5bfd85f99a6a7c2c91cf70241c1e46c56ae957))
- feat(scripts): add soak-test.sh — runtime VRAM accretion validation (closes gap from #41) ([563a39e](https://github.com/noonghunna/club-3090/commit/563a39e0d3e7acbc15bb3c743d81cdcbef442dd4))
- feat: detect repo drift in preflight + add scripts/update.sh ([43fe2a4](https://github.com/noonghunna/club-3090/commit/43fe2a4e20ac8eb5c3f406f25ca0588a0989fb21))
- feat(launch/switch): register vllm/dual-nvlink as a known variant ([75de7c9](https://github.com/noonghunna/club-3090/commit/75de7c95dbcbc0c2c87f8130960340d204956224))
- feat(preflight): warn when Genesis tree out of sync with setup.sh's declared pin ([d552ed9](https://github.com/noonghunna/club-3090/commit/d552ed92166a07ce5fc3c289d9b42745f8479da5))
- feat(scripts/report.sh): capture per-GPU PCIe lane width + Gen + bus ID ([535be29](https://github.com/noonghunna/club-3090/commit/535be29df4520095bdb07cfe093031ca076f65b2))
- feat(scripts/report.sh): capture container-internal Python/CUDA versions ([e491e07](https://github.com/noonghunna/club-3090/commit/e491e07972275e2155421182a7f2df830170cd21))
- feat(scripts): add report.sh — paste-ready triage report ([31982f0](https://github.com/noonghunna/club-3090/commit/31982f0e6b029498b7244273217d448250aeeb20))
- push long-text/bounded-thinking back to 185K + 0.975; long-vision stays 140K + 0.95 ([df91d64](https://github.com/noonghunna/club-3090/commit/df91d641c443e1dd308cde8cc06175655dcfcd8e))
- feat(vllm): structured-CoT bounded-thinking compose (cross-rig port) ([3d151b9](https://github.com/noonghunna/club-3090/commit/3d151b9edc2621cfa45a7f38f8f5c05962fe924e))
- Push verified ceilings: long-text 218K, long-vision 198K ([f3e5b52](https://github.com/noonghunna/club-3090/commit/f3e5b5217c93d1476062caf5c94c1bfe93029dba))
- Verify 256K single-prompt prefill on dual.yml (Sandermage cross-rig) ([5270d94](https://github.com/noonghunna/club-3090/commit/5270d9400adfa07687ebd1beaa24cb812b10f1ea))


### 🎯 New models + serving paths

- composes: formalize Status enum + Caveats field (100% coverage) ([e1137d6](https://github.com/noonghunna/club-3090/commit/e1137d6889bbb6c7d7ddb584c942488f654c3b86))
- composes: rename dual4 → multi4 to align topology prefix with MULTI_CARD.md framing ([d33e6f8](https://github.com/noonghunna/club-3090/commit/d33e6f82da84e3e402bd2f1e0904c56cbcdb656a))
- composes: complete profile-schema header rollout (8 more composes) ([fca643d](https://github.com/noonghunna/club-3090/commit/fca643d6437bfc79522da57278a7001d1b268887))
- compose: extend VLLM_ENFORCE_EAGER hook to dual / dual-nvlink / dual4 + HARDWARE.md docs ([5ec40c6](https://github.com/noonghunna/club-3090/commit/5ec40c65ffd47b805026a9e65023a3bfe0a1dbd4))
- compose: VLLM_ENFORCE_EAGER env hook + WSL2 .env docs ([#99](https://github.com/noonghunna/club-3090/pull/99) by @easel)
- Add dual-nvlink-dflash-noviz compose variant (NVLink + DFlash N=5, 200K ctx, no vision) ([63ab224](https://github.com/noonghunna/club-3090/commit/63ab224c570516f158eee13cde22afcd9a4ba944))
- Add docker-compose.dual-nvlink-dflash.yml (#92) ([#92](https://github.com/noonghunna/club-3090/pull/92) by @danbedford)
- composes: PYTORCH_CUDA_ALLOC_CONF env-override knob + WSL2 boot-crash docs (#84) ([#84](https://github.com/noonghunna/club-3090/pull/84) by @easel)
- Add Gemma 4 + DFlash compose (vLLM PR #41703 Codex-rebased overlay) (#81) ([#81](https://github.com/noonghunna/club-3090/pull/81) by @noonghunna)
- composes: env-override knobs MAX_MODEL_LEN + GPU_MEMORY_UTILIZATION (#79) ([#79](https://github.com/noonghunna/club-3090/pull/79) by @noonghunna)
- add Gemma 4 31B + Google MTP drafter (first Ampere data) (#68) ([#68](https://github.com/noonghunna/club-3090/pull/68) by @noonghunna)
- Add dual NVLINK Docker Compose setup for Qwen3.6-27B ([1350450](https://github.com/noonghunna/club-3090/commit/135045002464a440381c8f77d4385a0045e754de))
- Add llama.cpp compose + perf chart + Q3_K_XL bench data ([39692c9](https://github.com/noonghunna/club-3090/commit/39692c98e5f2ea963da8274815b24fb3da70ecfd))
- Add long-vision + long-text composes (formalize R3' / R3''' bench rows) ([b641719](https://github.com/noonghunna/club-3090/commit/b641719eb815de978f01ddb6c2caed978cb45408))


### 🐛 Bug fixes

- fix: verify-full.sh broken pipe + llama-cpp DISABLE_THINKING env hook ([8f103f3](https://github.com/noonghunna/club-3090/commit/8f103f33ec8ed42c293e12b6bb39e73f736b1946))
- fix(preflight): catch missing llama.cpp GGUF before container boot (#63) ([#63](https://github.com/noonghunna/club-3090/pull/63) by @noonghunna)
- fix: remove thinking prompt from Carnice chat template + JSON tool format ([3729144](https://github.com/noonghunna/club-3090/commit/3729144107c587be2576171bad039aa453afceb2))
- fix: missing pipe in DUAL_CARD table row ([a28ba38](https://github.com/noonghunna/club-3090/commit/a28ba387dcdf3b6bb735872109e86062a5a5eb71))
- fix(soak): flag silent-empty turns (HTTP 200 + 0 tokens) as warnings ([f32d8a6](https://github.com/noonghunna/club-3090/commit/f32d8a69721059537557dcaeaaf522732798339a))
- fix: 3 issues from community feedback ([2f8ed19](https://github.com/noonghunna/club-3090/commit/2f8ed197ce8fb1ec1ce91a1d7647847bbca996f8))
- fix(soak-test, switch): calibration + boot-progress UX from first cross-rig runs ([8e9cf70](https://github.com/noonghunna/club-3090/commit/8e9cf70d9997d04336ead0eb7664cac608b64b3c))
- fix(dual-nvlink): rename to avoid collision + vendored Marlin path ([147f2e3](https://github.com/noonghunna/club-3090/commit/147f2e33ee8e8c021ab70f000928927326e9b4e8))
- fix(default compose): swap P65 (cudagraph workaround) → P67 (proper Triton kernel fix) ([620d918](https://github.com/noonghunna/club-3090/commit/620d918db3c0a346ae245ffaf78b7ecf0d789f70))
- fix(long-text-no-mtp): drop P65 + P85 — missed in a26e30b ([22e6549](https://github.com/noonghunna/club-3090/commit/22e654989b5658b09af989508584ce635826398e))
- fix(composes): drop GENESIS_ENABLE_P65 + P85 — out of sync with v7.69 dispatcher v2 ([a26e30b](https://github.com/noonghunna/club-3090/commit/a26e30b279d5dacbdaf7489c5dfb8d1203219166))
- fix(setup.sh): auto-clone vllm-src Marlin patched fork (was manual step) ([2e934ad](https://github.com/noonghunna/club-3090/commit/2e934ad18ad70d98e2e314ca3a96759935393949))
- fix(docs): replace dead luce-spec/llama-cpp-dflash links with Luce-Org/lucebox-hub ([e9c658c](https://github.com/noonghunna/club-3090/commit/e9c658cbc6ca453e9502b20a6fa6e682b2e5f752))
- fix(scripts): register vllm/long-text-no-mtp in switch.sh + launch.sh ([1f09a05](https://github.com/noonghunna/club-3090/commit/1f09a059d59138288bf630881c6870dacc91d9ed))
- fix(dflash): close the docs+setup gap that hit @lolren on club-3090#18 ([eb54cf4](https://github.com/noonghunna/club-3090/commit/eb54cf4e68da057a884b8d5fa8d26c8fd04969a0))
- fix(verify): drop tail buffer on Genesis check 2 anchor (refines 95b0905) ([f2c1433](https://github.com/noonghunna/club-3090/commit/f2c143326ea710cd1b724407dff5367930f14534))
- fix(verify+docs): close two items from troymroberts cross-rig validation (#25) ([95b0905](https://github.com/noonghunna/club-3090/commit/95b090567c646e7bbfcada5a05ec622dc9936ca2))
- fix(launch): pass per-variant URL + CONTAINER to verify-full.sh (#20) ([77ca576](https://github.com/noonghunna/club-3090/commit/77ca5767f5bf27ba0774edf1ded301c826d66277))
- fix(docs): bump curl smoke-test max_tokens 30 → 200 (#14) ([2f8bade](https://github.com/noonghunna/club-3090/commit/2f8bade82c53886f2525e0a5cb0efe748b1135e9))
- fix(vllm): fail fast when Genesis patches volume is empty (#13) ([0df8f74](https://github.com/noonghunna/club-3090/commit/0df8f743192809dbdcda942887b625b0f48699f2))
- fix: address open issues #1, #4, #7 ([ebacba1](https://github.com/noonghunna/club-3090/commit/ebacba1efd052fa3eda7ee3b05f2f8479a2fb2ff))


### 📊 Benchmarks + cross-rig data

- results: re-bench dual.yml + dual-dflash + dual-dflash-noviz on v0.20 ([0bdcb69](https://github.com/noonghunna/club-3090/commit/0bdcb69fa3e446442c8bc744dcb588e1697cba55))
- results: dual-turbo re-bench with corrected env vars (PN22 / PN26 naming fix) ([077228e](https://github.com/noonghunna/club-3090/commit/077228e81b06aebca3401fc03456f4a3eb55e227))


### 📝 Documentation

- docs: add Discord invite to README + FAQ + issue template ([c18257f](https://github.com/noonghunna/club-3090/commit/c18257f4399e0e7a5ee6bc38e80b10ff97ed2a8e))
- docs: refresh 4090 cross-rig knee with @laurimyllari's richer 38-cap sweep ([20ca297](https://github.com/noonghunna/club-3090/commit/20ca29737897df1d52c7c31ad6674a9d08aca54e))
- AGENTS.md: codify why patches/cache stay engine-level (not under a topology) ([9fbce96](https://github.com/noonghunna/club-3090/commit/9fbce961202965aeccd6851799b7abbdc806d355))
- AGENTS.md: capture compose naming + profile schema + experimental-compose conventions ([62e636c](https://github.com/noonghunna/club-3090/commit/62e636c0525156e6a98faaf318ce50c85a44de6b))
- docs+composes: align Gemma 4 compose names to Qwen's <topology>-<feature>.yml convention ([fe86b48](https://github.com/noonghunna/club-3090/commit/fe86b48c2134df8b333ff8445f40a7c6205aad0b))
- docs: surface Gemma 4 31B + add at-a-glance profile schemas to canonical composes ([4d7356a](https://github.com/noonghunna/club-3090/commit/4d7356aac69fbe46e87cf44083ee84965287ca19))
- docs: add Community projects section pointing at VykosX/club-3090-server ([cd48764](https://github.com/noonghunna/club-3090/commit/cd487648c9bc42c9807ec458b09e21d2ce238a5e))
- docs: laptop EC-managed power + TQ3 vs fp8 KV naming-trap; verify-stress: auto-bump curl timeout under VLLM_ENFORCE_EAGER ([fe23eff](https://github.com/noonghunna/club-3090/commit/fe23eff8f0dcac9647dffa198959b89e42e9fe33))
- docs + compose: ship Phase 2 INT8 PTH validation results — 262K Gemma 4 unblocked ([1e1886a](https://github.com/noonghunna/club-3090/commit/1e1886a3a95825f387bcc33badba3a52409e7778))
- docs(hardware): add Qwen3.6-35B-A3B (MoE) 3090 power-cap charts + comparison ([ec27d75](https://github.com/noonghunna/club-3090/commit/ec27d7594eadcad6a343fe4b4e3246f195b87eef))
- docs(img): reposition freq-cap chart annotations to clear right margin ([2f7eb44](https://github.com/noonghunna/club-3090/commit/2f7eb44a15b1383e90cfd8b8245193a9363cd255))
- docs(hardware): add 5090 clock-lock chart + Blackwell freq-cap section ([119a5fa](https://github.com/noonghunna/club-3090/commit/119a5fa00db659ac5283540d70cea65257c4cbaa))
- docs(hardware): regen 3090 power-cap charts with SM clock + plateau evidence ([9f77be7](https://github.com/noonghunna/club-3090/commit/9f77be791bced574965276d8271eaa28dc58f5a9))
- docs(hardware): reconcile 230W vs 290W vs 330W sweet-spot story ([a7a1d59](https://github.com/noonghunna/club-3090/commit/a7a1d591d5154fb8c0822738ff66536f85ae9fb0))
- docs(hardware): @apnar prefill-heavy 5090 sweep — proves per-workload power ceiling ([d5ef8c8](https://github.com/noonghunna/club-3090/commit/d5ef8c89d09c35b37ce10b6a85db63d374ebcf17))
- docs(hardware): correct 3090 cooling class — air, not water ([1f94478](https://github.com/noonghunna/club-3090/commit/1f94478179f9fe4d1daff644a1cf1eb5f06cc0cc))
- docs(hardware): embed 3090 + Qwen3.6 + llama.cpp power-cap chart ([42afdbb](https://github.com/noonghunna/club-3090/commit/42afdbbff8ac552f716c9d61383b9a80e9f8280b))
- docs(hardware): embed 4090 + Qwen3.6 + llama.cpp power-cap chart ([e70258c](https://github.com/noonghunna/club-3090/commit/e70258c47f6a134f5f4f503a06e074f1a7d54758))
- docs(hardware): embed 5090 + Gemma 4 power-cap efficiency chart ([8b1d51a](https://github.com/noonghunna/club-3090/commit/8b1d51ab3c5b4d976cea1f1c5c74ba8c1f3b4a42))
- docs(engines): more honest vLLM GGUF status ([2d9aa14](https://github.com/noonghunna/club-3090/commit/2d9aa1483ccdc446a6e3609e86eb4010c08474fe))
- docs(engines): fix 12 corrupted table separators from ik_llama.cpp column add ([8f5b924](https://github.com/noonghunna/club-3090/commit/8f5b92491a44e06873c9c8a252b6602589550043))
- docs(engines): add ik_llama.cpp as 5th column to comparison matrix ([0959206](https://github.com/noonghunna/club-3090/commit/09592065f5261f17d55efc2e053690552d148fbb))
- docs(hardware): add 5090 + Gemma 4 + MTP cross-rig anchor rows (apnar disc #86) ([bef5701](https://github.com/noonghunna/club-3090/commit/bef57012a725fe8c5f0975ff531508826c5eb45e))
- docs: add INFERENCE_ENGINES.md feature matrix (vLLM/llama.cpp/SGLang/ktransformers) ([dfceccb](https://github.com/noonghunna/club-3090/commit/dfceccbf5577c8fb44d1a746b2808803ca659a46))
- docs: codify canonical power-cap-sweep command for cross-rig anchors ([886b619](https://github.com/noonghunna/club-3090/commit/886b619cc45d3a5f26adeebb3ec78508ce856388))
- docs: BENCHMARKS rows + CHANGELOG entry for danbedford NVLink+DFlash variants ([b893d60](https://github.com/noonghunna/club-3090/commit/b893d60f43a02aea8b4032003004d855eb97980e))
- docs(benchmarks): @apnar 5090 Gemma 4 MTP + DFlash rows (disc #67) ([98b0601](https://github.com/noonghunna/club-3090/commit/98b0601b6888b86116312f2b9df38e9f871b7521))
- docs(benchmarks): three cross-rig rows from 2026-05-07 reports ([76aacdc](https://github.com/noonghunna/club-3090/commit/76aacdc22043e224e6a080f23dccad4146d01cf5))
- docs(benchmarks): add @aaronlockhartdev patched-P2P driver row (#91, disc #70) ([4eea837](https://github.com/noonghunna/club-3090/commit/4eea837da808bf7f6bfd2c944bc7c19fecb79726))
- docs(upstream): note we filed cross-rig validation on vLLM PR #40391 ([e46f1e8](https://github.com/noonghunna/club-3090/commit/e46f1e8e03de6b0d882a95581fd73163594796d6))
- docs(gemma-4): int8_per_token_head on Ampere — Codex investigation verdict ([1c2c156](https://github.com/noonghunna/club-3090/commit/1c2c156003550b5b1b004c329461f7d7ba2588bb))
- docs: surface host-build contributor flow + power-cap-sweep in README + CONTRIBUTING ([9aa6cb2](https://github.com/noonghunna/club-3090/commit/9aa6cb2b0e93c8b45d33b00b368532d7055086ca))
- docs(benchmarks): add @lamentofhighborne 1× 3090 llama.cpp MTP row (#85) ([68dbfaf](https://github.com/noonghunna/club-3090/commit/68dbfafe94148806a97025c1758bd6864454c1af))
- docs(hardware): add @apnar's 5090 power-cap anchor + compute-saturation note ([60d4df6](https://github.com/noonghunna/club-3090/commit/60d4df6ce7a960c7ff6a38c78c6be85a55e4608c))
- docs(upstream): correct Gemma 4 per-token-head KV row — upstream PR exists ([eb9f955](https://github.com/noonghunna/club-3090/commit/eb9f9552832931d4cc5e2bdd0a9d21f18f739e80))
- docs(gemma-4): document fp8 + int8 KV exploration on Ampere — both blocked ([bb07eb5](https://github.com/noonghunna/club-3090/commit/bb07eb59aec1c70f1748a43be51acbaccc1e2364))
- docs(gemma-4): empirical ctx ceilings + PR #41745 merge status ([1038e5f](https://github.com/noonghunna/club-3090/commit/1038e5fc77f72f28c0900cf53a947e90f008b002))
- docs(power): add cooling caveat — 388W stock requires liquid cooling ([b15c5e1](https://github.com/noonghunna/club-3090/commit/b15c5e1f33bee67ed17c9301e630f54af6d81827))
- docs(power): revise default cap 230W → 330W per @syangsao cross-rig data ([2fe017f](https://github.com/noonghunna/club-3090/commit/2fe017f88dee7036184c6ee0e048c91c59754cea))
- docs(benchmarks): correct V100 row VRAM 14.6→15.6 GB/card per @efschu ([d7bffec](https://github.com/noonghunna/club-3090/commit/d7bffeccb74e330f070cf3461019a387b6e766ff))
- docs(benchmarks): add @efschu 2× Tesla V100 16GB row (first sm_70 Volta data) ([9212c60](https://github.com/noonghunna/club-3090/commit/9212c606e07c0cb4f52ea5bcf259e987cb184630))
- docs(benchmarks): @danbedford 2× 3090 cross-rig matrix (6 benches, controlled PCIe vs NVLink) ([6e57215](https://github.com/noonghunna/club-3090/commit/6e572156883fe2d5a291922307346b526b930525))
- docs(benchmarks): add @laurimyllari 4090 single-card vllm/long-text row ([461c4d4](https://github.com/noonghunna/club-3090/commit/461c4d4d3d9cadbd88ad6bd39437958238ff7c62))
- docs(benchmarks): add @lolren 2× 3090 + Ryzen 5950X cross-rig rows (3 variants) ([34a2348](https://github.com/noonghunna/club-3090/commit/34a23486c4bc10b1a54c6eccdc6a793ddeff1fe7))
- docs(benchmarks): add @apriori dual-dflash row (EPYC 7302P + Arch + 2× 3090) ([344e595](https://github.com/noonghunna/club-3090/commit/344e595cb915f2168d48b26492624c5c555c4832))
- docs(upstream): track llama.cpp MTP PR #22673 + non-adoption rationale (#64) ([#64](https://github.com/noonghunna/club-3090/pull/64) by @noonghunna)
- docs(contributing): clarify issues-vs-discussions routing (#61) ([#61](https://github.com/noonghunna/club-3090/pull/61) by @noonghunna)
- docs: add Carnice BF16MTP to DUAL_CARD, vllm README, and CHANGELOG ([fbd3531](https://github.com/noonghunna/club-3090/commit/fbd3531960894e4f1dac1c29e55fdd99224c4f6c))
- docs(runtimes): tighten Proxmox section — native venv works (#49) ([a51202c](https://github.com/noonghunna/club-3090/commit/a51202c7b32e755afa2739d35574efa41fbcf17c))
- docs(hardware): note SM86 structural ~70% TG drop at 131K (cross-rig) ([eb5cd70](https://github.com/noonghunna/club-3090/commit/eb5cd708c3899953ecd9bb9852bd5825609b0799))
- docs: capture environmental footnotes — WSL2 TDR + Proxmox uvloop (#49, #50) ([224ca71](https://github.com/noonghunna/club-3090/commit/224ca71b1910d5ca4eb8f2379aa353c4ce0f3156))
- docs(cliffs): add rig-class caveat — "known good" is rig-specific (#49) ([53d5c6b](https://github.com/noonghunna/club-3090/commit/53d5c6b02f4dac7fab16f53aee37391ca77bc67c))
- docs(multi-card): topology-aware pair selection on awkward GPU counts (#49) ([8e60539](https://github.com/noonghunna/club-3090/commit/8e605397e05f00ee6eca2c825e49e6b2a02a7250))
- docs(benchmarks): walk back PFlash "shippable" framing — TTFT + NIAH ≠ full validation (#230, #231) ([ccac1ff](https://github.com/noonghunna/club-3090/commit/ccac1ff1751ce5b80c1d635e6e88d0a8294b0a6e))
- docs(benchmarks): PFlash long-context bench — 131K source ceiling on 1× 3090 (#230) ([ebca0c8](https://github.com/noonghunna/club-3090/commit/ebca0c8921293b156fffc338c3aee708621384ac))
- docs(benchmarks): K8V4 result + P2P-CNS finding on lucebox-hub dual-GPU (#229) ([e78eaa1](https://github.com/noonghunna/club-3090/commit/e78eaa1148af83566753d2ffb1c66fc1cbf2aba5))
- docs(benchmarks): add lucebox-hub DFlash dual-GPU bench — no-op on 24 GB cards (#229) ([cb089e1](https://github.com/noonghunna/club-3090/commit/cb089e1e36c3cc37db45da630331d0a5bfa10215))
- docs(benchmarks): add @JusefPol's 2× 3090 + NVLink dual-nvlink row (#29, #31) ([017d0d2](https://github.com/noonghunna/club-3090/commit/017d0d2c2009ddd15ec50395e1947d52562e4747))
- docs(lucebox): record PRs #78 + #80 — dual-GPU PFlash + DFlash split shipped (May 2026) ([dec0f22](https://github.com/noonghunna/club-3090/commit/dec0f22dac051c96b38a31b7245020f0736025c9))
- docs(sglang): refresh per-engine + comparison pages — DFlash + MTP native upstream as of May 2026 ([ecc2d74](https://github.com/noonghunna/club-3090/commit/ecc2d747aea7d7c0e06aaacae4e6bbbfbe1c3b40))
- docs(structured-cot): soften Phase 3 framing per Codex v2-prompt validation ([011d4cc](https://github.com/noonghunna/club-3090/commit/011d4cc37111dcb857338684faaa57a7bce2a717))
- docs(cliffs/hardware): ground Cliff 2 + TQ3 explanations in published literature ([9b370f5](https://github.com/noonghunna/club-3090/commit/9b370f5ab1ab24bfc0ff6a5a96022cdc3e093606))
- docs: cross-reference TQ3→fp8 KV swap from CLIFFS, DUAL_CARD, dual-turbo.yml + CHANGELOG record (#47) ([129a4f4](https://github.com/noonghunna/club-3090/commit/129a4f42f4e3a1eab64abcdf6a444937b566c353))
- docs(hardware): 20 GB Ampere TP=2 needs fp8_e5m2 KV, not TQ3 (#47) ([124f08c](https://github.com/noonghunna/club-3090/commit/124f08c7ceaf400965622c3038e851a1d62365b4))
- docs(benchmarks): add @snoby's 2× 4090 dual-dflash-noviz row (#46) ([fc4c061](https://github.com/noonghunna/club-3090/commit/fc4c061be1298124e2c144c7143b308eee4f57bb))
- docs: align bug-report + FAQ + MULTI_CARD with report.sh --full / --soak ([b859630](https://github.com/noonghunna/club-3090/commit/b85963033aa62465a0c75a911d7ce394be52a098))
- docs(benchmarks): add Rig column for cross-rig contributions ([d8e7f73](https://github.com/noonghunna/club-3090/commit/d8e7f73eb281ea62771b38458429d14271bd6427))
- docs: add BENCHMARKS.md + extend grammar harness for full-bench mode ([9043678](https://github.com/noonghunna/club-3090/commit/90436788fbf54258e98a206da4260d6fb94fbb40))
- docs+gates: PR template, soak-continuous gate, Phase 2 grammar A/B ([85a6ea8](https://github.com/noonghunna/club-3090/commit/85a6ea8c48d44558476f09d2bc5a1a6c9fa93d2f))
- docs: UPSTREAM tracker + SINGLE_CARD polish — close the cliff-2b research thread ([451b9f3](https://github.com/noonghunna/club-3090/commit/451b9f37ab645fb2c9b3540017518a6ea32179df))
- docs: surface Cliff 2b multi-turn envelope + WHY TP=2 / llama.cpp escape ([04764c5](https://github.com/noonghunna/club-3090/commit/04764c5f28c3c21ad0621d9693356a3712918514))
- docs(UPSTREAM): sync 3 upstream changes + add next-week revisit queue ([4327fd3](https://github.com/noonghunna/club-3090/commit/4327fd30247c87bda7bac43672635356bfa2847e))
- docs: surface scripts/update.sh + repo-drift detection ([bca5a06](https://github.com/noonghunna/club-3090/commit/bca5a063c964b0029189c46aeec6cdce6323b72a))
- docs(vllm-marlin-pad/README): add sanity-check procedure before image-bump syncs ([1bb85fa](https://github.com/noonghunna/club-3090/commit/1bb85fadb82f92b80216a6a1dfa4eff87e25b03d))
- docs: add MULTI_CARD.md for 3+ GPU users (derived, untested locally) ([75a64a6](https://github.com/noonghunna/club-3090/commit/75a64a694e0789d2ec3ed74c64eda96c789a2de8))
- docs(FAQ): add WSL2 RAM-constraint failure mode to troubleshooting ([3bf7da7](https://github.com/noonghunna/club-3090/commit/3bf7da7501e3bc0e909cf7eeb55acb425697e7e3))
- docs: surface triage ladder at issue-filing time + add at-a-glance table ([f55b0a7](https://github.com/noonghunna/club-3090/commit/f55b0a734f259f031da18e7d823ef7eb44dbbca5))
- docs(FAQ): add 5-step triage ladder before symptom-matching ([9560efd](https://github.com/noonghunna/club-3090/commit/9560efd1f7616bd91b3d753d5ffc961ad3d3641d))
- docs: add PFlash integration feasibility memo (Codex audit, 2026-05-02) ([90a83a3](https://github.com/noonghunna/club-3090/commit/90a83a3fb5e4a931380a3920b30047ab062a23a2))
- docs: route bug + bench templates through scripts/report.sh ([b9a1305](https://github.com/noonghunna/club-3090/commit/b9a13056cc04a45f828c4d6e3809ce2f5c979c60))
- docs(dual-card): substrate refs from v7.65/v7.66 → v7.69 ([95b2c3b](https://github.com/noonghunna/club-3090/commit/95b2c3b1fa36600f88815b90d66eda86e20eb22c))
- docs: full sync to v7.69 + Cliff 2 60K closure recipes ([f8c9c36](https://github.com/noonghunna/club-3090/commit/f8c9c365e06ffdfa0d938b0e7c6f6557a8e8f1f1))
- docs(UPSTREAM): track Pflash (Luce-Org prefill accelerator) — flagged by @troymroberts (#25) ([e0e1752](https://github.com/noonghunna/club-3090/commit/e0e1752b3a0299671a4c5fec610fa3e321caed95))
- docs(CLIFFS): note v7.68 cross-rig test outcome — 3 regressions, master stays on v7.66 ([ae1b92f](https://github.com/noonghunna/club-3090/commit/ae1b92fef33b3873464b45cfab30a73733064621))
- docs: Genesis #14/#15 fixes shipped on Sandermage dev (P38B/P15B/PN25 pending v7.65) ([60d7b02](https://github.com/noonghunna/club-3090/commit/60d7b02c55ae3c4b85d65977508068ab2e25ed27))
- docs(upstream): refresh tracker for v0.20 blockers, P38/FA varlen filings, v7.64 closures ([f633fdb](https://github.com/noonghunna/club-3090/commit/f633fdbe17d91ee6c56af3d7d20ea7e11e337bac))
- docs+composes: refresh long-text/long-vision/bounded-thinking headers + max_tokens guidance ([cc4f083](https://github.com/noonghunna/club-3090/commit/cc4f0835e6b0214b5775ffd3bb638a0b6e8cf0d7))
- docs + bounded-thinking: roll new context defaults across user-facing surfaces ([d803278](https://github.com/noonghunna/club-3090/commit/d803278ebc78028a58172a6a9cfc976c7bbbc0ea))
- docs(compose): document Cliff 1 mech B real-workload gap + escape hatches (#16) ([6bff99a](https://github.com/noonghunna/club-3090/commit/6bff99a3f2a2bc17caaf72c7e23b465799094d27))
- charts: add tweet-asset variant (single-card vLLM only, 2 bars) ([f754669](https://github.com/noonghunna/club-3090/commit/f754669562ea2be8f83215423a112b2f4b0af433))
- charts: combined width 18 + 2-line group labels + dual VRAM title says vLLM ([24c8a62](https://github.com/noonghunna/club-3090/commit/24c8a629fd7c632286ba99e8f5b8f166b41f9012))
- charts: fix layout overlap with Luce DFlash 7th bar ([1ce7dc4](https://github.com/noonghunna/club-3090/commit/1ce7dc4512a292c906c5f85df27e7851f879369f))
- docs+charts: add Luce DFlash bench + watch entry; cautions in single-card chart ([cf71feb](https://github.com/noonghunna/club-3090/commit/cf71feb3e809cf618930959c3f5a6198a81c4cbc))
- docs: demote 48K/tools-text/minimal to fallback; lead with long-* + llama.cpp ([48f93e5](https://github.com/noonghunna/club-3090/commit/48f93e550fc3232783b516e6d22bf484defb6f5b))
- docs: fix stale chart ref in HARDWARE.md + delete obsolete vram-budget.svg ([cc02699](https://github.com/noonghunna/club-3090/commit/cc026993da6b2bfb3dd3a2322970317524f6399d))
- docs: catch remaining stale 192K/205K refs in long-text.yml header ([f00f279](https://github.com/noonghunna/club-3090/commit/f00f279d381885e979b0e3e46428df5c40171fd8))
- docs: final cleanup pass on stale 192K/205K refs ([a1fc225](https://github.com/noonghunna/club-3090/commit/a1fc22556a26c7dbbdfe8995364361ccbb93a5ff))
- docs+scripts+charts: propagate new ceilings (long-vision 198K, long-text 218K) ([427d2f8](https://github.com/noonghunna/club-3090/commit/427d2f8aa9f47931ea2a5258b59936f32b1bb7fe))
- docs: record verified ceilings and bisection in CLIFFS + CHANGELOG ([26e5f65](https://github.com/noonghunna/club-3090/commit/26e5f65975eea982ae2babec8a2cbfb32e05ae5a))
- docs: note revised Cliff 1 diagnosis posted on Sandermage issue #11 ([8d8968b](https://github.com/noonghunna/club-3090/commit/8d8968b034e11af6ad76b2ffb952c76d7846b357))
- docs: link PN12 PR #13 + record independent validation pass ([5e38365](https://github.com/noonghunna/club-3090/commit/5e383657f988e320ab2e15e44d1a509e5f839d95))
- docs: revise Cliff 1 analysis (PN12 anchor drift was the real bug) ([13d325b](https://github.com/noonghunna/club-3090/commit/13d325b1eddf8062341c5723503516389548074a))
- Document Cliff 1 205K closure ([9f6182e](https://github.com/noonghunna/club-3090/commit/9f6182edc65691fe17e83df7cc88559db084e25a))
- changelog: link P101 PR #12 in 2026-04-30 entry ([90a03ce](https://github.com/noonghunna/club-3090/commit/90a03ce2775aa08c8e972df3c6eeaf23067ace1c))
- docs: link P101 PR #12 in UPSTREAM and CLIFFS ([d0d79b1](https://github.com/noonghunna/club-3090/commit/d0d79b1c25ab334f78f1ae4530f3f2ebbed91e76))
- CLIFFS.md: post-2026-04-30 architectural-wall conclusion ([8580dc6](https://github.com/noonghunna/club-3090/commit/8580dc612dfe4be605552671448b34777993a914))
- CLIFFS.md: refine clamp formula + implementation shape (ChatGPT review) ([da6393b](https://github.com/noonghunna/club-3090/commit/da6393bb79da167a018834dff71843cff2337853))
- Add docs/CLIFFS.md — comprehensive prefill-cliff synopsis ([b0eed46](https://github.com/noonghunna/club-3090/commit/b0eed46ff7e86f54c3ca6b19803cbd996a6f83fd))
- LLAMA_CPP.md: add structural explanation of why prefill cliffs don't fire ([17aff4c](https://github.com/noonghunna/club-3090/commit/17aff4ce05d14ed56515928d31caf7ccfce72c07))
- Add docs/UPSTREAM.md + AGENTS.md (consolidate upstream tracking) ([53d811d](https://github.com/noonghunna/club-3090/commit/53d811d82b0fc09b2f5ebf2aa557718a97d9c18b))
- Add docs/COMPARISONS.md — self-host vs cloud and other local options ([297a982](https://github.com/noonghunna/club-3090/commit/297a9821f5c2f0a0489bb86490d9a21055b1357c))
- Add docs/FAQ.md — common questions answered for tweet click-throughs ([1b9374b](https://github.com/noonghunna/club-3090/commit/1b9374b8b5fd47541d168241642cddec8c3b6f04))
- Add docs/EXAMPLES.md — client snippets + IDE / Open WebUI connection ([91b817f](https://github.com/noonghunna/club-3090/commit/91b817fa72d22d54bd9ab029711d8866b008763b))
- README: lead with two-routes framing (matches launch tweet) ([710def5](https://github.com/noonghunna/club-3090/commit/710def58e421aaa2629b19495bef1f1f3bdb76cb))


### 🔧 Pin bumps + upstream

- bump Genesis pin 753344b → fc89395 (v7.66 dev tip) ([7a7efbe](https://github.com/noonghunna/club-3090/commit/7a7efbea0dfd6694abe0bcfcbdb570d85fb9a884))
- v0.20 migration + Genesis v7.65 dev tip + cold-start cache + env-var alignment ([5aa97a2](https://github.com/noonghunna/club-3090/commit/5aa97a25d910012c1a614978665e57fee53934d0))
- Genesis v7.62.x + PN8 on FP8 paths (closes Cliff 1 on tools-text) ([51a4001](https://github.com/noonghunna/club-3090/commit/51a4001af78e7e3cc7d8a0f10fe276c8f10afee6))


### 🛠️ Scripts + tooling

- ci: add Release Drafter for CalVer release notes ([c49db50](https://github.com/noonghunna/club-3090/commit/c49db508e64bb2332822b15fe54239845de7f9a2))
- power-cap-sweep: also sum delta.reasoning (third field-path) ([1528b59](https://github.com/noonghunna/club-3090/commit/1528b591c3900fde4c5fffb6af137063053947b5))
- power-cap-sweep: sum delta.reasoning_content alongside delta.content ([71e5954](https://github.com/noonghunna/club-3090/commit/71e5954ea987ece658ecfa1f232ccf3506a41fbf))
- power-cap-sweep: clamp prefill calibration to model context window ([32f924c](https://github.com/noonghunna/club-3090/commit/32f924c1c4889f26113dcf0f3ae8677339a95a08))
- power-cap-sweep: plateau auto-detection + multi-mode chain docs ([fd11ae6](https://github.com/noonghunna/club-3090/commit/fd11ae64c5dfb29ae0941e29ce96364d85d490cd))
- power-cap-sweep: add SM/mem clock + throttle% + pstate sampling ([ab2796d](https://github.com/noonghunna/club-3090/commit/ab2796dd6eaba09086f03847fa4e8c6cd9d55852))
- power-cap-sweep: time-bounded prefill-heavy + decode-concurrent (Codex round 2) ([1ede998](https://github.com/noonghunna/club-3090/commit/1ede998ced854f970018380dbf829132b3f9fe5f))
- power-cap-sweep: time-bounded streaming bench (Codex Option A redesign) ([7877c04](https://github.com/noonghunna/club-3090/commit/7877c047b55eb80a2941e6da1490389ffbb5aff3))
- power-cap-sweep: 4 cross-card portability fixes ([652103f](https://github.com/noonghunna/club-3090/commit/652103f07405535bea9c1dd659ab3610e4f86443))
- power-cap-sweep: env-overridable bench shape for decode-single mode ([c638c30](https://github.com/noonghunna/club-3090/commit/c638c305873e2a6b109302b2cae1f99fcad5ce43))
- setup.sh: auto-create .env for WSL2 boot-crash workaround (#60) ([4861ee7](https://github.com/noonghunna/club-3090/commit/4861ee7b6bfb6e337de541e44cecc30e3343b9c4))
- power-cap-sweep: --concurrency-stretch N flag for probing headroom past plateau pick ([3991ecc](https://github.com/noonghunna/club-3090/commit/3991ecc5b945fad1eaba1165e7d9a85dc6d80701))
- power-cap-sweep: plateau-detection auto-calibration (saturate headroomy GPUs) ([29e7de5](https://github.com/noonghunna/club-3090/commit/29e7de5a90ea70807c32d33ab4ebca9814f74e55))
- report.sh: engine-aware Active container probes (vllm + llamacpp) ([6fa66d2](https://github.com/noonghunna/club-3090/commit/6fa66d2f97e23563f2c5f3e7965473f3b6672d31))
- report.sh: capture recently-exited containers' boot logs (#60) ([cd980f6](https://github.com/noonghunna/club-3090/commit/cd980f64b7e7276016eae9c4cd47557ed9211ee9))
- setup.sh: add gemma-4-31b model support (#89) ([dd3bccc](https://github.com/noonghunna/club-3090/commit/dd3bcccb05f3027ca7dda6cabca962d4b7a75c5c))
- power-cap-sweep: --concurrency auto for workload-calibrated sweeps (Codex) ([f811457](https://github.com/noonghunna/club-3090/commit/f811457fffaad61c834d6c2b2b32ecca66376fa2))
- power-cap-sweep: --bench-runs N for variance mitigation (Codex) ([f99fad3](https://github.com/noonghunna/club-3090/commit/f99fad3361a577e8360c4c7a1d36531d80216c97))
- power-cap-sweep: document decode-concurrent n=1 variance caveat ([18c74de](https://github.com/noonghunna/club-3090/commit/18c74def0a6b987eecac26883bb13b2f602fe791))
- power-cap-sweep: load-mode flag + concurrent/prefill modes (Codex iteration) ([f387622](https://github.com/noonghunna/club-3090/commit/f38762251b31333a4bde463c3c1af2796bcec28c))
- verify-stress: engine-aware diagnostic hints (closes #87) ([4f01abb](https://github.com/noonghunna/club-3090/commit/4f01abb2d5fb318ee8862db51b19045257f4a69a))
- power-cap-sweep: make CONTAINER optional for host engine builds (#85, #87) ([2bb3cf7](https://github.com/noonghunna/club-3090/commit/2bb3cf72170b57de56358ca4ce4893346ebbabf0))
- scripts(verify-full, soak-test): decouple from docker/vLLM assumptions (#85, #87) ([a8606e3](https://github.com/noonghunna/club-3090/commit/a8606e34398d1c207fcfb6e6c989c2f94e766296))
- power-cap-sweep: fix stale summary footer + add compute-saturation note ([8c26c4b](https://github.com/noonghunna/club-3090/commit/8c26c4b56af0414ff8c0a499076250c6c38cefe3))
- power-cap-sweep: reduce per-cap bench to ~30s for faster sweeps ([a413321](https://github.com/noonghunna/club-3090/commit/a413321ad95667b9c767a8e56ee267657cdc690d))
- power-cap-sweep: 10W default increment + under-load median power sampling ([6d70b72](https://github.com/noonghunna/club-3090/commit/6d70b7287084cfa40dfdcf7470a8234cf8b5dbba))
- power-cap-sweep: auto-derive cap range from card's min/max power limits ([e5c7a34](https://github.com/noonghunna/club-3090/commit/e5c7a34e91e8577f61133693878f1625f92e99fc))
- Add scripts/power-cap-sweep.sh — automated cross-rig power-cap A/B (#83) ([#83](https://github.com/noonghunna/club-3090/pull/83) by @noonghunna)
- scripts: auto-detect running container + port in verify / bench (closes #52 promise) ([29718ca](https://github.com/noonghunna/club-3090/commit/29718cac994a7060e994fc85b898ffbec8fd73c1))
- verify-stress: add 3 probes to cover the bug shapes we missed ([5e745c5](https://github.com/noonghunna/club-3090/commit/5e745c5c85547c028a86fe2bcf83376d61b6c8b5))
- Add scripts/health.sh — operational health check for running server ([e7780c5](https://github.com/noonghunna/club-3090/commit/e7780c556a55f98038b287fca9314a35c88ec1a5))
- Split verify-full.sh → verify-full.sh (fast functional) + verify-stress.sh (boundary) ([5060e22](https://github.com/noonghunna/club-3090/commit/5060e22a6c25320104edf10fe799b4c2c31a2296))


### 🧹 Maintenance

- restructure: promote topology to a directory level (single/dual/multi4) ([acd7ffb](https://github.com/noonghunna/club-3090/commit/acd7ffb67c07a1df4b34ec11a7ec52087f249d96))
- Drop vllm-gemma4-mtp overlay tree (merged upstream as #41745, validated) ([aa99173](https://github.com/noonghunna/club-3090/commit/aa99173e7ad9577e6d95032b67c596c254d4ee13))
- chore(gitignore): allow results/lucebox-*/ — evidence for BENCHMARKS lucebox row ([030f780](https://github.com/noonghunna/club-3090/commit/030f780f24d5c14777ccd8e19d2788c58b7afcd8))
- chore(tools): commit residency-instrument as research tool with framing README (#41, #217) ([ed05d1c](https://github.com/noonghunna/club-3090/commit/ed05d1c35ca804a369108e18915af9e5db5bc4a1))
- chore(results): commit grammar bench evidence + gitignore investigation artifacts (#217) ([d82e898](https://github.com/noonghunna/club-3090/commit/d82e89807aefbcdf9d6b1bcf1ed83ad5f9552617))
- refactor: vendor vllm#40361 Marlin patched files in-repo (drops /opt/ai/vllm-src/ host dep) ([d8b341f](https://github.com/noonghunna/club-3090/commit/d8b341fa8cea9a7dec47c26a5f3afc81fd7e08d2))
- chore: untrack docs/diagnostics/, gitignore the path ([3f18053](https://github.com/noonghunna/club-3090/commit/3f18053659f2f2997574ed6da7317f7e5872f20e))
- Remove no-genesis-mtp.yml (research artifact, not user-facing) ([f4a28b1](https://github.com/noonghunna/club-3090/commit/f4a28b19eb4466d504dcf4e7c532e0d4fac5e967))
- Remove fast-chat.yml; extend P68/P69 disable to default ([37a4895](https://github.com/noonghunna/club-3090/commit/37a4895f6dae510e42729c6502d23e83599894a8))
- Restructure docs around hardware axis: SINGLE_CARD.md + DUAL_CARD.md ([26ac811](https://github.com/noonghunna/club-3090/commit/26ac8118de51480e6c0ecce6c8dc0ceccabc93fb))
- Audit + reconcile dual-card compose headers, patches README, setup output ([0f33561](https://github.com/noonghunna/club-3090/commit/0f33561b6bd85f890cd36d5ada7bfb489e10c6d7))


### 🧹 Other

- benchmarks: add JDWarner #107 TB3 dual-eGPU + mixed-arch row ([fa9df49](https://github.com/noonghunna/club-3090/commit/fa9df49ef2cd55f088db94dba67b3533702e9baa))
- Rename gemma-mtp-fp8.yml → gemma-mtp-int8.yml to match Ampere reality ([160e8fc](https://github.com/noonghunna/club-3090/commit/160e8fce8b5158c9870e4714f8e05bf63fa9460f))
- Two regressions caught + reframe Phase 2 around INT8 PTH (Ampere reality) ([119f296](https://github.com/noonghunna/club-3090/commit/119f2965401c19132f9c654420b742c9eb684b63))
- gemma-mtp-fp8: vendor rebased PR #40391 + stacked tool-parser fixes (#42006 + #41991) ([f93d312](https://github.com/noonghunna/club-3090/commit/f93d31215e20b195e07d4c30d2ad854852c9b7dc))
- gemma-mtp: drop PR #41745 overlay + bump to post-merge nightly ([595be8f](https://github.com/noonghunna/club-3090/commit/595be8fb8eb0442916a3570494ec5b90fc3e33f3))
- llama.cpp: --reasoning-format none default (opencode unblock, #97) ([af00ab7](https://github.com/noonghunna/club-3090/commit/af00ab7bef911ed6127ac900ecc081f9e5293ddc))
- Set dual-nvlink-dflash-noviz --max-model-len default to 188000 ([89c6862](https://github.com/noonghunna/club-3090/commit/89c686288e482a5b3529afd3af01d86157232c51))
- patches: qwen3coder tool-parser deferred-commit sidecar (#72) ([2e00b6d](https://github.com/noonghunna/club-3090/commit/2e00b6d718ea3e30fb0a0a380eaff095c39c098f))
- TQ3 composes: propagate PN34 to remaining 4 (follow-up to #82 audit) ([ab69f65](https://github.com/noonghunna/club-3090/commit/ab69f656910aa00a77da5c06aea9cd9f03041750))
- vllm/default: also enable P98 (belt+suspenders with PN34, follow-up to #82) ([2c7efe6](https://github.com/noonghunna/club-3090/commit/2c7efe61086181dfd6777bd2c1a2e55e2957d2c5))
- vllm/default: add GENESIS_ENABLE_PN34_WORKSPACE_LOCK_RELAX=1 (#82) ([3167497](https://github.com/noonghunna/club-3090/commit/3167497fef643267e42df7009272bb6c062c13fe))
- add dual-nvlink-turbo variant (rebased on v7.72.2 master, sibling-table edits dropped) (#65) ([#65](https://github.com/noonghunna/club-3090/pull/65) by @noonghunna)
- release(v7.72.2-uplift): Genesis pin + vLLM pin + sidecar consolidation (#59) ([#59](https://github.com/noonghunna/club-3090/pull/59) by @noonghunna)
- carnice-bf16mtp: restore original template + qwen3_xml parser ([d57579c](https://github.com/noonghunna/club-3090/commit/d57579c31ae6b4a42d0bf604e0e86364a2e94b85))
- carnice-bf16mtp: JSON tool format + empty think block, no reasoning parser ([a350df7](https://github.com/noonghunna/club-3090/commit/a350df7c911b8c8935980e328a7b4c57f374c70b))
- carnice-bf16mtp: add HF model URL to header ([5da50ec](https://github.com/noonghunna/club-3090/commit/5da50ec8978d64ebcefbf11637921955a6edd0e7))
- carnice-bf16mtp: formal narrative + code bench results ([7fef94f](https://github.com/noonghunna/club-3090/commit/7fef94f600a906687d60f4c4a9da85e3659d9da7))
- carnice-bf16mtp: 2 streams at 262K confirmed + formal bench numbers ([66d42c7](https://github.com/noonghunna/club-3090/commit/66d42c7940cacd011ad2468fcb1320f5384766c0))
- carnice-bf16mtp: 65K context was config choice, not VRAM ceiling — bumped to 262K ([1cf0cb2](https://github.com/noonghunna/club-3090/commit/1cf0cb288e046af486f3ace1ef2295f4944989b2))
- Carnice-V2-27B + BF16 MTP overlay — new compose variant ([bc28542](https://github.com/noonghunna/club-3090/commit/bc28542c5571c929ecee3e6371f30457855e9618))
- extend PN25 v3 + PN30 dst-shaped temp fix to all 4 TQ3 composes ([b875624](https://github.com/noonghunna/club-3090/commit/b875624f2d9ea41d6ead3a8563f9ef37ffbdb59c))
- Genesis pin d89a089 → 753344b + cross-rig validation of Sander's PN30/PN31 ([2b5ab4d](https://github.com/noonghunna/club-3090/commit/2b5ab4d0cf761e895772290ecaf45573727a0553))
- cliffs: v0.20 unblock recipe + 50K-stress-PASSES finding ([9506561](https://github.com/noonghunna/club-3090/commit/9506561ba8fdc35ef515a17275a2c94a5bec1e69))
- cliffs: document P38 silently no-op'd on TurboQuant KV path ([91355b8](https://github.com/noonghunna/club-3090/commit/91355b8fd577fc172f3f6d2af035d06b5ce08ec7))
- long-text/long-vision/bounded-thinking: middle-ground recovery 130K → 175K / 120K → 140K ([383b5cc](https://github.com/noonghunna/club-3090/commit/383b5cc38197d2ffa68a001c1e0c4c60877d99fe))
- long-text/long-vision: enable P37 + back off context for activation headroom ([1a931b4](https://github.com/noonghunna/club-3090/commit/1a931b4042090f182266aa150fa0e31d15afdbd5))
- genesis: bump pin v7.62 → v7.64 + add compile-safe FFN sidecar (#16) ([53d0663](https://github.com/noonghunna/club-3090/commit/53d0663a50c91f0a929917ae6390303842508e9e))
- Add local FA max seqlen clamp sidecar ([9f06a0f](https://github.com/noonghunna/club-3090/commit/9f06a0fe79e8e4f55b438c2e2427b8738e72d1cf))
- Fix local PN12 activation pool anchor ([41eabac](https://github.com/noonghunna/club-3090/commit/41eabac17b0b8b558121e213be1498855be314d6))
- CLIFFS: document PN12-is-partial finding (full stack still hits wall) ([537875a](https://github.com/noonghunna/club-3090/commit/537875a7fd1235ef21006ef1c5f5c2d5aabee74a))
- Add genesis #11 row to UPSTREAM.md ([bb406f9](https://github.com/noonghunna/club-3090/commit/bb406f90f16d2c59a0512b060f7af3028140e02a))
- Add Max ctx column to TL;DR + perf-summary tables on both pages ([e94c2e7](https://github.com/noonghunna/club-3090/commit/e94c2e78c4176704f4dffe93137af6f9d56f201a))
- DUAL_CARD: promote perf chart to top, parallel to SINGLE_CARD ([19fb8e7](https://github.com/noonghunna/club-3090/commit/19fb8e730f5f009f73ceef0e31ced393a2f9b2c2))
- Disable P68/P69 on long-vision, long-text, dual-turbo too ([f0cbcc6](https://github.com/noonghunna/club-3090/commit/f0cbcc6a9c9333af4dfaf6a7267ff8a93767a157))
- Disable Genesis P68/P69 in shipped composes (silent-stop bugfix) ([aab8ff4](https://github.com/noonghunna/club-3090/commit/aab8ff4a0e1eddc4c53ab24ef31ff748c54f84c8))
- Split charts per GPU-count page; chart sources land in tools/charts/ ([3742244](https://github.com/noonghunna/club-3090/commit/3742244e4d98960732569551490a64c62a23d1d8))
- Move performance chart into docs/img/ alongside vram-budget-dual ([2e3ae0c](https://github.com/noonghunna/club-3090/commit/2e3ae0c7861b4a5f74bdec0bff1b8cdca399a837))
- UX polish: pre-flight checks + cards-first wizard + PNG embeds ([abc06c3](https://github.com/noonghunna/club-3090/commit/abc06c3e3317ab2472242f8410a0d105f3631a16))
- FAQ: add VS Code Copilot LLM Gateway entry ([f275bf5](https://github.com/noonghunna/club-3090/commit/f275bf502a9ac914f011d750c1f63486ce981436))
- Add CONTRIBUTING.md — what kind of PRs land cleanly ([0c261eb](https://github.com/noonghunna/club-3090/commit/0c261ebcdfaf8bd057195d007eee28dfc5922085))
- CHANGELOG: capture post-launch polish day in cross + per-model logs ([1cc6ee6](https://github.com/noonghunna/club-3090/commit/1cc6ee6e24f991bed4a63eb084c82bea0a17bf21))
- Add launch.sh wizard + switch.sh stateless variant switcher ([4b77ed5](https://github.com/noonghunna/club-3090/commit/4b77ed5eb1eee64bbf913a332f38a54746c17d05))
- Add per-card VRAM allocation diagram + reference from model README ([88523b3](https://github.com/noonghunna/club-3090/commit/88523b3d05985476ae5bcbaeee05aab4d091319e))
- Cite Kaitchup Qwen3.6-27B GGUF eval as quant-quality lens ([b7ef91f](https://github.com/noonghunna/club-3090/commit/b7ef91f9518d5b8f521d2b850570722322c4ea3b))
- Pin Genesis to exact tested commit + add .env.example + issue templates ([ec704e4](https://github.com/noonghunna/club-3090/commit/ec704e4e2e86d8ff2ec990d8d544427f3e957dcd))
- Dual-card re-bench on club-3090 substrate + fix dual-turbo mount path ([c701474](https://github.com/noonghunna/club-3090/commit/c70147426dd241e894186f40bb3207a53f43c8df))
- dual-turbo: switch kv-cache-dtype k8v4 → 3bit_nc to align with test findings ([3e1f5f6](https://github.com/noonghunna/club-3090/commit/3e1f5f61c0475474461008a71d54ca39ddc908b5))
- Pin Genesis version + fix MODEL_DIR defaults + clean stale headers ([7f00e52](https://github.com/noonghunna/club-3090/commit/7f00e5214072491637ba7b02cdec2c9e8135b445))
- Fix .gitignore + add the entire models/ tree (initial commit was incomplete) ([2511a98](https://github.com/noonghunna/club-3090/commit/2511a981109b983d05247a485db8bdf999c6d38e))
- Initial commit — club-3090: model-agnostic LLM serving recipes for RTX 3090 ([3fa3333](https://github.com/noonghunna/club-3090/commit/3fa33332ce12b042c171fc98ad21fe412c0f92a0))



[Pin: `git checkout v2026.05.09`]

