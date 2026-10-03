from .chittorgarh import get_mainboard_ipos
from .telegram import send_message

def main():
    rows=get_mainboard_ipos()
    if not rows: send_message('⚠️ Could not extract IPO dashboard data today.'); return
    lines=['<b>📊 Mainboard IPO Update</b>','']
    for row in rows[:30]: lines.append(' | '.join(row))
    send_message('\n'.join(lines))
if __name__=='__main__': main()
