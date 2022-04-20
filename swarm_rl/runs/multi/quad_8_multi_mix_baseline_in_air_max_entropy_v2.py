from sample_factory.runner.run_description import RunDescription, Experiment, ParamGrid
from swarm_rl.runs.quad_multi_deepsets_obstacle_baseline import QUADS_8_MULTI_NO_OBSTACLES_PARAMETERZE_CLI, seeds

_params = ParamGrid([
    ('seed', seeds(4)),
    ('quads_init_random_state', [False]),
    ('max_entropy_coeff', [0.1]),
])

BIG_MODEL_CLI = QUADS_8_MULTI_NO_OBSTACLES_PARAMETERZE_CLI + (
    ' --hidden_size=256 --quads_neighbor_hidden_size=256 --quads_obs_repr=xyz_vxyz_R_omega'
)

_experiment = Experiment(
    'max_entropy-1e-1-8_agents',
    BIG_MODEL_CLI,
    _params.generate_params(randomize=False),
)

RUN_DESCRIPTION = RunDescription('quad_multi', experiments=[_experiment])

# python -m sample_factory.runner.run --run=swarm_rl.runs.multi.quad_8_multi_mix_baseline_in_air_max_entropy --runner=processes --max_parallel=4 --pause_between=1 --experiments_per_gpu=1 --num_gpus=4