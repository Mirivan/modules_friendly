from .. import loader
import asyncio
from collections import deque
@loader.tds
class LoveMirMod(loader.Module):
	strings = {"name": "Love (Mirivan)"}
	@loader.owner
	async def lovemircmd(self, message):
		deq = deque(list('❤️🧡💛💚💙💜🖤🤍'))
        try:
            for _ in range(48):
                await asyncio.sleep(0.5)
                await event.edit(''.join(deq))
                deq.rotate(1)
        except Exception:
        	pass
