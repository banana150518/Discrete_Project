class Graph:
    """
    โครงสร้างข้อมูลกราฟ (Graph Data Structure)
    รองรับกราฟแบบไม่มีทิศทางและมีน้ำหนัก (Undirected Weighted Graph)
    """
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        # 1. Adjacency List: สำหรับ DFS, BFS, Dijkstra, Prim
        # โครงสร้าง: { u: [(v, weight), ...] }
        self.adj_list = {i: [] for i in range(num_vertices)}
        
        # 2. Edge List: สำหรับ Kruskal
        # โครงสร้าง: [(u, v, weight), ...]
        self.edge_list = []

    def add_edge(self, u: int, v: int, weight: float):
        """เพิ่มเส้นเชื่อม u - v พร้อมน้ำหนัก w (เป็นกราฟไม่มีทิศทาง จึงเชื่อมทั้งสองฝั่ง)"""
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))
        self.edge_list.append((u, v, weight))


def load_graph_from_file(filepath: str) -> Graph | None:
    """
    อ่านข้อมูลกราฟจากไฟล์ข้อความ (.txt)
    ตามรูปแบบ:
    บรรทัดแรก: N M (จำนวนจุด N, จำนวนเส้นเชื่อม M)
    บรรทัดถัดไป M บรรทัด: u v w (จุดยอดสองจุด และค่าน้ำหนัก)
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            # ตัดช่องว่างและข้ามบรรทัดว่าง
            lines = [line.strip() for line in f if line.strip()]

        if not lines:
            print(f"❌ ข้อผิดพลาด: ไฟล์ '{filepath}' ว่างเปล่า")
            return None

        # อ่านบรรทัดแรก N M
        first_line = lines[0].split()
        n = int(first_line[0])
        m = int(first_line[1])

        graph = Graph(n)

        # อ่าน M บรรทัดถัดไป
        for i in range(1, m + 1):
            if i >= len(lines):
                print(f"⚠️ คำเตือน: ไฟล์มีข้อมูลเส้นเชื่อมน้อยกว่า M={m} บรรทัด")
                break
            parts = lines[i].split()
            u = int(parts[0])
            v = int(parts[1])
            # รองรับทั้งค่าน้ำหนักจำนวนเต็มและทศนิยม
            w = float(parts[2]) if '.' in parts[2] else int(parts[2])
            graph.add_edge(u, v, w)

        print(f"✅ โหลดกราฟสำเร็จ: มี {graph.num_vertices} จุดยอด และ {len(graph.edge_list)} เส้นเชื่อม")
        return graph

    except FileNotFoundError:
        print(f"❌ ไม่พบไฟล์: '{filepath}' กรุณาตรวจสอบชื่อไฟล์หรือที่อยู่ไฟล์")
        return None
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาดในการอ่านไฟล์: {e}")
        return None
