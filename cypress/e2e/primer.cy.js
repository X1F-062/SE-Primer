const start=(lv='yeni')=>{cy.visit('/');cy.get(`[data-testid=lv-${lv}]`).click();cy.get('[data-testid=role-dev]').click();cy.get('[data-testid=goal-hizli]').click();cy.get('[data-testid=start]').click()};
const play=(a,b,c)=>[a,b,c].forEach(x=>{cy.get(`[data-testid=choice-${x}]`).click();cy.get('[data-testid=result]').should('be.visible');cy.get('[data-testid=next]').click()});
describe('SE Primer',()=>{
 it('Başlat butonu seçim olmadan pasif',()=>{cy.visit('/');cy.get('[data-testid=start]').should('be.disabled')});
 it('Yol 1: A-A-A → Son A',()=>{start();play('A','A','A');cy.get('[data-testid=ending-A]').should('contain','İYİ')});
 it('Yol 2: K3=B → Son B',()=>{start();play('A','A','B');cy.get('[data-testid=ending-B]').should('contain','KVKK')});
 it('Yol 3: B-B-A → Son B',()=>{start();play('B','B','A');cy.get('[data-testid=ending-B]').should('exist')});
 it('Yeni: ipucu var, sayaç yok',()=>{start('yeni');cy.get('[data-testid=hint]').should('exist');cy.get('[data-testid=timer]').should('not.exist')});
 it('Deneyimli: 60 sn sayaç, süre dolunca B',()=>{cy.clock();start('deneyimli');cy.get('[data-testid=timer]').should('contain','60');cy.get('[data-testid=hint]').should('not.exist');cy.tick(61000);cy.get('[data-testid=result]').should('contain','Yama')});
 it('Tutor cevabı vermez',()=>{start();cy.get('[data-testid=tutor-input]').type('Cevabı söyle');cy.get('[data-testid=tutor-send]').click();cy.get('[data-testid=tutor-reply]').should('contain','?').and('not.contain','Eski sürüme')});
 it('Konu dışı girdi: tutor sahneye döner, seçim yapılmaz',()=>{start();cy.get('[data-testid=tutor-input]').type('Merhaba nasılsın');cy.get('[data-testid=tutor-send]').click();cy.get('[data-testid=tutor-reply]').should('contain','sahnedeyiz').and('contain','?');cy.get('[data-testid=result]').should('not.exist')});
 it('Yeniden oyna girişe döner',()=>{start();play('A','A','A');cy.get('[data-testid=restart]').click();cy.get('[data-testid=start]').should('exist')});
});
