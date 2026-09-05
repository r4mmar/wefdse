import time
import random
from datetime import datetime
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.live import Live

console = Console()

def buat_tabel_data():
    # Membuat tabel untuk menampilkan data
    tabel = Table(title="📡 Monitoring Data Terkini")
    tabel.add_column("Parameter", style="cyan", no_wrap=True)
    tabel.add_column("Nilai", style="green", justify="right")
    
    # Simulasi data (nantinya bisa Anda ubah untuk menarik data dari API/Sensor sesungguhnya)
    tabel.add_row("Suhu Server", f"{random.randint(35, 60)} °C")
    tabel.add_row("Ping Jaringan", f"{random.randint(15, 40)} ms")
    tabel.add_row("Status Layanan", "[bold green]ONLINE[/bold green]")
    tabel.add_row("Trafik Data", f"{random.randint(100, 999)} KB/s")
    
    return tabel

def buat_dashboard():
    # Mengatur struktur layout (pembagian layar terminal)
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="main")
    )
    # Membelah bagian 'main' menjadi kiri dan kanan
    layout["main"].split_row(
        Layout(name="kiri"),
        Layout(name="kanan")
    )
    
    # --- Bagian Header ---
    waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header_teks = f"[bold white]🚀 MY TERMINAL DASHBOARD[/bold white] | 🕒 {waktu_sekarang}"
    layout["header"].update(Panel(header_teks, style="on blue", justify="center"))
    
    # --- Bagian Kiri (Tabel Data) ---
    layout["kiri"].update(Panel(buat_tabel_data(), title="Data Utama", border_style="cyan"))
    
    # --- Bagian Kanan (Log / Teks Informasi) ---
    log_teks = "[yellow]Log Sistem Aktif:[/yellow]\n\n"
    log_teks += "✓ Berhasil membaca file konfigurasi...\n"
    log_teks += "✓ Memuat pembaruan data jaringan...\n"
    log_teks += "✓ Sistem berjalan normal.\n\n"
    log_teks += "[dim]Tekan Ctrl+C untuk keluar dari dashboard.[/dim]"
    layout["kanan"].update(Panel(log_teks, title="Log Sistem", border_style="green"))
    
    return layout

# Menjalankan dashboard secara real-time 
if __name__ == "__main__":
    console.clear()
    try:
        # Fitur 'Live' akan me-refresh layar setiap 1 detik tanpa berkedip
        with Live(buat_dashboard(), refresh_per_second=1, console=console) as live:
            while True:
                time.sleep(1)
                live.update(buat_dashboard()) # Update tampilan secara terus-menerus
    except KeyboardInterrupt:
        console.print("\n[bold red]Dashboard ditutup.[/bold red] Sampai jumpa! 👋")
