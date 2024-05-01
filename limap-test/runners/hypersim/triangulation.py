import os, sys
import numpy as np
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Hypersim import Hypersim
from loader import read_scene_hypersim

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import limap.util.config as cfgutils
import limap.runners
import limap.visualize as limapvis

def run_scene_hypersim(cfg, dataset, scene_id, img_count, cam_id=0):
    imagecols = read_scene_hypersim(cfg, dataset, scene_id, img_count, cam_id=cam_id, load_depth=False)
    linetracks = limap.runners.line_triangulation(cfg, imagecols)
    return linetracks

def parse_config():
    import argparse
    arg_parser = argparse.ArgumentParser(description='triangulate 3d lines')
    arg_parser.add_argument('-c', '--config_file', type=str, default='cfgs/triangulation/hypersim.yaml', help='config file')
    arg_parser.add_argument('--default_config_file', type=str, default='cfgs/triangulation/default.yaml', help='default config file')
    arg_parser.add_argument('--npyfolder', type=str, default=None, help='folder to load precomputed results')

    args, unknown = arg_parser.parse_known_args()
    cfg = cfgutils.load_config(args.config_file, default_path=args.default_config_file)
    shortcuts = dict()
    shortcuts['-nv'] = '--n_visible_views'
    shortcuts['-nn'] = '--n_neighbors'
    shortcuts['-sid'] = '--scene_id'
    cfg = cfgutils.update_config(cfg, unknown, shortcuts)
    cfg["folder_to_load"] = args.npyfolder
    if cfg["folder_to_load"] is None:
        cfg["folder_to_load"] = os.path.join("precomputed", "hypersim", cfg["scene_id"])
    return cfg

def main():

    start_time = time.time()
    img_count = 0
    cfg = parse_config()
    dataset = Hypersim(cfg["data_dir"])
    linetracks = None
    imagecols = None

    while img_count < 100:
        img_count +=5                                                           #加入建模的圖片張數
        linetracks, imagecols = run_scene_hypersim(cfg, dataset, cfg["scene_id"], img_count, cam_id=cfg["cam_id"])

    print("--- %s seconds ---" % (time.time() - start_time))
    
    VisTrack = limapvis.Open3DTrackVisualizer(linetracks)
    import pdb
    pdb.set_trace()
    VisTrack.vis_reconstruction(imagecols, n_visible_views=cfg["n_visible_views"], width=2)
    pdb.set_trace()

if __name__ == '__main__':
    main()

