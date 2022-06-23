import unittest

from torchmimic.benchmarks import (
    IHMBenchmark,
    DecompensationBenchmark,
    LOSBenchmark,
    PhenotypingBenchmark
)
# from torchmimic.benchmarks.multitask import Multitask_Trainer


from torchmimic.models import StandardLSTM

from torchmimic.utils import get_free_gpu


class TestLSTM(unittest.TestCase):
    def test_standard_lstm_phenotype(self):
        device = get_free_gpu()

        model = StandardLSTM(
            n_classes=25,
            hidden_dim=256,
            num_layers=1,
            dropout_rate=0.3,
            bidirectional=True,
        )

        trainer = PhenotypingBenchmark(
            model=model,
            train_batch_size=8,
            test_batch_size=256,
            data="/data/datasets/mimic3-benchmarks/data/phenotyping",
            learning_rate=0.001,
            weight_decay=0,
            report_freq=200,
            device=device,
            sample_size=1000,
        )

        trainer.fit(2)

    def test_standard_lstm_ihm(self):
        device = get_free_gpu()

        model = StandardLSTM(
            n_classes=1,
            hidden_dim=256,
            num_layers=1,
            dropout_rate=0.3,
            bidirectional=True,
        )

        trainer = IHMBenchmark(
            model=model,
            train_batch_size=8,
            test_batch_size=256,
            data="/data/datasets/mimic3-benchmarks/data/in-hospital-mortality",
            learning_rate=0.001,
            weight_decay=0,
            report_freq=200,
            device=device,
            sample_size=1000,
        )

        trainer.fit(2)

    def test_standard_lstm_los(self):
        device = get_free_gpu()

        model = StandardLSTM(
            n_classes=10,
            hidden_dim=256,
            num_layers=1,
            dropout_rate=0.3,
            bidirectional=True,
        )

        trainer = LOSBenchmark(
            model=model,
            train_batch_size=8,
            test_batch_size=256,
            data="/data/datasets/mimic3-benchmarks/data/length-of-stay",
            learning_rate=0.001,
            weight_decay=0,
            report_freq=200,
            device=device,
            sample_size=20,
            partition=10,
        )

        trainer.fit(2)

    def test_standard_lstm_decomp(self):
        device = get_free_gpu()

        model = StandardLSTM(
            n_classes=1,
            hidden_dim=256,
            num_layers=1,
            dropout_rate=0.3,
            bidirectional=True,
        )

        trainer = DecompensationBenchmark(
            model=model,
            train_batch_size=8,
            test_batch_size=256,
            data="/data/datasets/mimic3-benchmarks/data/decompensation",
            learning_rate=0.001,
            weight_decay=0,
            report_freq=200,
            device=device,
            sample_size=1000,
            partition=10,
        )

        trainer.fit(2)
        
    # def test_standard_lstm_multi(self):
    #     device = get_free_gpu()

#         model = StandardLSTM(
#             n_classes=1,
#             hidden_dim=256,
#             num_layers=1,
#             dropout_rate=0.3,
#             bidirectional=True,
#         )

#         trainer = Multitask_Trainer(
#             model=model,
#             train_batch_size=8,
#             test_batch_size=256,
#             data="/data/datasets/mimic3-benchmarks/data/multitask",
#             learning_rate=0.001,
#             weight_decay=0,
#             report_freq=200,
#             device=device,
#             small_part=True,
#             partition=10,
#         )

#         trainer.fit(2)
