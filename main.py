import sys
import argparse
from graph import load_graph_from_file, Graph

def run_menu_mode(graph: Graph):
    """โหมดเมนู Interactive: ให้ผู้ใช้กดเลือกตัวเลขใน Terminal"""
    while True:
        print("\n" + "=" * 45)
        print("                 เมนูอัลกอริทึม                ")
        print("=" * 45)
        print("1. DFS & BFS (คนที่ 2 ทำ)")
        print("2. Dijkstra - หาเส้นทางสั้นสุด (คนที่ 2 ทำ)")
        print("3. Prim - หา Minimum Spanning Tree (คนที่ 3 ทำ)")
        print("4. Kruskal - หา Minimum Spanning Tree (คนที่ 3 ทำ)")
        print("5. ดูโครงสร้างกราฟ (Adjacency & Edge List)")
        print("0. ออกจากโปรแกรม")
        print("-" * 45)

        choice = input("กรุณาเลือกเมนู (0-5): ").strip()

        if choice == '1':
            try:
                start = int(input(f"ระบุจุดเริ่มต้น (0 ถึง {graph.num_vertices - 1}): "))
                if not (0 <= start < graph.num_vertices):
                    print("❌ จุดยอดอยู่นอกช่วง!")
                    continue
                print(f"\n[เรียกฟังก์ชัน DFS & BFS] เริ่มที่จุดยอด: {start}")
                # TODO (คนที่ 2): dfs_bfs(graph, start)
            except ValueError:
                print("❌ กรุณาป้อนตัวเลขจำนวนเต็ม")

        elif choice == '2':
            try:
                src = int(input(f"ระบุจุดต้นทาง (0 ถึง {graph.num_vertices - 1}): "))
                dest = int(input(f"ระบุจุดปลายทาง (0 ถึง {graph.num_vertices - 1}): "))
                if not (0 <= src < graph.num_vertices and 0 <= dest < graph.num_vertices):
                    print("❌ จุดยอดอยู่นอกช่วง!")
                    continue
                print(f"\n[เรียกฟังก์ชัน Dijkstra] จากจุด {src} ไปยัง {dest}")
                # TODO (คนที่ 2): dijkstra(graph, src, dest)
            except ValueError:
                print("❌ กรุณาป้อนตัวเลขจำนวนเต็ม")

        elif choice == '3':
            try:
                start = int(input(f"ระบุจุดเริ่มต้น (0 ถึง {graph.num_vertices - 1}): "))
                if not (0 <= start < graph.num_vertices):
                    print("❌ จุดยอดอยู่นอกช่วง!")
                    continue
                print(f"\n[เรียกฟังก์ชัน Prim] เริ่มที่จุดยอด: {start}")
                # TODO (คนที่ 3): prim(graph, start)
            except ValueError:
                print("❌ กรุณาป้อนตัวเลขจำนวนเต็ม")

        elif choice == '4':
            print("\n[เรียกฟังก์ชัน Kruskal] ไม่ต้องระบุจุดเริ่มต้น")
            # TODO (คนที่ 3): kruskal(graph)

        elif choice == '5':
            print("\n📌 โครงสร้างกราฟปัจจุบัน:")
            print("\n[Adjacency List]")
            for u, neighbors in graph.adj_list.items():
                print(f"  จุด {u} เชื่อมกับ -> {neighbors}")
            print("\n[Edge List]")
            for u, v, w in graph.edge_list:
                print(f"  เส้น ({u} - {v}) ค่าน้ำหนัก: {w}")

        elif choice == '0':
            print("\n👋 จบการทำงาน ขอบคุณครับ!")
            break
        else:
            print("❌ เลือกเมนูไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง")


def run_cli_args_mode(args, graph: Graph):
    """โหมด Command-Line Arguments: ทำงานตามคำสั่งที่ส่งเข้ามาทาง Terminal ทันที"""
    algo = args.algo.lower()
    
    if algo in ['dfs', 'bfs', 'dfs_bfs']:
        if args.start is None:
            print("❌ โปรดระบุจุดเริ่มต้นด้วย --start <node>")
            return
        print(f"🚀 รัน {algo.upper()} | จุดเริ่มต้น: {args.start}")
        # TODO (คนที่ 2): เรียก dfs/bfs

    elif algo == 'dijkstra':
        if args.start is None or args.end is None:
            print("❌ โปรดระบุต้นทางและปลายทางด้วย --start <node> --end <node>")
            return
        print(f"🚀 รัน Dijkstra | จากจุด: {args.start} -> ปลายทาง: {args.end}")
        # TODO (คนที่ 2): เรียก dijkstra

    elif algo == 'prim':
        if args.start is None:
            print("❌ โปรดระบุจุดเริ่มต้นด้วย --start <node>")
            return
        print(f"🚀 รัน Prim | จุดเริ่มต้น: {args.start}")
        # TODO (คนที่ 3): เรียก prim

    elif algo == 'kruskal':
        print(f"🚀 รัน Kruskal (ไม่ต้องระบุจุดเริ่มต้น)")
        # TODO (คนที่ 3): เรียก kruskal

    else:
        print(f"❌ ไม่รู้จักอัลกอริทึม '{args.algo}' (เลือกได้: dfs, bfs, dijkstra, prim, kruskal)")


def main():
    parser = argparse.ArgumentParser(description="CSS113 Graph Algorithms Project")
    parser.add_argument("file", nargs="?", help="ที่อยู่ไฟล์ข้อมูลกราฟ (.txt)")
    parser.add_argument("--algo", choices=["dfs", "bfs", "dfs_bfs", "dijkstra", "prim", "kruskal"], help="อัลกอริทึมที่ต้องการรัน")
    parser.add_argument("--start", type=int, help="จุดยอดเริ่มต้น (สำหรับ DFS, BFS, Dijkstra, Prim)")
    parser.add_argument("--end", type=int, help="จุดยอดปลายทาง (สำหรับ Dijkstra)")

    args = parser.parse_args()

    # ถ้าไม่ได้ระบุชื่อไฟล์ผ่านอาร์กิวเมนต์ ให้ถามใน Terminal
    filepath = args.file
    if not filepath:
        print("========================================")
        print("      CSS113 Graph Algorithms Project   ")
        print("========================================")
        filepath = input("กรุณาใส่ชื่อหรือที่อยู่ไฟล์กราฟ (เช่น input_sample.txt): ").strip()

    graph = load_graph_from_file(filepath)
    if not graph:
        sys.exit(1)

    # เลือกว่าจะทำงานแบบ CLI Arguments หรือ Interactive Menu
    if args.algo:
        run_cli_args_mode(args, graph)
    else:
        run_menu_mode(graph)


if __name__ == "__main__":
    main()
