import code_generation.producer as p
from code_generation.producer import q
from config.utility import AddSystematicShift


def build_config():
    base_config = {
        "min_tau_pt": 30.0,
        "max_tau_eta": 2.3,
        "max_tau_dz": 0.2,
        "min_muon_pt": 23.0,
        "max_muon_eta": 2.5,
        "met_filters": ["Flag_goodVertices", "Flag_METFilters"],
        "tau_id": [
            "Tau_idDeepTau2017v2p1VSjet",
            "Tau_idDeepTau2017v2p1VSe",
            "Tau_idDeepTau2017v2p1VSmu",
        ],
        "tau_id_idx": [4, 4, 1],
        "muon_id": "Muon_mediumId",
        # "muon_iso": "Muon_pfRelIso04_all",
        "muon_iso_cut": 0.15,
        "require_candidate": ["nTau", "nMuon"],
        "require_candidate_number": [1, 1],
    }

    config = {"": base_config}

    config["producers"] = {
        "global": [p.MetFilter, p.GoodTaus, p.GoodMuons,],
        "mt": [
            p.MTPairSelection,
            p.GoodMTPairFilter,
            p.LVMu1,
            p.LVTau2,
            p.DiTauPairQuantities,
        ],
    }

    config["output"] = {
        "mt": [
            q.pt_1,
            q.pt_2,
        ]
    }

    shift_dict = {"min_tau_pt": 31.0}
    AddSystematicShift(config, "tauCutUp", shift_dict, [p.TauPtCut])

    return config
