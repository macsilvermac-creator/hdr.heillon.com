
with open('C:/hdr.heillon.com/index.html', encoding='utf-8') as f:
    c = f.read()

# Adicionar 3-step onboarding + contact box depois do paragrafo da secção adopt
# Encontrar o final da secção adopt para inserir os steps
old_para_end = '<span data-en>Any organization can verify HDR artifacts'

# Inserir 3 passos depois do h2/p da secção adopt
steps_html = '''
    <!-- 3-step onboarding -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1rem;margin:2rem 0">
      <div style="background:rgba(0,217,126,.04);border:1px solid rgba(0,217,126,.15);border-radius:10px;padding:1.5rem">
        <div style="font-family:var(--font-mono);font-size:.6rem;letter-spacing:.2em;color:rgba(0,217,126,.6);margin-bottom:.6rem">PASSO 01</div>
        <div style="font-size:1rem;font-weight:600;color:#E8E4D9;margin-bottom:.5rem">Ler RFC-0001</div>
        <p style="font-size:.83rem;color:#5A6478;line-height:1.6;margin-bottom:.9rem">A especificacao completa do HDR. Gratuita, publica, para sempre.</p>
        <a href="#rfc" style="font-family:var(--font-mono);font-size:.7rem;color:rgba(0,217,126,.8);text-decoration:none">Ver RFC-0001 &rarr;</a>
      </div>
      <div style="background:rgba(201,168,76,.04);border:1px solid rgba(201,168,76,.15);border-radius:10px;padding:1.5rem">
        <div style="font-family:var(--font-mono);font-size:.6rem;letter-spacing:.2em;color:rgba(201,168,76,.6);margin-bottom:.6rem">PASSO 02</div>
        <div style="font-size:1rem;font-weight:600;color:#E8E4D9;margin-bottom:.5rem">Verificar ao vivo</div>
        <p style="font-size:.83rem;color:#5A6478;line-height:1.6;margin-bottom:.9rem">Testa o protocolo com um HDR real. Sem conta, sem login. Em 30 segundos.</p>
        <a href="#verify" style="font-family:var(--font-mono);font-size:.7rem;color:rgba(201,168,76,.8);text-decoration:none">Abrir verificador &rarr;</a>
      </div>
      <div style="background:rgba(123,127,196,.04);border:1px solid rgba(123,127,196,.15);border-radius:10px;padding:1.5rem">
        <div style="font-family:var(--font-mono);font-size:.6rem;letter-spacing:.2em;color:rgba(123,127,196,.6);margin-bottom:.6rem">PASSO 03</div>
        <div style="font-size:1rem;font-weight:600;color:#E8E4D9;margin-bottom:.5rem">Integrar via API</div>
        <p style="font-size:.83rem;color:#5A6478;line-height:1.6;margin-bottom:.9rem">1 endpoint POST /lc2s/execute. Qualquer linguagem. O teu sistema nao muda.</p>
        <a href="https://heillon.com/#cta" style="font-family:var(--font-mono);font-size:.7rem;color:rgba(123,127,196,.8);text-decoration:none">Falar com equipa &rarr;</a>
      </div>
    </div>
    <!-- Dev contact box -->
    <div style="background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.07);border-radius:10px;padding:1.5rem;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1rem;margin-top:.5rem">
      <div>
        <p style="font-family:var(--font-mono);font-size:.68rem;color:#5A6478;margin-bottom:.3rem">A integrar? Fala connosco directamente.</p>
        <p style="font-size:.85rem;color:#E8E4D9">Suporte tecnico para developers e arquitectos.</p>
      </div>
      <a href="mailto:contact@heillon.com?subject=HDR%20API%20Integration" style="font-family:var(--font-mono);font-size:.72rem;letter-spacing:.08em;padding:.65rem 1.4rem;background:rgba(201,168,76,.12);border:1px solid rgba(201,168,76,.35);color:#C9A84C;text-decoration:none;border-radius:5px;white-space:nowrap">contact@heillon.com &rarr;</a>
    </div>
    <span data-en>Any organization can verify HDR artifacts'''

c2 = c.replace('<span data-en>Any organization can verify HDR artifacts', steps_html, 1)

print('Steps injected:', '3-step onboarding' in c2)
print('Dev contact box:', 'Dev contact box' in c2)

with open('C:/hdr.heillon.com/index.html', 'w', encoding='utf-8') as f:
    f.write(c2)
print('Saved hdr')
