# โครงงานวิชา CSS113 - Graph Algorithms

โปรแกรมประมวลผลข้อมูลกราฟและวิเคราะห์ด้วยอัลกอริทึมทางคอมพิวเตอร์ (DFS, BFS, Dijkstra, Prim, Kruskal)

## โครงสร้างโปรเจกต์
* `graph.py` : โครงสร้างข้อมูลกราฟ (Adjacency List & Edge List) และฟังก์ชันอ่านไฟล์
* `main.py` : ตัวควบคุมโปรแกรมและส่วนประสานงานผู้ใช้ (รองรับทั้งเมนู Interactive และ CLI Arguments)
* `input_sample.txt` : ไฟล์ตัวอย่างข้อมูลกราฟตามข้อกำหนดของโครงงาน

## วิธีติดตั้งและรันโปรแกรม

### ข้อกำหนดระบบ
* Python 3.8 ขึ้นไป (ไม่ต้องติดตั้งไลบรารีภายนอกเพิ่มเติม ใช้ Standard Library ล้วน)

### 1. วิธีรันแบบโต้ตอบ (Interactive Menu)
```bash
python main.py
```
โปรแกรมจะถามชื่อไฟล์ และแสดงเมนูให้กดเลือกตัวเลข 1-5 หรือ 0 เพื่อออกจากโปรแกรม

### 2. วิธีรันแบบส่งคำสั่งในบรรทัดเดียว (CLI Arguments)
```bash
# ทดสอบ Dijkstra (หาเส้นทางลัดจาก 0 ไป 4)
python main.py input_sample.txt --algo dijkstra --start 0 --end 4

# ทดสอบ DFS / BFS
python main.py input_sample.txt --algo dfs --start 0

# ทดสอบ Prim
python main.py input_sample.txt --algo prim --start 0

# ทดสอบ Kruskal
python main.py input_sample.txt --algo kruskal
```

## รูปแบบไฟล์ข้อมูลกราฟ (.txt)
```text
N M
u1 v1 w1
...
uM vM wM
```
* **N**: จำนวนจุดยอด (0 ถึง N-1)
* **M**: จำนวนเส้นเชื่อม
* **u v w**: จุดปลาย u, จุดปลาย v, ค่าน้ำหนัก w
