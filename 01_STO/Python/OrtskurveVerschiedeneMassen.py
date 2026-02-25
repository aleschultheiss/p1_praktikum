import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc


def plot_collision_diagram(mp, mt, v0=1.0):
    vs = v0 * (mp / (mp + mt))
    

    up = v0 * (mt / (mp + mt))
    ut = vs
    
    Rp = up
    Rt = ut

    fig, ax = plt.subplots(figsize=(8, 8))
    
    circle_p = plt.Circle((vs, 0), Rp, color='blue', fill=False, label='$v_p$ Ortskurve (Projektil)', linewidth=1.5)
    circle_t = plt.Circle((vs, 0), Rt, color='green', fill=False, label='$v_t$ Ortskurve (Target)', linewidth=1.5)
    ax.add_artist(circle_p)
    ax.add_artist(circle_t)

    angles = np.linspace(0, np.pi, 8, endpoint=False)
    
    for theta in angles:
        vpx = vs + Rp * np.cos(theta)
        vpy = Rp * np.sin(theta)
        ax.quiver(0, 0, vpx, vpy, angles='xy', scale_units='xy', scale=1, 
                  alpha=0.6, width=0.005, color='darkblue')
        
        vtx = vs + Rt * np.cos(theta + np.pi)
        vty = Rt * np.sin(theta + np.pi)
        ax.quiver(0, 0, vtx, vty, angles='xy', scale_units='xy', scale=1, 
                  alpha=0.6, width=0.005, color='darkgreen')

        arc_radius = 0.2 + (theta * 0.1) 

        angle_p = np.degrees(np.arctan2(vpy, vpx))
        angle_t = np.degrees(np.arctan2(vty, vtx))
        
        arc = Arc((0, 0), arc_radius, arc_radius, angle=0, 
                  theta1=angle_t, theta2=angle_p, color='red', lw=1.5, alpha=0.7)
        if theta > 0:
            ax.add_patch(arc)

    limit = max(vs + Rp, vs + Rt) * 1.2
    ax.set_xlim(-limit * 0.2, limit)
    ax.set_ylim(-limit/2, limit/2)
    ax.axhline(0, color='black', lw=1)
    ax.set_aspect('equal')
    ax.set_title(f'Elastischer Stoss: $m_p={mp}, m_t={mt}$')
    ax.legend(loc='upper right')
    
    plt.grid(True, linestyle='--', alpha=0.5)

    if mp < mt:
        relation = '<'
    elif mp > mt:
        relation = '>'
    else:
        relation = '='

    plt.savefig(f'Ortskurve_m_p_{relation}_m_t.png', dpi=1000, bbox_inches='tight')


plot_collision_diagram(mp=0.8, mt=1)
plot_collision_diagram(mp=1, mt=1)
plot_collision_diagram(mp=1, mt=0.8)