
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('C:/hdr.heillon.com/index.html', encoding='utf-8') as f:
    content = f.read()

# Find the closing </section> after adopt section and add contact box before it
adopt_close = content.find('</section>', content.find('id="adopt"'))
print('Adopt section closes at:', adopt_close)

contact_box = '''
  <!-- Contact CTA box -->
  <div style="margin-top:3rem;background:linear-gradient(135deg,rgba(10,14,24,.95),rgba(14,20,35,.95));border:1px solid rgba(201,168,76,.22);border-radius:14px;padding:2.5rem;max-width:640px">
    <p style="font-family:'IBM Plex Mono',monospace;font-size:.62rem;letter-spacing:.22em;color:rgba(201,168,76,.7);text-transform:uppercase;margin-bottom:.6rem">Proximo passo</p>
    <h3 style="font-size:clamp(1.2rem,2.5vw,1.7rem);font-weight:300;color:#E8E4D9;margin-bottom:.75rem;line-height:1.3">
      <span data-pt>O seu sistema gera decisions?<br>A HEILLON faz com que elas provem que existiram.</span>
      <span data-en style="display:none">Does your system make decisions?<br>HEILLON makes them cryptographically provable.</span>
    </h3>
    <p style="font-size:.88rem;color:#6A7590;margin-bottom:1.6rem;line-height:1.7">
      <span data-pt>Um endpoint. Sem migracao. Sem mudancas na sua stack. A prova comeca no primeiro request.</span>
      <span data-en style="display:none">One endpoint. No migration. No stack changes. Proof starts from the first request.</span>
    </p>
    <div style="display:flex;gap:.85rem;flex-wrap:wrap;align-items:center">
      <a href="https://vitrine.heillon.com" style="padding:.65rem 1.6rem;background:rgba(201,168,76,.12);border:1px solid rgba(201,168,76,.35);border-radius:7px;font-family:'IBM Plex Mono',monospace;font-size:.72rem;letter-spacing:.1em;color:#C9A84C;text-decoration:none;text-transform:uppercase">
        <span data-pt>Ver infraestrutura</span><span data-en style="display:none">See infrastructure</span> &#8594;
      </a>
      <a href="mailto:contact@heillon.com?subject=HDR%20Integration%20Request" style="padding:.65rem 1.4rem;background:transparent;border:1px solid rgba(255,255,255,.1);border-radius:7px;font-family:'IBM Plex Mono',monospace;font-size:.72rem;letter-spacing:.1em;color:#8A95A8;text-decoration:none;text-transform:uppercase">
        contact@heillon.com
      </a>
    </div>
  </div>
'''

new_content = content[:adopt_close] + contact_box + '\n' + content[adopt_close:]
print('Contact box injected:', 'Proximo passo' in new_content)

with open('C:/hdr.heillon.com/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Saved OK')
