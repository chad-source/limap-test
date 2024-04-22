import os, sys
import shutil
import numpy as np
from scipy.fft import dst
import time

import limap.base as _base
import limap.util.io as limapio
import limap.visualize as limapvis

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'runners/hypersim'))
from Hypersim import Hypersim
from loader import read_scene_hypersim

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import limap.util.config as cfgutils
import limap.runners

def run_scene_hypersim(cfg, dataset, scene_id, cam_id=0):
    imagecols = read_scene_hypersim(cfg, dataset, scene_id, cam_id=cam_id, load_depth=False)
    linetracks = limap.runners.line_triangulation(cfg, imagecols)
    return linetracks

def parse_config_triangulation():
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

def parse_args_3d_lines():
    import argparse
    arg_parser = argparse.ArgumentParser(description='visualize 3d lines')
    arg_parser.add_argument('-i', '--input_dir', type=str,default= 'outputs/quickstart_triangulation/finaltracks', required=None, help='input line file. Format supported now: .obj, .npy, linetrack folder.')
    arg_parser.add_argument('-nv', '--n_visible_views', type=int, default=2, help='number of visible views')
    arg_parser.add_argument('--imagecols', type=str, default=None, help=".npy file for imagecols")
    arg_parser.add_argument("--metainfos", type=str, default=None, help=".txt file for neighbors and ranges")
    arg_parser.add_argument('--mode', type=str, default="open3d", help="[pyvista, open3d]")
    arg_parser.add_argument('--use_robust_ranges', action='store_true', help="whether to use computed robust ranges")
    arg_parser.add_argument('--scale', type=float, default=1.0, help="scaling both the lines and the camera geometry")
    arg_parser.add_argument('--cam_scale', type=float, default=1.0, help="scale of the camera geometry")
    arg_parser.add_argument('--output_dir', type=str, default=None, help="if set, save the scaled lines in obj format")
    args = arg_parser.parse_args()
    return args

def vis_3d_lines(lines, mode="open3d", ranges=None, scale=1.0):
    if mode == "pyvista":
        limapvis.pyvista_vis_3d_lines(lines, ranges=ranges, scale=scale)
    elif mode == "open3d":
        limapvis.open3d_vis_3d_lines(lines, ranges=ranges, scale=scale)
    else:
        raise NotImplementedError

def vis_reconstruction(linetracks, imagecols, mode="open3d", n_visible_views=4, ranges=None, scale=1.0, cam_scale=1.0):
    if mode == "open3d":
        VisTrack = limapvis.Open3DTrackVisualizer(linetracks)
    else:
        raise ValueError("Error! Visualization with cameras is only supported with open3d.")
    VisTrack.report()
    VisTrack.vis_reconstruction(imagecols, n_visible_views=n_visible_views, ranges=ranges, scale=scale, cam_scale=cam_scale)

def main():

    src_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "original_image", "images")
    dst_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "ai_001_001", "images")

    start_time = time.time()
    count = 0

    while(count < 100):
        for num, folder in enumerate(os.listdir(src_folder)):
            temp = 0
            if num == 0:
                for index, filename in enumerate(os.listdir(os.path.join(src_folder, folder))):
                    if (index / 4) < count:
                        continue
                    else:
                        if temp < 20:
                            src_path = os.path.join(os.path.join(src_folder, folder), filename)
                            dst_path = os.path.join(os.path.join(dst_folder, folder), filename)
                            shutil.copy(src_path, dst_path)
                            temp += 1
                        else:
                            break
            elif num == 1:
                for index, filename in enumerate(os.listdir(os.path.join(src_folder, folder))):
                    if (index / 9) < count:
                        continue
                    else:
                        if temp < 45:
                            src_path = os.path.join(os.path.join(src_folder, folder), filename)
                            dst_path = os.path.join(os.path.join(dst_folder, folder), filename)
                            shutil.copy(src_path, dst_path)
                            temp += 1
                        else:
                            break
            elif num == 2:
                for index, filename in enumerate(os.listdir(os.path.join(src_folder, folder))):
                    if (index / 10) < count:
                        continue
                    else:
                        if temp < 50:
                            src_path = os.path.join(os.path.join(src_folder, folder), filename)
                            dst_path = os.path.join(os.path.join(dst_folder, folder), filename)
                            shutil.copy(src_path, dst_path)
                            temp += 1
                        else:
                            break
            else:
                for index, filename in enumerate(os.listdir(os.path.join(src_folder, folder))):
                    if (index / 11) < count:
                        continue
                    else:
                        if temp < 55:
                            src_path = os.path.join(os.path.join(src_folder, folder), filename)
                            dst_path = os.path.join(os.path.join(dst_folder, folder), filename)
                            shutil.copy(src_path, dst_path)
                            temp += 1
                        else:
                            break
        count += 5

        

        cfg = parse_config_triangulation()
        dataset = Hypersim(cfg["data_dir"])
        run_scene_hypersim(cfg, dataset, cfg["scene_id"], cam_id=cfg["cam_id"])

        args = parse_args_3d_lines()
        lines, linetracks = limapio.read_lines_from_input(args.input_dir)
        ranges = None
        if args.metainfos is not None:
            _, ranges = limapio.read_txt_metainfos(args.metainfos)
        if args.use_robust_ranges:
            ranges = limapvis.compute_robust_range_lines(lines)
        if args.n_visible_views > 2 and linetracks is None:
            raise ValueError("Error! Track information is not available.")
        if count == 100:
            print("--- %s seconds ---" % (time.time() - start_time))
            if args.imagecols is None:
                vis_3d_lines(lines, mode=args.mode, ranges=ranges, scale=args.scale)
            else:
                if (not os.path.exists(args.imagecols)) or (not args.imagecols.endswith('.npy')):
                    raise ValueError("Error! Input file {0} is not valid".format(args.imagecols))
                imagecols = _base.ImageCollection(limapio.read_npy(args.imagecols).item())
                vis_reconstruction(linetracks, imagecols, mode=args.mode, n_visible_views=args.n_visible_views, ranges=ranges, scale=args.scale, cam_scale=args.cam_scale)
        if args.output_dir is not None:
            limapio.save_obj(args.output_dir, lines)


if __name__ == '__main__':
    main()
